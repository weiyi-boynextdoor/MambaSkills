"""Generate ecommerce ad videos with Veo from a video-director prompt."""

from __future__ import annotations

import argparse
import mimetypes
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai.types import (
	GenerateVideosConfig,
	GenerateVideosSource,
	Image,
	VideoGenerationReferenceImage,
	VideoGenerationReferenceType,
)


DEFAULT_MODEL = "veo-3.1-generate-001"
DEFAULT_ASPECT_RATIO = "16:9"
DEFAULT_POLL_SECONDS = 15


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(
		description="Generate a Veo advertising video from a MambaSalesman video-director prompt.",
	)
	prompt_group = parser.add_mutually_exclusive_group(required=True)
	prompt_group.add_argument("--prompt", help="Production-ready English video prompt.")
	prompt_group.add_argument("--prompt-file", type=Path, help="UTF-8 text file containing the video prompt.")
	parser.add_argument(
		"--reference-image",
		action="append",
		default=[],
		metavar="PATH[:MIME_TYPE]",
		help="Reference image for product, model, scene, or brand assets. Repeat for multiple images.",
	)
	parser.add_argument("--output", type=Path, default=Path("outputs") / "veo-output.mp4")
	parser.add_argument("--model", default=DEFAULT_MODEL)
	parser.add_argument("--aspect-ratio", default=DEFAULT_ASPECT_RATIO)
	parser.add_argument("--poll-seconds", type=int, default=DEFAULT_POLL_SECONDS)
	parser.add_argument(
		"--env-file",
		type=Path,
		default=Path(__file__).resolve().parents[1] / ".env",
		help="Path to a .env file with Google GenAI or Vertex AI environment variables.",
	)
	return parser.parse_args()


def read_prompt(args: argparse.Namespace) -> str:
	if args.prompt is not None:
		return args.prompt.strip()
	return args.prompt_file.read_text(encoding="utf-8").strip()


def guess_mime_type(path: Path, explicit_mime_type: str | None) -> str:
	if explicit_mime_type:
		return explicit_mime_type
	mime_type, _ = mimetypes.guess_type(path)
	if not mime_type or not mime_type.startswith("image/"):
		raise ValueError(f"Could not infer an image MIME type for {path}. Pass PATH:MIME_TYPE.")
	return mime_type


def parse_reference_image(value: str) -> VideoGenerationReferenceImage:
	path_value, separator, mime_value = value.rpartition(":")
	if separator and mime_value.startswith("image/"):
		image_path = Path(path_value)
		explicit_mime_type = mime_value
	else:
		image_path = Path(value)
		explicit_mime_type = None
	mime_type = guess_mime_type(image_path, explicit_mime_type)
	return VideoGenerationReferenceImage(
		image=Image(
			image_bytes=image_path.read_bytes(),
			mime_type=mime_type,
		),
		reference_type=VideoGenerationReferenceType.ASSET,
	)


def build_config(args: argparse.Namespace) -> GenerateVideosConfig:
	reference_images = [parse_reference_image(value) for value in args.reference_image]
	return GenerateVideosConfig(
		aspect_ratio=args.aspect_ratio,
		reference_images=reference_images or None,
	)


def main() -> int:
	args = parse_args()
	if args.env_file.exists():
		load_dotenv(args.env_file)

	prompt = read_prompt(args)
	if not prompt:
		raise ValueError("Prompt is empty.")
	if args.poll_seconds < 1:
		raise ValueError("--poll-seconds must be at least 1.")

	client = genai.Client()
	operation = client.models.generate_videos(
		model=args.model,
		source=GenerateVideosSource(prompt=prompt),
		config=build_config(args),
	)

	while not operation.done:
		time.sleep(args.poll_seconds)
		operation = client.operations.get(operation)
		print(operation, flush=True)

	if not operation.response or not operation.response.generated_videos:
		print("Video generation finished without a generated video.", file=sys.stderr)
		return 1

	video = operation.response.generated_videos[0].video
	args.output.parent.mkdir(parents=True, exist_ok=True)
	args.output.write_bytes(video.video_bytes)
	print(f"Saved video to {args.output}")
	return 0


if __name__ == "__main__":
	try:
		raise SystemExit(main())
	except Exception as exc:
		print(f"Error: {exc}", file=sys.stderr)
		raise SystemExit(1)

# https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-an-image?hl=zh-cn

import time
from pathlib import Path

from google import genai
from google.genai.types import (
    GenerateVideosConfig,
    GenerateVideosSource,
    Image,
    VideoGenerationReferenceImage,
    VideoGenerationReferenceType,
)
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[1]

load_dotenv(ROOT_DIR / ".env")

client = genai.Client()

model_image = (ROOT_DIR / "inputs" / "yujie.jpg").read_bytes()
merchandise_image = (ROOT_DIR / "inputs" / "iphone17.png").read_bytes()

operation = client.models.generate_videos(
    model="veo-3.1-generate-001",
    source=GenerateVideosSource(
        prompt="Generate a advertisement video for the new iPhone 17. The first image is the model image. She uses the phone and talks about the features in Chinese. She says 'iphone 17,太带派了！'. The second image is the reference image of the merchandise from multiple views.",
    ),
    config=GenerateVideosConfig(
        aspect_ratio="16:9",
        reference_images=[
            VideoGenerationReferenceImage(
                image=Image(
                    image_bytes=model_image,
                    mime_type="image/jpeg",
                ),
                reference_type=VideoGenerationReferenceType.ASSET,
            ),
            VideoGenerationReferenceImage(
                image=Image(
                    image_bytes=merchandise_image,
                    mime_type="image/png",
                ),
                reference_type=VideoGenerationReferenceType.ASSET,
            ),
        ]
    ),
)

while not operation.done:
    time.sleep(15)
    operation = client.operations.get(operation)
    print(operation)

if operation.response:
    video = operation.response.generated_videos[0].video
    with open("outputs/output.mp4", "wb") as f:
        f.write(video.video_bytes)

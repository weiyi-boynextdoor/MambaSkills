# Provider Input Limits

Research date: 2026-05-22.

Provider behavior changes quickly. Check the target product surface and model version before making a hard promise about supported references, duration, resolution, or audio.

## Quick Comparison

| Provider | Officially confirmed input notes | Reference-image notes | Duration or output notes | Research caution |
| --- | --- | --- | --- | --- |
| Seedance | Seedance 1.0 model pages describe text-to-video and image-to-video variants. Seedance 2.0 public API reference exists. | Seedance 1.0 Lite image-to-video supports a first frame plus optional last frame, or `1-4` reference images in the model page reviewed. Seedance 1.0 Pro Fast model notes first-frame image input. | Check the model page or endpoint for the active version. | Do not generalize one Seedance version to every Seedance endpoint. |
| Kling | Kling 3.0 supports text or reference-image input in the product guide reviewed. Kling O1 describes reference and element workflows. | Kling 3.0 image-to-video accepts `1` reference image in the guide reviewed. Kling O1 video references accept `1-7` reference images, and O1 elements can use `1-4` images per element. | Kling 3.0 text-to-video guide lists `3s-15s` duration and `1080p` or `720p` resolution in the guide reviewed. | Kling limits are model-specific and differ across 3.0, O1, and older modes. |
| Veo | Vertex AI supports text prompts, image-to-video, interpolation with first and last frames, and reference-image workflows depending model and feature path. | Veo subject reference workflow supports up to `3` subject images. Style reference allows only `1` style image. | Vertex AI docs list the available Veo model and generation path details per endpoint. | Veo reference-image guidance is feature-specific; subject, style, first frame, and last frame are not interchangeable. |
| Sora | OpenAI video API supports text prompts and optional image reference input. | The API guide documents one `input_reference` image parameter. Sora app documentation describes uploading media in product workflows, but the reviewed docs do not state a universal app-wide reference-image maximum. | API guide currently documents `sora-2` and `sora-2-pro` with fixed duration and size options defined by the API. | Distinguish Sora app workflows from the OpenAI video API. |
| xAI Grok Imagine | xAI video generation supports text-to-video and image-to-video. Reference-to-video supports text plus reference images. | xAI reference-to-video docs say the API accepts `1-7` reference images. | xAI guides describe up to `10` seconds and configurable aspect ratio, resolution, and duration options by request type. | Use xAI docs for the API surface; Grok consumer product behavior may differ. |

## Provider Notes

### Seedance

- Treat Seedance as a versioned family.
- The Seedance 1.0 Lite model page reviewed distinguishes first-frame and last-frame use from multiple reference-image use.
- The Seedance 1.0 Pro Fast model page reviewed is narrower and calls out first-frame image input.
- The Seedance 2.0 API reference was located during research, but the public page reviewed did not expose a clear single maximum for all multimodal reference inputs. Confirm the exact endpoint before promising a count.

### Kling

- For Kling 3.0, official product guidance gives a simple text-to-video and image-to-video path.
- For Kling O1, official guidance adds stronger reference workflows:
	- `Video Reference`: `1-7` reference images.
	- `Elements`: `1-4` images per element.
- Do not describe O1 multi-reference behavior as if it applied to every Kling model.

### Veo

- Separate these concepts in prompts and UI assumptions:
	- first-frame image
	- last-frame image
	- subject reference images
	- style reference image
- Subject reference images are for preserving subject appearance.
- Style reference image is for style guidance and has a different limit.

### Sora

- The OpenAI API guide uses a single optional reference image parameter for image-guided generation.
- Sora product surfaces can expose storyboard or media-upload workflows that are not identical to the API contract.
- Do not promise reference-video or multi-image behavior unless the active Sora surface explicitly supports it.

### xAI Grok Imagine

- Distinguish:
	- text-to-video
	- image-to-video
	- reference-to-video
- Reference-to-video is the official multi-image path found in the xAI docs reviewed.
- Use concise reference instructions that name which subject details should remain stable.

## Research Rules For The Skill

- Ask which provider and model surface the user targets before optimizing prompt syntax for references.
- If the user does not know the provider yet, produce a provider-neutral director prompt first.
- Record version-sensitive claims with the model name when possible.
- If an official source does not publish a limit, say `not confirmed in the official docs reviewed` instead of filling the gap from third-party posts.

## Official Sources Checked

- [Seedance 1.0 Lite model page](https://docs.byteplus.com/en/docs/ModelArk/1520757)
- [Seedance 1.0 Pro Fast model page](https://docs.byteplus.com/en/docs/ModelArk/1520758)
- [Seedance 2.0 API reference](https://docs.byteplus.com/en/docs/ModelArk/2168526)
- [Kling 3.0 user guide](https://app.klingai.com/global/quickstart/kling-3.0)
- [Kling O1 user guide](https://app.klingai.com/global/quickstart/kling-o1)
- [Veo reference-image guide](https://cloud.google.com/vertex-ai/generative-ai/docs/video/use-reference-images-to-guide-video-generation)
- [OpenAI video generation guide](https://platform.openai.com/docs/guides/video-generation)
- [xAI video generation guide](https://docs.x.ai/docs/guides/video-generation)
- [xAI reference-to-video guide](https://docs.x.ai/developers/model-capabilities/video/reference-to-video)

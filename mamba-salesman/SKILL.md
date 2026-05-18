---
name: mamba-salesman
description: Create ecommerce advertising poster prompts, AI-generated poster images, advertising video director specs, and Veo ad videos for product ads, marketplace posters, social-commerce creatives, campaign visuals, and conversion-focused ecommerce ad concepts.
---

# MambaSalesman

Create ecommerce ad poster prompts, AI poster images, advertising video director specs, and Veo advertising videos.

## Active Features

- Generate advertising poster prompts.
- Generate AI poster images from approved poster prompts.
- Generate advertising video director specs for first-frame prompts, scripts, optional dialogue, and background music style.
- Generate Veo advertising videos from video-director prompts and reference images.

## Planned Features

- Multi-scene storyboards.

For unfinished notes, read `references/development.md`.

## Inputs

Collect only what is needed:

- Product name and category.
- Core selling points.
- Target customer.
- Platform, aspect ratio, or exact image size.
- Video length, if relevant.
- Brand tone.
- Required text, logo, or offer.
- Product reference image or brand asset, if provided.
- Additional reference images, such as model, scene, prop, styling, or mood references.
- Output directory and filename pattern, if the user wants generated assets saved to disk.

If inputs are missing, make reasonable ecommerce assumptions and state them briefly.
For advertising video director requests, default to 16:9 and 8 seconds unless the user specifies otherwise.

## Poster Prompt Workflow

Use this workflow when the user asks for ad concepts, poster prompts, image prompts, or prompt variants.

1. Identify the product, buyer, offer, and conversion goal.
2. Choose a creative angle: premium, practical, social-commerce, seasonal, bundle, comparison, or lifestyle.
3. Produce concise image-generation prompts in English.
4. Include layout guidance, lighting, composition, product treatment, background, typography area, and platform fit.
5. Avoid claims that are medical, financial, unverifiable, or stronger than the user supplied.

For detailed prompt patterns, read `references/poster-prompt.md`.

## Poster Image Workflow

Use this workflow when the user asks to generate the poster image itself.

1. Build or refine the final English image prompt.
2. Preserve user-provided product, brand, copy, color, and platform constraints.
3. If the user provides a reference image or brand asset, keep product appearance, packaging, logo placement, and brand cues consistent unless the user asks for a redesign.
4. Preserve requested aspect ratio or exact output size when the available image generation capability supports it.
5. Request a clean ecommerce composition with clear product focus and usable text space.
6. Generate the image with the available image generation capability.
7. If the user specifies an output directory, save the generated image there using the requested filename pattern; avoid overwriting existing files.
8. Do not add extra commentary after image generation unless the user asks for analysis or revisions.

For image-specific guidance, read `references/poster-image.md`.

## Advertising Video Director Workflow

Use this workflow when the user asks for advertising video concepts, video first-frame prompts, scripts, dialogue, background music direction, or video generation preparation.

1. Analyze the product reference image first: product identity, shape, material, color, packaging, logo placement, texture, scale cues, and important details that must remain consistent.
2. Analyze additional reference images when provided: model appearance and pose, scene, environment, props, lighting, styling, mood, camera language, and brand cues.
3. Identify the target customer, selling point, conversion goal, platform, aspect ratio, duration, and brand tone.
4. If the user does not specify platform details, set aspect ratio to 16:9 and duration to 8 seconds.
5. Create an English first-frame image prompt that can become the opening frame or visual anchor for video generation.
6. Write a concise advertising script with time-coded beats that fit the selected duration.
7. Include dialogue or voiceover only when useful for the campaign, product category, or user request.
8. Specify background music style, tempo, mood, instrumentation, and any sound design cues.
9. Keep claims conservative and do not invent discounts, certifications, awards, performance numbers, or regulated-category results.

For detailed video director patterns, read `references/video-director.md`.

## Veo Video Generation Workflow

Use this workflow when the user asks to generate the advertising video itself.

1. Follow the Advertising Video Director Workflow first, then convert the spec into one production-ready English Veo prompt.
2. Use the first-frame prompt, script beats, dialogue or voiceover, background music style, format, and negative direction as the generation prompt.
3. Keep the product reference image as the first reference image whenever one is provided; add model, scene, styling, mood, or brand images after it.
4. Default to model `veo-3.1-generate-001`, aspect ratio `16:9`, and 8 seconds unless the user specifies otherwise.
5. Run `scripts/generate_veo_video.py` with `--prompt-file` or `--prompt`, any `--reference-image` values, `--aspect-ratio`, and `--output`.
6. Load credentials from the skill-local `.env` by default. The script expects Google GenAI or Vertex AI environment variables such as `GOOGLE_GENAI_USE_VERTEXAI`, `GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_LOCATION`, or API-key based auth supported by the installed SDK.
7. If generation fails, report the failure directly; do not create a substitute video or copy unrelated media.

Example:

```bash
python mamba-salesman/scripts/generate_veo_video.py \
	--prompt-file outputs/video-prompt.txt \
	--reference-image inputs/product.png \
	--reference-image inputs/model.jpg \
	--aspect-ratio 16:9 \
	--output outputs/ad-video.mp4
```

## Output Rules

- Markdown and comments must be English.
- Keep outputs direct and commercially useful.
- Default to three strong variants unless the user asks for a different count.
- Use tabs for indentation in files created for this skill.
- For video director-only requests, output production-ready creative specs but do not claim that the final video has been generated.
- For Veo generation requests, state the output video path only after the script successfully writes the mp4.

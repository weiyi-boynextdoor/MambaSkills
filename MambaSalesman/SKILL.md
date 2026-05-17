---
name: MambaSalesman
description: Create ecommerce advertising poster prompts and AI-generated poster images for product ads, marketplace posters, social-commerce creatives, campaign visuals, and conversion-focused ecommerce ad concepts.
---

# MambaSalesman

Create ecommerce ad poster prompts and AI poster images.

## Active Features

- Generate advertising poster prompts.
- Generate AI poster images from approved poster prompts.

## Planned Features

- Advertising video scripts.
- AI-generated advertising videos.
- Multi-scene storyboards.

For unfinished notes, read `references/development.md`.

## Inputs

Collect only what is needed:

- Product name and category.
- Core selling points.
- Target customer.
- Platform or aspect ratio.
- Brand tone.
- Required text, logo, or offer.
- Reference image or brand asset, if provided.

If inputs are missing, make reasonable ecommerce assumptions and state them briefly.

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
4. Request a clean ecommerce composition with clear product focus and usable text space.
5. Generate the image with the available image generation capability.
6. Do not add extra commentary after image generation unless the user asks for analysis or revisions.

For image-specific guidance, read `references/poster-image.md`.

## Output Rules

- Markdown and comments must be English.
- Keep outputs direct and commercially useful.
- Default to three strong variants unless the user asks for a different count.
- Use tabs for indentation in files created for this skill.
- Mark video-related requests as planned unless the user explicitly asks for a draft-only concept.

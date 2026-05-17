# Advertising Video Director Reference

Use this reference to create ecommerce advertising video director specs.

## Scope

The advertising director capability prepares the creative inputs needed for AI advertising video generation. It analyzes product reference images and optional supporting reference images, then produces:

- A video first-frame image prompt.
- A concise advertising script.
- Dialogue or voiceover, when useful.
- Background music and sound direction.
- Aspect ratio and duration.

Unless the user specifies otherwise, default to:

- Aspect ratio: 16:9.
- Duration: 8 seconds.

## Reference Image Analysis

Start with the product reference image. Preserve:

- Product category and exact visible form.
- Shape, silhouette, color, material, finish, and texture.
- Packaging, label, logo placement, typography style, and recognizable brand cues.
- Scale, hero angle, and details that affect product recognition.

Then analyze any additional reference images:

- Model: age range, styling, pose, expression, wardrobe, hand position, and interaction with the product.
- Scene: location type, surfaces, props, weather, season, time of day, and background depth.
- Mood: lighting, color palette, camera style, energy, luxury level, realism, and pacing.
- Brand assets: logo use, color system, typography mood, required text-safe areas, and visual restrictions.

When references conflict, prioritize product accuracy first, then brand requirements, then scene mood.

## Output Template

```text
Video Director Spec

Product Reading:
[Brief description of the product reference image and non-negotiable visual details.]

Reference Integration:
[How model, scene, styling, or mood references should influence the video.]

Campaign Angle:
[Audience, selling point, emotional hook, and conversion goal.]

Format:
Aspect ratio: [ratio]
Duration: [seconds]
Platform fit: [platform or general use]

First-Frame Image Prompt:
[English image-generation prompt for the opening frame. Include product accuracy, scene, subject, composition, camera angle, lighting, text-safe area, style, and aspect ratio.]

Script:
0:00-0:02 - [Opening hook visual/action.]
0:02-0:05 - [Product benefit or interaction.]
0:05-0:08 - [Brand/product hero and CTA moment.]

Dialogue or Voiceover:
[Short lines only if useful. Use "None" when a silent visual ad is stronger.]

Background Music Style:
[Genre, tempo, mood, instrumentation, and sound design cues.]

Negative Direction:
[What to avoid during image or video generation.]
```

## First-Frame Prompt Template

```text
Commercial advertising video opening frame for [product], based on the provided product reference image, preserving [key product details].
Scene: [environment/reference integration], [model or hand interaction if relevant].
Composition: [camera angle], product as the clear hero, [foreground/background], clean text-safe space for [headline/logo/offer].
Lighting and style: [brand tone], [lighting], [color palette], premium realistic commercial cinematography.
Video format: opening frame for an [duration]-second ad, [aspect ratio], designed for smooth motion into [next action].
Avoid: distorted product, changed packaging, warped logo, clutter, unreadable text, unsupported claims, unrealistic motion.
```

## Script Patterns

Use simple time-coded beats. For the default 8-second format, prefer three beats:

- 0:00-0:02: Hook with product, model, or scene movement.
- 0:02-0:05: Demonstrate the main benefit visually.
- 0:05-0:08: Hero product reveal, brand moment, and call to action.

For a no-dialogue ad, make the motion and music carry the story.
For a dialogue or voiceover ad, keep lines short enough to fit the duration.
For premium products, use fewer words and slower pacing.
For social-commerce products, use a stronger hook, quicker cuts, and clearer benefit language.

## Dialogue and Voiceover Rules

- Include dialogue only when it improves persuasion or clarity.
- Keep dialogue natural and short.
- Do not force a spokesperson if the product is better served by silent cinematic presentation.
- Avoid invented guarantees, medical claims, financial outcomes, or measurable performance claims unless supplied by the user.
- Use the language requested by the user; otherwise match the user-facing campaign market when known.

## Background Music Guidance

Describe music in generation-friendly terms:

- Genre or reference mood: sleek electronic pop, warm acoustic, cinematic luxury, upbeat retail, clean tech, playful lifestyle.
- Tempo: slow, medium, upbeat, high-energy.
- Instrumentation: soft synth bass, light percussion, piano accents, strings, guitar, airy pads, subtle risers.
- Sound design: product whoosh, soft click, fabric movement, sparkle accent, room ambience, transition hit.

Avoid naming copyrighted songs or asking for direct imitation of a living artist.

## Negative Direction

Use when helpful:

```text
distorted product shape, changed logo, inaccurate packaging, extra fake labels, cluttered scene, overexposed highlights, unreadable text, awkward hands, unnatural face, exaggerated claims, medical claims, before-and-after result, low-resolution video, jittery camera
```

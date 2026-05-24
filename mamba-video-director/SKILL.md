---
name: mamba-video-director
description: Direct AI short-video prompt creation through conversation, turning rough video ideas into production-ready video generation prompts.
---

# MambaVideoDirector

Create AI short-video director prompts through conversation.

## Current Scope

- Develop video concepts with the user through dialogue.
- Turn approved creative direction into video-generation prompts.

## Session State

When a video plan includes confirmed technical settings, clip segmentation, or per-clip prompts, persist the working state in the user's current running directory:

`.mamba-video-director.json`

Use this file to recover state if conversation memory is incomplete. Treat the file as local runtime metadata, not skill source.

### Serialization Protocol

Use UTF-8 encoded JSON with two-space indentation. Keep the file human-readable and stable between updates. Preserve unknown top-level fields when updating an existing state file.

Use this shape:

```json
{
  "updated_at": "2026-05-24T09:30:00+08:00",
  "project": {
    "title": "",
    "brief": "",
    "target_platform": ""
  },
  "video_config": {
    "duration_seconds": null,
    "aspect_ratio": "",
    "provider": "",
    "api_or_model": "",
    "resolution": "",
    "audio": ""
  },
  "clips": [
    {
      "index": 1,
      "duration_seconds": null,
      "role": "",
      "start_time_seconds": null,
      "end_time_seconds": null,
      "prompt": "",
      "negative_prompt": "",
      "continuity_requirements": []
    }
  ],
  "open_questions": [],
  "final_prompt_pack": {
    "status": "draft",
    "prompt": "",
    "provider_notes": "",
    "export_notes": ""
  },
  "revision_notes": []
}
```

Field meanings:

- `updated_at`: Last time the state file was written, using ISO 8601 with timezone.
- `project`: Human-facing project identity and creative brief.
- `project.title`: Short project name or working title.
- `project.brief`: One-paragraph summary of the video goal, subject, audience, and creative direction.
- `project.target_platform`: Intended publishing surface, such as TikTok, YouTube Shorts, Instagram Reels, Douyin, or a custom delivery channel.
- `video_config`: Technical generation settings that affect prompt structure and output planning.
- `video_config.duration_seconds`: Total intended video duration in seconds.
- `video_config.aspect_ratio`: Output aspect ratio, such as `9:16`, `16:9`, `1:1`, or `4:5`.
- `video_config.provider`: Video generation provider or product family, such as Sora, Veo, Kling, Seedance, Runway, or provider-neutral.
- `video_config.api_or_model`: Specific API, model, or generation surface when known, such as `veo-3`, `kling-3.0`, or a local wrapper name.
- `video_config.resolution`: Exact output resolution only when required, such as `1080x1920`; otherwise leave empty.
- `video_config.audio`: Audio plan or support assumption, such as no audio, natural sound, music bed, voiceover, or provider-specific audio notes.
- `clips`: Ordered list of clip-level prompt units. This is the single source of truth for clip count, clip order, clip durations, and how the video is cut.
- `clips[].index`: 1-based clip number matching the clip order.
- `clips[].duration_seconds`: Duration of this clip in seconds.
- `clips[].role`: Narrative or production role of the clip, such as opening reveal, product detail, action beat, transition, payoff, or closing frame.
- `clips[].start_time_seconds`: Start time of this clip within the final edited video.
- `clips[].end_time_seconds`: End time of this clip within the final edited video.
- `clips[].prompt`: Positive generation prompt for this clip.
- `clips[].negative_prompt`: Clip-specific negative prompt or failure modes to avoid.
- `clips[].continuity_requirements`: Clip-specific items that must carry over from previous or later clips.
- `open_questions`: Unresolved questions that must be confirmed before finalizing prompts or generation settings.
- `final_prompt_pack`: Final deliverable state for the user or video API.
- `final_prompt_pack.status`: `draft` while still changing, `needs_confirmation` when blocked by missing user/provider details, or `ready` when usable.
- `final_prompt_pack.prompt`: Final combined prompt, or the main provider-ready prompt when the provider expects a single prompt.
- `final_prompt_pack.provider_notes`: Provider-specific assumptions, limits, warnings, or formatting instructions.
- `final_prompt_pack.export_notes`: Practical generation or editing notes, such as clip order, filename suggestions, seed/reference usage, or handoff instructions.
- `revision_notes`: Chronological short notes describing meaningful changes to the plan.

Write rules:

- Use `null` for unknown numeric values.
- Use an empty string for unknown text values.
- Use an empty array for unknown lists.
- `final_prompt_pack.status` should be `draft`, `ready`, or `needs_confirmation`.
- Keep clip order stable by `clips[].index`.
- Derive clip count, clip order, total planned clip duration, and single-clip versus multi-clip status from `clips`.
- Do not keep a separate segmentation summary that duplicates `clips`.
- When a user changes a confirmed decision, update the relevant field and append a short entry to `revision_notes`.
- Do not delete existing meaningful fields just because they were not mentioned in the latest user message.

Before producing or revising a final prompt pack, read the state file if it exists, merge in the latest user decisions, and write the updated state back to the same path.

## Conversation Start

When the user starts from a rough idea, help them develop it instead of requiring a final prompt up front.

Confirm these creative constraints early when they are missing and materially affect the next step:

- Video type or intended format.
- Target duration.
- Aspect ratio or target platform.
- Target AI video provider or model surface, when duration, references, continuity, or output behavior depends on provider limits.

If the user has not specified a target duration, ask for the duration before producing a final prompt or multi-clip plan.

If the user needs more than one generated clip, seamless continuity, storyboard segmentation, or any output that may exceed a single model generation length, ask which AI video provider or model surface they plan to use before planning clip lengths. If they do not know yet, create a provider-neutral plan with conservative clip durations and clearly mark provider-specific assumptions for later confirmation.

Ask only for the missing constraints that matter now. If the user is still exploring an idea, make a brief working assumption and continue, then confirm the constraints before producing the final prompt.

Ask for exact resolution only when the target platform, delivery requirement, or generation tool needs it.

## Reference Files

- Read `references/video-effects-prompts.md` when the user needs camera moves, visual effects, transition language, or prompt vocabulary for video direction.
- Read `references/multi-clip-continuity.md` when the user needs a video longer than one model generation, seamless multi-clip transitions, storyboard-to-clip breakdowns, or per-clip prompt packs.
- Read `references/provider-input-limits.md` before promising model-specific reference-image, video-input, duration, or output-format behavior.
- Read `references/provider-safety-review.md` before drafting prompts that may face moderation, likeness, rights, violence, sexual-content, or policy-review risk.

For unfinished design notes, read `references/development.md`.

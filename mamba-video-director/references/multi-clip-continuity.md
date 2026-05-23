# Multi-Clip Continuity Planning

Use this reference when a requested video may need multiple generated clips because of model duration limits, story structure, platform format, or continuity requirements.

## Goal

Turn a longer video idea into a production-ready clip plan with one prompt per generated segment, plus transition and editing instructions that help the final video feel continuous.

Do not treat multi-clip work as simple equal-duration splitting. Segment by narrative beats, camera logic, action completion, provider duration limits, and available reference-input features.

## Required Checks

Before producing a final multi-clip plan, confirm:

- Target duration.
- Target AI video provider or model surface.
- Aspect ratio or delivery platform.

If target duration is missing, ask for it.

If provider or model surface is missing, ask for it when it affects clip length, reference-image workflow, first-frame or last-frame support, video continuation, storyboard behavior, or output format.

If the user does not know the provider yet, create a provider-neutral plan using conservative `6-8s` generated clips and mark provider-specific details as assumptions to verify later.

Read `provider-input-limits.md` before stating exact provider limits.

## Provider Capability Tiers

Use the provider's active model surface to choose the continuity strategy.

| Capability | Continuity strategy |
| --- | --- |
| Text-to-video only | Use hidden cuts, match cuts, repeated continuity constraints, and post-production stitching. Avoid promising frame-perfect continuity. |
| First-frame image-to-video | Export the previous clip's final usable frame and use it as the next clip's first-frame reference. |
| First-frame plus last-frame or interpolation | Define both entry and exit frames for each clip; use the previous clip's end frame as the next clip's start frame when supported. |
| Reference-image workflow | Keep subject, wardrobe, product, style, and setting stable with labeled references; still use explicit opening and ending frame descriptions. |
| Video continuation or storyboard workflow | Plan shots as connected storyboard cells, then specify continuity constraints, transition behavior, and handoff frames for each cell. |

## Planning Workflow

1. Build a continuity bible:
	- subject identity and stable visual details
	- wardrobe, props, product, or character constraints
	- location, time of day, lighting, weather, and color palette
	- lens feel, camera style, aspect ratio, and pacing
	- negative constraints for common drift risks
2. Break the story into clips:
	- choose clip durations below the provider maximum
	- preserve complete action beats inside each clip
	- place cuts where motion, occlusion, light, foreground objects, or framing can hide discontinuity
	- reserve `1-2s` of overlap when possible so the editor can trim to the best handoff
3. Define handoff frames:
	- opening frame for each clip
	- ending frame for each clip
	- what reference image or previous frame should be used, if supported
4. Write one prompt per clip:
	- include the continuity bible constraints in every prompt
	- name the clip number and its role in the sequence
	- describe the visible action and timing
	- use one dominant camera move per short clip unless the provider supports reliable multi-shot generation
	- specify the transition behavior at the end of the clip
5. Add edit instructions:
	- which frames to export as references
	- where to trim overlap
	- how to bridge clips with audio, motion blur, light, or match cuts
	- color, stabilization, and speed-ramp notes when needed

## Continuity Techniques

Use these when clip-to-clip consistency is more important than novelty:

- `Use Clip 01 final usable frame as Clip 02 first-frame reference.`
- `Hold the same subject scale, lens feel, lighting direction, and color temperature across both clips.`
- `End on a clean pose that the next clip can start from.`
- `Create a brief foreground occlusion before the cut.`
- `Use a match cut on the same hand gesture, body direction, object shape, or camera motion.`
- `Use a whip-pan, light wipe, shadow wipe, doorframe pass, smoke pass, or object crossing lens to hide the transition.`
- `Keep the first second of the next clip visually close to the previous clip's final frame.`

Avoid asking for exact continuous action across unrelated generations unless the provider supports a continuation or frame-conditioned workflow. Frame-perfect physical continuity is not reliable in text-only generation.

## Output Format

For multi-clip requests, prefer this structure:

```text
Continuity bible
- [stable subject, world, style, camera, and negative constraints]

Clip plan
| Clip | Duration | Purpose | Generation input | Opening frame | Ending frame | Transition |

Per-clip prompts
Clip 01 prompt:
[prompt]

Clip 02 prompt:
[prompt]

Editing notes
- [reference-frame export instructions]
- [overlap trimming notes]
- [audio/color/stabilization notes]
```

## Per-Clip Prompt Template

```text
Clip [number] of [total], [duration], [aspect ratio].
Role in sequence: [narrative purpose].
Continuity: keep [subject], [wardrobe/product], [location], [lighting], [style], [lens/camera feel] consistent with the continuity bible.
Generation input: [text-only / first-frame from Clip X / first and last frame / reference images / storyboard cell].
Opening frame: [precise starting composition and action state].
Action: [visible action with timing and one dominant camera movement].
Ending frame: [precise ending composition designed for the next clip].
Transition: [hidden cut, match cut, whip pan, light wipe, foreground occlusion, or direct continuation].
Avoid: [critical drift or artifact risks].
```

## Practical Defaults

- Use `6-8s` clip targets when provider limits are unknown.
- Use fewer, stronger beats rather than many tiny fragments.
- For a `30s` video, start with `4` clips of about `7-8s` or `5` clips of about `6s`, then adjust by narrative rhythm.
- For social ads, keep the first clip visually decisive and the final clip clean enough for product, CTA, or logo treatment when allowed.
- For cinematic scenes, prioritize continuity of motion direction, light direction, and subject scale.

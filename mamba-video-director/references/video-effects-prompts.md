# Video Effects Prompt Notes

Research date: 2026-05-22.

Use this file as a prompt vocabulary reference, not as a guarantee that every model will obey every effect phrase.

## Prompting Pattern

Official Veo prompt guidance recommends describing the subject, scene, action, camera movement, visual style, and optional audio or negative constraints. Kling and Seedance product guidance also emphasizes structured scene direction, camera language, and model-specific multi-shot or reference guidance.

Prefer this order when converting a director idea into a video prompt:

1. State the subject and what must stay consistent.
2. State the visible action and its timing.
3. State the scene, lighting, atmosphere, and material cues.
4. State shot size, camera angle, lens feel, and camera movement.
5. State style, pacing, audio, and transition behavior when relevant.
6. Add negative direction only for failures that matter.

## Camera Movement Vocabulary

| Intent | Prompt phrases |
| --- | --- |
| Reveal scale | `slow dolly out`, `crane up reveal`, `pull back from macro detail into a wide establishing shot` |
| Increase intimacy | `slow push-in`, `gentle dolly-in toward the eyes`, `camera glides closer as the subject pauses` |
| Follow motion | `tracking shot`, `side-follow shot`, `low-angle chase camera`, `camera follows behind at walking pace` |
| Orbit subject | `clockwise orbit`, `half-circle arc around the subject`, `camera circles the product while highlights travel across the surface` |
| Add handheld energy | `controlled handheld movement`, `subtle handheld sway`, `documentary follow camera with restrained shake` |
| Add precision | `locked-off tripod shot`, `symmetrical static frame`, `mechanical slider move` |
| Change attention | `rack focus from foreground detail to the subject`, `focus pull from logo to face`, `shallow depth of field reveal` |
| Emphasize verticality | `tilt up from feet to skyline`, `vertical rise past the subject`, `top-down descent into the scene` |

## Shot And Lens Vocabulary

| Need | Prompt phrases |
| --- | --- |
| Establish world | `wide establishing shot`, `aerial city overview`, `full-body environmental portrait` |
| Show emotion | `medium close-up`, `intimate close-up`, `eye-level portrait framing` |
| Show detail | `macro detail shot`, `extreme close-up of texture`, `product surface highlight detail` |
| Make subject powerful | `low-angle hero shot`, `center-framed hero composition`, `foreground-to-background depth` |
| Make space feel compressed | `telephoto compression`, `long-lens portrait feel`, `soft layered background` |
| Make space feel immersive | `wide-angle perspective`, `near-lens foreground motion`, `deep spatial parallax` |

## Motion And Timing Vocabulary

| Effect | Prompt phrases |
| --- | --- |
| Graceful motion | `slow deliberate movement`, `floating fabric motion`, `gentle breeze-driven movement` |
| Fast impact | `rapid acceleration`, `sharp impact beat`, `fast pass-by with motion blur` |
| Slow motion | `cinematic slow motion`, `high-speed capture feel`, `droplets suspended in slow motion` |
| Time compression | `timelapse light shift`, `clouds race across the sky`, `day-to-night progression` |
| Loopable motion | `seamless cyclical motion`, `return to the opening pose`, `continuous repeating gesture` |
| Beat-based motion | `three clear beats: reveal, interaction, payoff`, `action changes on the music accent` |

## Visual Effects Vocabulary

### Atmosphere

- `volumetric light rays through haze`
- `fine dust particles visible in backlight`
- `rain streaks catching neon reflections`
- `mist curling around the subject`
- `heat shimmer over sunlit pavement`
- `soft breath vapor in cold air`

### Particles And Materials

- `spark fragments scatter on impact`
- `glittering glass-like particles assemble around the object`
- `ink disperses through water`
- `liquid splash crown forms and settles`
- `metallic reflections glide across the surface`
- `fabric fibers and stitching visible in macro light`

### Transformations

- `object assembles from layered components`
- `scene morphs from sketch lines into photoreal detail`
- `seasonal environment transitions around the same subject`
- `light wipes across the frame and reveals the next state`
- `particles collapse into the final logo-free hero composition`

### Screen And Tech Effects

- `subtle holographic interface glow around the device`
- `clean data-light pulses travel along the surface`
- `transparent UI reflections stay secondary to the subject`
- `controlled scan-light reveal`

Avoid vague effects such as `cool special effects` or `epic VFX`. Name what appears, how it moves, and whether it should stay subtle or dominant.

## Transition Vocabulary

| Transition | Prompt phrases |
| --- | --- |
| Match cut | `match cut on circular motion`, `cut on the same hand gesture`, `shape-matched transition` |
| Whip transition | `whip-pan transition into the next scene`, `fast lateral blur reveals a new location` |
| Light transition | `bright flare wipe`, `neon reflection washes into the next shot`, `shadow wipe across frame` |
| Object transition | `foreground object crosses lens and reveals the next scene`, `camera passes through glass into the interior` |
| Continuous shot illusion | `one continuous flowing shot`, `camera move hides the transition behind the subject` |

## Prompt Templates

### Single-shot cinematic prompt

```text
A [subject] [visible action] in [scene]. [Lighting and atmosphere]. [Shot size and angle]. The camera [camera movement] with [lens or focus behavior]. Motion is [pace and timing]. Visual style: [style cues]. Keep [consistency constraints]. Avoid [high-value negative constraints].
```

### Short multi-beat prompt

```text
Create a [duration] [aspect ratio] short video with three clear beats.
Beat 1: [opening image and camera behavior].
Beat 2: [action escalation and effect].
Beat 3: [payoff frame and ending motion].
Keep the subject consistent across all beats. Use [lighting], [style], and [audio direction if supported]. Avoid [critical failure modes].
```

## Practical Rules

- Keep each motion request physically compatible with the shot. Do not stack a crane move, orbit, whip pan, macro focus pull, and handheld shake into one short beat unless the model is explicitly expected to cut.
- Prefer one dominant camera move per short shot.
- Prefer visible, filmable descriptions over abstract mood words.
- Separate subject motion from camera motion when precision matters.
- State whether an effect is subtle, restrained, intense, foreground, background, or a transition.
- For reference-based generation, describe what must be preserved from the reference separately from what should change in motion.

## Official Sources Checked

- [Veo prompt guide](https://cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide)
- [Kling 3.0 user guide](https://app.klingai.com/global/quickstart/kling-3.0)
- [Seedance prompt guide](https://docs.byteplus.com/en/docs/ModelArk/VideoGenerationPromptGuide)

# Provider Safety Review Notes

Research date: 2026-05-22.

Use this file to make prompts more review-friendly, not to evade safety systems.

## Core Rule

The skill should help users describe lawful, rights-aware, non-exploitative video ideas clearly. It should not help users bypass provider moderation, disguise disallowed requests, or guess unsafe wording that might slip through.

## Prompt Habits That Usually Reduce Review Risk

- Use fictional, original, or user-owned characters unless the provider and user rights clearly allow a real person or protected character.
- State consent and context when a scene could be misread, such as staged action, fictional drama, or documentary reconstruction.
- Prefer non-graphic depictions when violence is not the creative point.
- Avoid sexual content involving minors or youthful ambiguity entirely.
- Avoid celebrity likeness, living public-figure manipulation, impersonation, misleading evidence, and realistic fake news framing unless the provider explicitly supports the exact use case and rights are clear.
- Avoid requests for hateful, extremist, criminal-instructional, exploitative, or self-harm-glorifying content.
- Use neutral production wording for sensitive but allowed work: `fictional`, `staged`, `non-graphic`, `no real person likeness`, `rights-cleared`, `age-appropriate`, `no deceptive news framing`.
- Ask for safer alternatives when the user's creative goal can survive a lower-risk treatment.

## Review-Friendly Prompt Rewrite Pattern

### Risky direction

```text
Make a realistic leaked video of a famous politician admitting a crime.
```

### Safer direction

```text
Create a fictional political-thriller scene with an original actor in a clearly staged cinematic setting, no real person likeness, no news overlay, no claim that the footage is real.
```

## Provider Signals Found In Official Sources

### OpenAI Sora

- OpenAI policy materials for Sora emphasize limits around real people, public figures, copyrighted characters and music, graphic sexual content, graphic violence, extremist propaganda, self-harm promotion, and exploitative content involving minors.
- The OpenAI video API guide also states that input images containing human faces are currently rejected.
- Practical implication: for Sora-facing prompts, prefer original characters and avoid relying on face-reference input unless the active product surface explicitly allows it.

### Google Veo

- Veo responsible-use guidance says prompts can be blocked when safety filters trigger, including prohibited-content and child-safety filters.
- Google guidance also states that generated videos are checked with safety filters and that citation checks can block requests likely to reproduce training data or recognizable copyrighted material.
- Practical implication: write original scenes, avoid underage-sensitive material, and do not ask for close reproduction of protected media.

### xAI Grok Imagine

- xAI acceptable-use policy prohibits areas such as child sexual abuse material, sexual content involving minors, non-consensual intimate imagery, harmful impersonation, certain harassment and exploitation, and content that violates law or third-party rights.
- Practical implication: keep likeness and rights assumptions explicit, especially in reference-driven video requests.

### Seedance

- Seedance model pages and API references are clear about model capability paths, but the official materials reviewed for this note did not provide a single public prompt-approval checklist for every Seedance surface.
- Practical implication: keep prompts rights-aware and non-exploitative, then verify surface-specific policy and moderation errors when generating.

### Kling

- Kling official product guides clearly document prompting and reference workflows, but the official materials reviewed for this note did not provide a detailed public approval checklist comparable to the OpenAI or Google policy pages reviewed.
- Practical implication: use the general review-friendly habits above and confirm the active Kling product policy before promising approval on sensitive content.

## Sensitive-Content Triage

Before producing a provider-targeted prompt, check whether the request includes:

- A real person's face, voice, or identity.
- A public figure, celebrity, politician, or influencer.
- A copyrighted character, logo-heavy brand recreation, or music-video imitation.
- Sexual content, nudity, minors, or age ambiguity.
- Graphic injury, cruelty, self-harm, criminal instruction, or extremist material.
- A deceptive claim that generated footage is real evidence, journalism, CCTV, or a leak.

If yes, decide whether to:

1. Continue with explicit safer framing.
2. Ask for rights or context.
3. Offer a fictional or non-graphic alternative.
4. Decline if the creative goal itself remains disallowed.

## Output Guidance For The Skill

- Do not promise that any prompt will pass moderation.
- Say why a sensitive rewrite is safer in plain language.
- Preserve the creative goal when possible while removing the risky dependency.
- Keep provider-specific restrictions separate from general safety heuristics.

## Official Sources Checked

- [OpenAI Sora policy page](https://openai.com/policies/creating-images-and-videos-in-line-with-our-policies/)
- [OpenAI video generation guide](https://platform.openai.com/docs/guides/video-generation)
- [Veo responsible AI and usage guidelines](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/responsible-ai-and-usage-guidelines)
- [xAI acceptable use policy](https://x.ai/legal/acceptable-use-policy)
- [Seedance prompt guide](https://docs.byteplus.com/en/docs/ModelArk/VideoGenerationPromptGuide)
- [Kling 3.0 user guide](https://app.klingai.com/global/quickstart/kling-3.0)

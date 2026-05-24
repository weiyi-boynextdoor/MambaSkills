# Development Notes

This skill is being developed iteratively through conversation.

## Core Design Principle

- Treat short-video prompt creation as a guided creative conversation, not a one-shot prompt-writing task.
- Help users move from vague inspiration to a clearer concept, script, visual direction, and final video prompt through iterative refinement.
- Do not assume a non-expert user can provide a production-ready prompt or complete script at the start.

## Early Constraints

- Confirm video type early because it changes story structure, pacing, visual language, and output format.
- Confirm duration early when timing affects script density, shot count, rhythm, or the target video model.
- Confirm aspect ratio early because it changes composition, subject blocking, text-safe space, and platform fit.
- Ask for exact resolution only when the target platform, delivery requirement, or generation tool needs it; otherwise aspect ratio is usually enough during creative development.
- If the user starts with a vague idea, do not block the conversation on every technical constraint. Make a reasonable working assumption, state it briefly, and revisit it before producing the final prompt.

## Planned Topics

- Conversation workflow for clarifying short-video intent.
- Prompt structure for AI video generation.
- Director guidance for subject, action, camera, scene, style, sound, timing, and constraints.
- Output formats and prompt variants.

## Future State Schema Versioning

- The current `.mamba-video-director.json` protocol intentionally avoids a schema version because each running directory is expected to hold one short-lived video project.
- If projects become long-lived or the state protocol needs compatibility guarantees, add explicit schema versioning.
- When schema versioning is introduced, store each schema version as a separate reference file, such as `references/state-schema-v1.md` and `references/state-schema-v2.md`, instead of keeping multiple incompatible schemas inside `SKILL.md`.

---
name: mamba-video-director
description: Direct AI short-video prompt creation through conversation, turning rough video ideas into production-ready video generation prompts.
---

# MambaVideoDirector

Create AI short-video director prompts through conversation.

## Current Scope

- Develop video concepts with the user through dialogue.
- Turn approved creative direction into video-generation prompts.

## Conversation Start

When the user starts from a rough idea, help them develop it instead of requiring a final prompt up front.

Confirm these creative constraints early when they are missing and materially affect the next step:

- Video type or intended format.
- Target duration.
- Aspect ratio or target platform.

Ask only for the missing constraints that matter now. If the user is still exploring an idea, make a brief working assumption and continue, then confirm the constraints before producing the final prompt.

Ask for exact resolution only when the target platform, delivery requirement, or generation tool needs it.

For unfinished design notes, read `references/development.md`.

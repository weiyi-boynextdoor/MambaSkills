---
name: mamba-resume
description: Tailor an existing resume or CV to a target job description, role profile, recruiter brief, or hiring requirement. Use when Codex needs to read a raw resume file, make minimal role-specific edits while preserving the candidate's original wording and style, and write a Markdown resume into an outputs/ directory.
---

# MambaResume

Modify an existing resume for a target role with conservative edits and Markdown output.

## Scope

- Accept one raw resume file as the source of truth.
- Accept job requirements from a job description, role brief, pasted text, or user notes.
- Rewrite only what improves alignment with the target job.
- Preserve the original structure, tone, chronology, and factual claims.
- Output the tailored resume as Markdown under `outputs/`.

For incomplete ideas, read `references/development.md`.

## Inputs

Collect only what is needed:

- Source resume file path.
- Target job description, role requirements, or hiring brief.
- Output filename, if the user has a preference.
- Language preference, if different from the original resume.
- Any strict constraints, such as no fabrication, one-page limit, ATS focus, or industry-specific terminology.

If the job requirements are missing, ask for them before rewriting. If the output filename is missing, derive it from the source resume name and target role.

## Resume Reading

Read the source resume before editing. Preserve the candidate's stated facts:

- Names, dates, employers, schools, titles, credentials, locations, links, and contact details.
- Project outcomes, metrics, tools, domains, and responsibilities.
- Section order and heading style unless the target job clearly benefits from a small reordering.
- Original language and formality level.

If the source format is not Markdown, extract the text faithfully first. Do not invent details to fill gaps.

## Job Matching

Identify the role's strongest signals:

- Required skills, tools, frameworks, certifications, languages, and years of experience.
- Domain keywords and seniority expectations.
- Responsibilities that map directly to existing resume experience.
- Soft-skill or leadership requirements that are already evidenced in the resume.
- ATS keywords that can be added naturally without changing meaning.

Prefer matching existing evidence over adding new phrasing. If a required skill is absent from the resume, do not add it unless the user explicitly confirms it is true.

## Editing Rules

Make the smallest useful set of changes:

- Keep the original style, sentence length, bullet density, and first-person/third-person convention.
- Keep accomplishments recognizable; strengthen wording only when the source already supports it.
- Replace generic wording with role-relevant wording when meaning stays true.
- Reorder bullets within a section only when it brings the most relevant experience forward.
- Trim unrelated details only when they distract from the target role or exceed the user's length constraint.
- Preserve metrics exactly unless the user provides corrected numbers.
- Do not fabricate employers, titles, dates, education, certifications, tools, projects, awards, publications, or measurable impact.
- Do not over-optimize with keyword stuffing.

When a valuable target requirement cannot be supported by the resume, leave it out and mention the gap separately to the user after writing the file.

## Output Workflow

1. Read the raw resume file.
2. Parse or summarize the target job requirements.
3. Map requirements to existing resume evidence.
4. Produce a tailored Markdown resume with minimal edits.
5. Save it under `outputs/` using a clear `.md` filename.
6. Report the output path and briefly note the main edit categories.
7. Mention any important target requirements that were not added because the resume did not support them.

## Markdown Output

Write clean Markdown:

- Use headings and bullets that mirror the original resume as closely as possible.
- Keep contact details and links readable.
- Avoid tables unless the source resume already uses a table-like structure and Markdown remains readable.
- Use plain Markdown, not HTML, unless needed to preserve an existing element.
- Do not include analysis notes inside the resume file.

Default filename pattern:

`outputs/<source-name>-<target-role>-tailored.md`

Normalize the role segment to lowercase hyphen-case. Avoid overwriting an existing file unless the user requests it.

## User Summary

After saving, respond with:

- The Markdown output path.
- A concise summary of what changed.
- Any unsupported job requirements that were intentionally not added.
- Any assumptions made, if they affected the result.

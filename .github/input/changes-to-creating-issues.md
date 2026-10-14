# Changes to Creating Issues

It turns out that the way we're generating issues needs adjustments. We need to do the following:

- Create separate issue files for all issues including sub-issues.
- Issues will be identified by title, and an issue number to simulate an actual GitHub issue.
- Umbrella issues will link to sub-issues rather than containing issue content. 
- Creating umbrella issues will be a new prompt.

Here's an example of a TechDocs issue in CNCF:
https://github.com/kedacore/keda-docs/issues/1363

The format ( headings), should follow the `.github\issue_template\kubevirt-doc-issue.md` format as that is KubeVirt's team's issue format for documentation.

Here's an example of an umbrella issue:
https://github.com/kedacore/keda-docs/issues/1361

The format should follow the `.github\issue_template\umbrella-issue.md` format. We don't need "Use case:" or "Specification:" in the headings.

I think it's prudent to have a separate prompt for generating issues. So there will be two:
create-issues.prompt.md
create-umbrella-issues.prompt.md

## Implementation

Build upon the "Recommendations and Issues" section for creating issue files, using prompt files, issues-coverage.md and any other related files with the changes described here.

Update the paragraph on line 52 of `.github\prompts\create-issues-prompt.md` to describe just linking to the sub-issues as depicted in `.github\issue_template\umbrella-issue.md`.

### Issue numbers

Issue numbers will be 5 digits. Let's start with the first issue being 9001.

In the top metadata, the `title:` shall be in the format "{title} #{Issue number}"

In the Umbrella issue, sub-issues shall be linked like this:
- [Reorganize Concepts #9938](../output/issues/9999-reorganize-concepts.md)

Increment the issue number by one for each issue, and add a table in `issues-coverage.md` that maps the issue numbers, (Col A), with the titles, (Col B).

Save issue files in the format "{issue-number}{condensed-issue-title}", for example: `9999-reorganize-concepts.md`. Save to `.github/output/issues/` as before. (I archived the previous run in the `prev_1` subfolder).

### Create new umbrella issues prompt

Create a new "create-umbrella-issues" prompt that will be run after all issue files have been created. This new session ascertains umbrella issues. 

Create the `.github/prompts/issues/create-umbrella-issues.prompt.md` and update copilot-instructions accordingly.

Curious, would Claude prefer it all in the same prompt? If so, let me know.

After the updated prompt files are complete, I'll run them.

## Copilot's Notes

Done. Changes:

Updated

•  .github/prompts/issues/create-issues.prompt.md  — now writes only standalone issues, numbered from 9001, file  NNNN-slug.md ,  title: … #NNNN , strict  kubevirt-doc-issue.md  headings, KEDA-style "commissioned by CNCF" boilerplate linking cncf/techdocs#343. Coverage report gains an  ## Issues  table (number → title/label/file) that the umbrella prompt consumes. Target raised to 40–60 issues since sub-issues are now files.
•  .github/issue_template/umbrella-issue.md  — sibling-relative links, matching example numbers.
•  .github/copilot-instructions.md  — directory tree, two-pass workflow, numbering, file-name rules, filled-in "Create umbrella issues" section.

New

•  .github/prompts/issues/create-umbrella-issues.prompt.md  — reads issue files + coverage table, groups 3–10 per theme, continues numbering, writes  U-NNNN-slug.md , appends to coverage report.

On one prompt vs. two: two is better. Grouping works best when the final, writer-reviewed set of issues is the sole input, and it keeps each session's context small. The only coupling is the issue number sequence, handled via the coverage table.

Suggestions

• Move the old  issues-coverage.md  into  prev_1/ ;  /create-issues  will overwrite it.
• If the uploader supports GitHub's native sub-issues, it can use the  #NNNN  list; otherwise consider having it add a "Part of #U" line to each sub-issue.

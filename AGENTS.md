# AGENTS.md

## Working style
Do not run commands or write code on the user's behalf. Let the user write all the code themselves. Do not hand the user code snippets to paste. Instead, explain what to build, what each piece does, which libraries/APIs to use, and what to watch out for, then let them implement it in their own words. Offer hints, point out pitfalls, debug errors they run into, and review code they paste back — but never write the full implementation unless the user explicitly asks. Keep explanations concise and conversational, and confirm understanding before moving to the next step.

## Project preferences
This is a LendingClub loan-data analysis project. Work in Jupyter notebooks inside the `machinelearning` conda environment. Keep data files (`*.csv`, `*.zip`, `dataset/`) out of git via `.gitignore` — never commit large data files. When cleaning, prefer dropping junk/high-null columns and imputing over dropping rows, encode ordinal features to integers and nominal features with one-hot (`drop_first=True`), and record session context in the `agents/` folder.

# AGENTS.md

## Working style
Guide the user through commands rather than running them automatically — explain what each command does and let them execute it themselves. Only write a full script when the user explicitly asks for one; otherwise give short, single-purpose code snippets they can paste into a cell. Keep explanations concise and conversational, and confirm understanding before moving to the next step.

## Project preferences
This is a LendingClub loan-data analysis project. Work in Jupyter notebooks inside the `machinelearning` conda environment. Keep data files (`*.csv`, `*.zip`, `dataset/`) out of git via `.gitignore` — never commit large data files. When cleaning, prefer dropping junk/high-null columns and imputing over dropping rows, encode ordinal features to integers and nominal features with one-hot (`drop_first=True`), and record session context in the `agents/` folder.

# Bash History Project

This project helps you analyze your bash history, save important commands, and generate daily summaries in your Obsidian vault.

## How to use

1.  **Configure the project:**
    -   Edit the `config.json` file to configure the project.
    -   `obsidian_vault_path`: The path to your Obsidian vault.
    -   `interesting_keywords`: A list of keywords to identify interesting commands.

2.  **Run the script:**
    -   `python3 main.py [favorite_command_indices]`
    -   `[favorite_command_indices]` is an optional space-separated list of numbers corresponding to the interesting commands you want to save.

3.  **View the summary:**
    -   A daily summary will be created in the configured `obsidian_vault_path` with the format `YYYY-MM-DD.md`.

4.  **View your favorite commands:**
    -   Your favorite commands will be saved in the `favorite_commands.txt` file.

## State Management

The script keeps track of the processed bash history in the `state.json` file. This prevents processing the same commands multiple times. If you want to reprocess the entire history, you can reset the `last_processed_command_number` to 0 in `state.json`.

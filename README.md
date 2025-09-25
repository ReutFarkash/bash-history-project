# Bash History Project

This project helps you analyze your bash history, save important commands, and generate daily summaries in your Obsidian vault.

## How to use

1.  **Add your bash history:**
    -   Copy your bash history into the `bash_history.txt` file.

2.  **Run the script:**
    -   `python3 main.py [favorite_command_indices]`
    -   `[favorite_command_indices]` is an optional space-separated list of numbers corresponding to the important commands you want to save.

3.  **View the summary:**
    -   A daily summary will be created in the `obsidian_vault` directory with the format `YYYY-MM-DD.md`.

4.  **View your favorite commands:**
    -   Your favorite commands will be saved in the `favorite_commands.txt` file.

## Important commands

The script identifies important commands based on a list of keywords. You can customize these keywords by editing the `important_keywords` list in `main.py`.
import re
import sys
import json
import subprocess
from datetime import datetime

def is_interesting(command, keywords):
    for keyword in keywords:
        if re.search(r"\b" + keyword + r"\b", command):
            return True
    return False

def generate_summary(commands, keywords):
    interesting_commands = []
    for command in commands:
        if is_interesting(command, keywords):
            interesting_commands.append(command.strip())

    summary = f"## Daily Summary - {datetime.now().strftime('%Y-%m-%d')}\n\n"
    summary += f"Total commands executed: {len(commands)}\n\n"
    summary += "### Interesting commands:\n"
    for command in interesting_commands:
        summary += f"- `{command}`\n"

    return summary, interesting_commands

def get_bash_history():
    result = subprocess.run("history", shell=True, capture_output=True, text=True, executable='/bin/bash')
    return result.stdout.splitlines()

def main():
    with open("config.json", "r") as f:
        config = json.load(f)

    with open("state.json", "r") as f:
        state = json.load(f)

    last_processed_command_number = state.get("last_processed_command_number", 0)

    history_lines = get_bash_history()
    new_commands = []
    max_command_number = last_processed_command_number

    for line in history_lines:
        match = re.match(r"\s*(\d+)\s+(.*)", line)
        if match:
            command_number = int(match.group(1))
            command = match.group(2)
            if command_number > last_processed_command_number:
                new_commands.append(command)
                if command_number > max_command_number:
                    max_command_number = command_number

    if not new_commands:
        print("No new commands to process.")
        return

    interesting_keywords = config.get("interesting_keywords", [])
    summary, interesting_commands = generate_summary(new_commands, interesting_keywords)

    # Save the summary to the Obsidian vault
    vault_path = config["obsidian_vault_path"]
    today = datetime.now().strftime('%Y-%m-%d')
    summary_file = f"{vault_path}/{today}.md"

    with open(summary_file, "w") as f:
        f.write(summary)

    print(f"Daily summary saved to {summary_file}")

    # Save favorite commands
    if len(sys.argv) > 1:
        favorite_indices = [int(i) for i in sys.argv[1:]]

        with open("favorite_commands.txt", "a") as f:
            for i in favorite_indices:
                if 1 <= i <= len(interesting_commands):
                    f.write(interesting_commands[i-1] + "\n")
        print("Favorite commands saved to favorite_commands.txt")

    # Update state
    state["last_processed_command_number"] = max_command_number
    with open("state.json", "w") as f:
        json.dump(state, f)

if __name__ == "__main__":
    main()

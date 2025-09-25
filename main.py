import re
import sys
import json
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

def main():
    with open("config.json", "r") as f:
        config = json.load(f)

    bash_history_file_path = config.get("bash_history_file_path", "bash_history.txt")
    with open(bash_history_file_path, "r") as f:
        commands = f.readlines()

    if not commands:
        print("No commands to process.")
        return

    interesting_keywords = config.get("interesting_keywords", [])
    summary, interesting_commands = generate_summary(commands, interesting_keywords)

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

if __name__ == "__main__":
    main()
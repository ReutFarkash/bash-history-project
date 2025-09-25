import re
import sys
from datetime import datetime

def is_important(command):
    important_keywords = ["git", "npm", "docker", "kubectl"]
    for keyword in important_keywords:
        if re.search(r"\b" + keyword + r"\b", command):
            return True
    return False

def generate_summary(commands):
    important_commands = []
    for command in commands:
        if is_important(command):
            important_commands.append(command.strip())

    summary = f"## Daily Summary - {datetime.now().strftime('%Y-%m-%d')}\n\n"
    summary += f"Total commands executed: {len(commands)}\n\n"
    summary += "### Important commands:\n"
    for command in important_commands:
        summary += f"- `{command}`\n"

    return summary, important_commands

def main():
    with open("bash_history.txt", "r") as f:
        commands = f.readlines()

    summary, important_commands = generate_summary(commands)

    # Save the summary to the Obsidian vault
    vault_path = "obsidian_vault"
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
                if 1 <= i <= len(important_commands):
                    f.write(important_commands[i-1] + "\n")
        print("Favorite commands saved to favorite_commands.txt")

if __name__ == "__main__":
    main()

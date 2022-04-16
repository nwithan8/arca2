"""
Run to install dependencies for all cogs in the bot.
"""

import os
import pip

if __name__ == "__main__":
    cog_list = []
    with open("cog_list.txt", "r") as f:
        for line in f.readlines():
            cog_list.append(line.strip())

    for cog in cog_list:
        requirements_file_path = f"cogs/{cog}/requirements.txt"
        if os.path.exists(requirements_file_path):
            pip.main(["install", "-r", requirements_file_path])
        else:
            print(f"No requirements file found for {cog}")
            continue
        print(f"Installed requirements for {cog}")
    print("Done!")

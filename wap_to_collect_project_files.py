import os

# Absolute path to your project
root_dir = "/Users/rohitkumar/Developer/full_stack_pp"

# Output file will be created in the current working directory (DSA folder)
output_file = "project.txt"

# Explicit files to exclude
excluded_files = {
    "Rohit_CSE_VII_2022-26.pdf",
    "requirements.txt",
    ".DS_Store",
    ".gitignore",
}

# Directories to exclude
excluded_dirs = {
    "__pycache__",
    ".git",
    ".fsvenv",
}

with open(output_file, "w", encoding="utf-8") as out:
    for foldername, subfolders, filenames in os.walk(root_dir):
        # Skip excluded directories (in place modification of subfolders avoids descending into them)
        subfolders[:] = [d for d in subfolders if d not in excluded_dirs]

        for filename in filenames:
            # Skip excluded files and extensions
            if (filename in excluded_files):
                continue

            filepath = os.path.join(foldername, filename)
            relpath = os.path.relpath(filepath, root_dir)  # relative path for header

            try:
                # Open file in read-only mode
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception as e:
                print(f"Skipping {filepath} (error: {e})")
                continue

            # Write header and content into project.txt
            out.write(f"\n\n#{relpath}\n\n")
            out.write(content)
            out.write("\n\n")  # ensure separation

print("Project files have been collected into project.txt")
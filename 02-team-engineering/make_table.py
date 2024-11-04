import os

# Define the directory containing the files
directory = "transcript/summaries/02-team-engineering"

# Initialize an empty list to hold the index entries
index_entries = []

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".md"):  # Assuming the files are Markdown files
        # Create a description (customize this as needed)
        description = f"This is the summary for {filename.replace('.md', '')}."

        # Create a link to the file
        file_link = f"[{filename}]({os.path.join(directory, filename)})"

        # Append the entry to the list
        index_entries.append(f"- {file_link}: {description}")

# Write the index to a README.md file
with open("README.md", "w") as readme_file:
    readme_file.write("# Index of Summaries\n\n")
    readme_file.write("\n".join(index_entries))

print("Index created successfully in README.md.")

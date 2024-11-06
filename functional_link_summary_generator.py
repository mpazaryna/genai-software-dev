import sys
from pathlib import Path
from typing import Dict, List, Tuple

import yaml


def load_config(config_path: str) -> dict:
    """Load configuration from YAML file"""
    try:
        with open(config_path, "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading config: {e}")
        sys.exit(1)


def find_summary_files(module_path: Path, module_name: str) -> List[Path]:
    """Find all markdown files in the summaries directory for given module"""
    summaries_path = module_path / "transcripts" / "summaries"
    if not summaries_path.exists():
        print(f"Summaries directory not found: {summaries_path}")
        return []

    return sorted(summaries_path.rglob("*.md"))


def organize_files_by_week(
    files: List[Path], base_path: Path
) -> Dict[str, List[Tuple[str, Path]]]:
    """Organize files by week and create (title, relative_path) tuples"""
    organized: Dict[str, List[Tuple[str, Path]]] = {}

    for file_path in files:
        # Get the parent directory name (could be 'module-01' or similar)
        week = file_path.parent.name

        # Create readable title from filename
        title = file_path.stem.replace("-", " ").replace("_", " ").title()

        # Create relative path from base directory (module root)
        relative_path = file_path.relative_to(base_path)

        if week not in organized:
            organized[week] = []
        organized[week].append((title, relative_path))

    return organized


def generate_markdown_content(
    organized_files: Dict[str, List[Tuple[str, Path]]]
) -> str:
    """Generate markdown content for the README"""
    content = []

    for module in sorted(organized_files.keys()):
        # Add module header if it's not a general category
        if module.startswith("module-"):
            content.append(f"\n### {module.replace('-', ' ').title()}\n")

        # Add files within this module
        for title, path in sorted(organized_files[module]):
            content.append(f"- [{title}]({path})")

    return "\n".join(content)


def update_readme(readme_path: Path, new_content: str) -> None:
    """Update or create README with new summary content"""
    start_marker = "<!-- BEGIN SUMMARIES -->\n"
    end_marker = "<!-- END SUMMARIES -->\n"
    summaries_header = "## Lecture Summaries\n\n"

    try:
        # Read existing content or create new
        if readme_path.exists():
            with open(readme_path, "r", encoding="utf-8") as f:
                current_content = f.read()
        else:
            current_content = "# Course Module\n\n"

        # Create new summary section
        new_section = (
            summaries_header + start_marker + new_content + "\n\n" + end_marker
        )

        # Replace existing section or append new one
        if start_marker in current_content:
            start_idx = current_content.find(start_marker) - len(summaries_header)
            end_idx = current_content.find(end_marker) + len(end_marker)
            final_content = (
                current_content[:start_idx] + new_section + current_content[end_idx:]
            )
        else:
            final_content = current_content.rstrip() + "\n\n" + new_section

        # Write updated content
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(final_content)

        print(f"Successfully updated {readme_path}")

    except Exception as e:
        print(f"Error updating README: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <config.yml>")
        sys.exit(1)

    # Load configuration
    config = load_config(sys.argv[1])

    # Setup paths
    module_name = config["module"]
    module_path = Path(config["module_path"])
    readme_path = module_path / config["readme_path"]

    # Find and process files
    summary_files = find_summary_files(module_path, module_name)
    if not summary_files:
        print("No summary files found")
        sys.exit(1)

    # Organize files and generate content
    organized_files = organize_files_by_week(summary_files, module_path)
    markdown_content = generate_markdown_content(organized_files)

    # Update README
    update_readme(readme_path, markdown_content)


if __name__ == "__main__":
    main()

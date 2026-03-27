from python.helpers import files, file_tree
from python.helpers.tool import Tool, Response
import os

class FullStackAudit(Tool):
    async def execute(self, **kwargs):
        # Get project structure
        project_name = self.agent.context.get_data("project")
        if project_name:
            from python.helpers.projects import get_project_folder
            base_path = get_project_folder(project_name)
        else:
            from python.helpers.settings import get_settings
            base_path = get_settings().get("workdir_path")

        tree = file_tree.file_tree(base_path, max_depth=5)

        # Check for important files
        files_to_check = [
            "package.json", "requirements.txt", "pyproject.toml",
            "docker-compose.yml", "Dockerfile", ".env", "README.md",
            "docs/blueprint.md", "docs/app_architecture.md"
        ]

        found_files = []
        for f in files_to_check:
            if files.exists(os.path.join(base_path, f)):
                found_files.append(f)

        # Analyze dependencies if package.json exists
        deps = ""
        pkg_json_path = os.path.join(base_path, "package.json")
        if files.exists(pkg_json_path):
            try:
                import json
                data = json.loads(files.read_file(pkg_json_path))
                deps = f"Dependencies: {list(data.get('dependencies', {}).keys())}"
            except: pass

        result = f"""# Full-Stack Project Audit
## Directory Structure
{tree}

## Critical Files Found
{', '.join(found_files)}

## Environment Analysis
{deps}

## Recommendations
- Ensure API documentation exists if you have a backend.
- Check for consistent type usage between frontend and backend.
- Verify that .env.example is provided for the user.
"""
        return Response(message=result, break_loop=False)

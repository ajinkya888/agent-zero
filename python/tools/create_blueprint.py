from python.helpers import files
from python.helpers.tool import Tool, Response
import os

class CreateBlueprint(Tool):
    async def execute(self, name="", content="", **kwargs):
        if not name or not content:
            return Response(message="Blueprint name and content are required.", break_loop=False)

        # Ensure valid filename
        safe_name = files.safe_file_name(name) or "blueprint"
        if not safe_name.endswith(".md"):
            filename = safe_name + ".md"
        else:
            filename = safe_name

        # Save to current project or workdir
        project_name = self.agent.context.get_data("project")
        if project_name:
            from python.helpers.projects import get_project_folder
            base_path = get_project_folder(project_name)
        else:
            from python.helpers.settings import get_settings
            base_path = get_settings().get("workdir_path")

        filepath = os.path.join(base_path, "docs", filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        files.write_file(filepath, content)

        result = f"Blueprint '{safe_name}' created successfully at {filepath}. Follow this plan strictly."
        return Response(message=result, break_loop=False)

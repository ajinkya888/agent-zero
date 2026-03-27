from python.helpers import files
from python.helpers.tool import Tool, Response
import os

class CreateTool(Tool):
    async def execute(self, name="", description="", code="", **kwargs):
        if not name or not code:
            return Response(message="Tool name and code are required.", break_loop=False)

        # Ensure valid filename
        safe_name = files.safe_file_name(name)
        if not safe_name.endswith(".py"):
            filename = safe_name + ".py"
        else:
            filename = safe_name

        filepath = os.path.join("usr/tools", filename)

        # Check if already exists
        if files.exists(filepath):
            return Response(message=f"Tool '{safe_name}' already exists. Use code execution to modify it if needed.", break_loop=False)

        # Add boilerplate if missing
        if "class" not in code or "Tool" not in code:
             return Response(message="Provided code must contain a class inheriting from Tool.", break_loop=False)

        files.write_file(filepath, code)

        result = f"Tool '{safe_name}' created successfully at {filepath}. You can now use it in your next turn by its name: '{safe_name.replace('.py','')}'."
        return Response(message=result, break_loop=False)

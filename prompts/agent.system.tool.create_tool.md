### create_tool:
Create a new permanent tool by saving a Python script.
Use this when you have a complex task that you want to automate for future use.
The code must contain a class inheriting from `Tool`.

usage:
~~~json
{
    "thoughts": [
        "I need a tool to handle specific file conversions...",
    ],
    "headline": "Creating a new custom tool",
    "tool_name": "create_tool",
    "tool_args": {
        "name": "my_new_tool",
        "description": "Short description of what the tool does",
        "code": "from python.helpers.tool import Tool, Response\n\nclass MyNewTool(Tool):\n    async def execute(self, **kwargs):\n        return Response(message='Success!', break_loop=False)"
    }
}
~~~

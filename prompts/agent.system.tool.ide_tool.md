### ide_tool:
Control the web-based IDE interface to help the user follow your work.
Actions:
- `open_file`: Opens the specified file in the code editor for the user to see.
- `close_file`: Closes the current editor.

usage:
~~~json
{
    "thoughts": [
        "I've updated the main logic, I'll open it for the user to review.",
    ],
    "headline": "Opening file in editor",
    "tool_name": "ide_tool",
    "tool_args": {
        "action": "open_file",
        "path": "src/main.py"
    }
}
~~~

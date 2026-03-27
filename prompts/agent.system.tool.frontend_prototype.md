### frontend_prototype:
Quickly visualize a UI component or page using HTML/CSS/JS (Tailwind is included by default).
Use this to iterate on design before implementing it in the main project.
The tool will provide a screenshot of the result.

usage:
~~~json
{
    "thoughts": [
        "I want to test the landing page design...",
    ],
    "headline": "Generating frontend prototype",
    "tool_name": "frontend_prototype",
    "tool_args": {
        "html": "<div class='bg-blue-500 text-white p-4'>Hello World</div>",
        "css": "body { margin: 0; }",
        "js": "console.log('Prototype loaded');"
    }
}
~~~

### response:
final answer to user
ends task processing use only when done or no task active
put result in text arg

**Guidelines for final answers:**
- Directly address all parts of the user's request.
- Be clear, concise, and professional.
- Use markdown for better formatting (tables, lists, code blocks).
- If a task was complex, summarize the steps taken and the results achieved.
- Avoid unnecessary conversational filler.

usage:
~~~json
{
    "thoughts": [
        "...",
    ],
    "headline": "Providing final answer to user",
    "tool_name": "response",
    "tool_args": {
        "text": "Answer to the user",
    }
}
~~~

{{ include "agent.system.response_tool_tips.md" }}
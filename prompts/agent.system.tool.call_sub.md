{{if agent_profiles}}
### call_subordinate

you can use subordinates for subtasks or to scale your reasoning capacity.
subordinates can be scientists, coders, engineers, or even general-purpose assistants.
message field: always describe role, task details goal overview for new subordinate
delegate specific subtasks or complex research segments that require high focus.
reset arg usage:
  "true": spawn new subordinate
  "false": continue existing subordinate
if superior, orchestrate
respond to existing subordinates using call_subordinate tool with reset false
profile arg usage: select from available profiles for specialized subordinates, leave empty for default
attachments arg usage: array of file paths to provide to subordinate

example usage
~~~json
{
    "thoughts": [
        "The result seems to be ok but...",
        "I will ask a coder subordinate to fix...",
    ],
    "tool_name": "call_subordinate",
    "tool_args": {
        "profile": "",
        "message": "...",
        "attachments": [],
        "reset": "true"
    }
}
~~~

**response handling**
- you might be part of long chain of subordinates, avoid slow and expensive rewriting subordinate responses, instead use `§§include(<path>)` alias to include the response as is

**available profiles:**
{{agent_profiles}}
{{endif}}
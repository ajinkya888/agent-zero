from typing import Any
from python.helpers.extension import Extension
from python.helpers import messages

SUMMARIZE_THRESHOLD = 2000

class SummarizeToolResult(Extension):
    async def execute(self, data: dict[str, Any] | None = None, **kwargs):
        if not data:
            return

        # get tool call result
        result = data.get("tool_result")
        if not isinstance(result, str) or len(result) < SUMMARIZE_THRESHOLD:
            return

        # Skip if already summarized
        if data.get("summarized"):
            return

        try:
            # Use utility model to summarize
            summary = await self.agent.call_utility_model(
                system=self.agent.read_prompt("fw.tool_result_summary.sys.md"),
                message=result
            )

            if summary and len(summary) < len(result):
                # Update tool_result with summary
                file_info = f" (saved to {data['file']})" if "file" in data else " (saved to file)"
                data["tool_result"] = f"[SUMMARY]: {summary}\n\n[Full output{file_info}]"
                data["summarized"] = True

        except Exception as e:
            # Fallback to simple truncation if summarization fails
            pass

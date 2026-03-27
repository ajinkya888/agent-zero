from python.helpers.tool import Tool, Response

class Reflect(Tool):
    async def execute(self, thoughts="", **kwargs):
        if not thoughts:
            return Response(message="Please provide your thoughts for reflection.", break_loop=False)

        # Reflection doesn't actually 'do' anything but adds the agent's internal monologue to the history
        # which helps in complex reasoning tasks.
        return Response(message=f"Reflection completed. You have analyzed: {thoughts}. Now proceed with your next move based on this analysis.", break_loop=False)

    def get_log_object(self):
        return self.agent.context.log.log(
            type="thought",
            heading=f"icon://psychology {self.agent.agent_name}: Reflecting",
            content=self.args.get("thoughts", ""),
            kvps=self.args,
        )

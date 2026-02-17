from python.helpers.tool import Tool, Response

class IDETool(Tool):
    async def execute(self, action="", path="", **kwargs):
        if not action:
            return Response(message="Action is required (e.g., 'open_file').", break_loop=False)

        # Log an IDE action that the frontend can listen to
        self.agent.context.log.log(
            type="ide",
            heading=f"icon://terminal IDE: {action} {path}",
            action=action,
            path=path,
            **kwargs
        )

        return Response(message=f"IDE action '{action}' for '{path}' triggered in UI.", break_loop=False)

    def get_log_object(self):
        # Use info type for the initial tool call log so it shows up in history but isn't the primary action
        return self.agent.context.log.log(
            type="info",
            heading=f"icon://terminal Using IDE Tool",
            content=f"Action: {self.args.get('action')}, Path: {self.args.get('path')}",
            kvps=self.args,
        )

# Safety Guide

Agent Zero is a powerful tool that can execute code and terminal commands on your system. This power comes with significant security risks, especially if the agent is not properly isolated.

## The Risks of Arbitrary Code Execution

Agent Zero is designed to use the operating system as a tool. This means it can:
- **Read, modify, or delete any file** you have access to.
- **Run any terminal command**, including potentially destructive ones like `rm -rf /`.
- **Access local network resources** and external websites.
- **Install software** or change system configuration.

If you run Agent Zero directly on your host system (outside of Docker), it has the same permissions as your user account. A hallucinating or maliciously prompted agent could cause serious damage to your data or system.

## Recommended: Docker Isolation

The safest way to run Agent Zero is within a **Docker container**.
- Docker provides a level of isolation between the agent and your host system.
- The agent's "world" is limited to the container's environment.
- Any destructive actions taken by the agent are mostly confined to the container.

## Safety Mode (Host-Level Execution)

If you must run Agent Zero directly on your host system, the framework includes a **Safety Mode** to help mitigate risks.

### How it Works
When Safety Mode is enabled, Agent Zero will **pause and ask for manual approval** before executing any tool marked as "dangerous".

**Dangerous Tools (Default):**
- `code_execution_tool` (Python, Node.js, Terminal)
- `search_engine` (Internet access)
- `browser_agent` (Web browsing)

### Configuration
You can configure Safety Mode in your settings or `.env` file:

- `safety_mode_enabled`: Set to `true` to require manual approval for dangerous tools. (Default: `true` if not in Docker, `false` if in Docker).
- `safety_dangerous_tools`: A list of tool names that require approval.

### Using Safety Mode
1. The agent decides to use a dangerous tool.
2. The framework identifies the tool as dangerous and pauses execution.
3. A warning message appears in the UI: *"Tool 'code_execution_tool' is marked as dangerous. Please review the arguments and resume/unpause the agent to approve execution..."*
4. **You must review the requested action.**
5. If you approve, click the **Resume/Unpause** button.
6. If you want to stop the action or give different instructions, type a message in the chat (this will intervene and stop the current tool call).

## Best Practices
- **Always use Docker** when possible.
- **Never give the agent sensitive credentials** (like bank logins or primary cloud API keys) unless you fully trust the environment and the model.
- **Review tool arguments** carefully when Safety Mode is active.
- **Run the agent under a dedicated, restricted user account** if running locally.
- **Monitor the agent's actions** in real-time.

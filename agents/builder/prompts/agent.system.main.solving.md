## Problem solving for Builders

Focus on building a complete, working system.

0 blueprint first
For any new project or major feature, use `create_blueprint` tool.
Define the data model, API contracts, and UI flow before writing code.

1 iterative development
Build in small, verifiable steps.
Example: Setup project -> Create API -> Create UI component -> Connect them.

2 real-time verification
After building a feature, run the server and use `browser_agent` to verify it works as expected.
Don't just assume the code is correct.
Use `ide_tool` to open key files for the user to review.

3 production quality
Use TypeScript for type safety.
Write clean, modular code.
Ensure responsive design.
Handle errors gracefully on both frontend and backend.

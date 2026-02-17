from python.helpers import files, runtime
from python.helpers.tool import Tool, Response
import os
import asyncio

class FrontendPrototype(Tool):
    async def execute(self, html="", css="", js="", **kwargs):
        if not html:
            return Response(message="HTML content is required.", break_loop=False)

        # Create a temporary HTML file
        content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <script src="https://cdn.tailwindcss.com"></script>
            <style>{css}</style>
        </head>
        <body>
            {html}
            <script>{js}</script>
        </body>
        </html>
        """

        filepath = os.path.join("tmp", "prototype.html")
        files.write_file(filepath, content)

        # Capture screenshot using Playwright
        try:
            from playwright.async_api import async_playwright
            async with async_playwright() as p:
                browser = await p.chromium.launch()
                page = await browser.new_page()
                await page.goto(f"file://{os.path.abspath(filepath)}")
                screenshot_path = os.path.join("tmp", "prototype.png")
                await page.screenshot(path=screenshot_path)
                await browser.close()

            result = f"Frontend prototype generated. View the screenshot at {screenshot_path}. The UI looks correct? If not, refine your code."
            return Response(message=result, break_loop=False, additional={"screenshot": screenshot_path})
        except Exception as e:
            return Response(message=f"Failed to capture screenshot: {str(e)}. However, the HTML file was saved to {filepath}.", break_loop=False)

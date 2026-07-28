from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from jinja2 import Template

from app import config

app = FastAPI(
    title="Try Hack Me",
    description="A sample project that will be hacked soon.",
    version="0.0.1337",
    debug=config.DEBUG,
)


@app.get("/", response_class=HTMLResponse)
async def try_hack_me(name: str = config.SUPER_SECRET_NAME):
    """
    Root endpoint that greets the user and provides a random text.

    Args:
        name (str, optional): Name of the user. Defaults to SUPER_SECRET_NAME.

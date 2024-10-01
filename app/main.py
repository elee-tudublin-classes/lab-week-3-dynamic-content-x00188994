# import dependencies
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime

# create app instance
app = FastAPI()

# set location for templates
templates = Jinja2Templates(directory="app/view_templates")

# handle http get requests for the site root /
# return the index.html page
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):

    serverTime: datetime = datetime.now().strftime("")
    return templates.TemplateResponse("index.html", {"request": request})




app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)

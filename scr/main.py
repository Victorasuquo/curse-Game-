from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import random

app = FastAPI()

# Static files and templates setup
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Tuples for curses
adjectives = ("green", "dirty", "vomit-covered", "self-loathing", "slimy", "spiky", "rotten", "crusty", "smelly", "filthy")
nouns = ("worm", "washing machine", "driver", "monster", "robot", "toaster", "dog", "cat", "alien", "ghost")
verbs = ("eats", "destroys", "annoys", "crushes", "smashes", "licks", "fights", "jumps on", "haunts", "stomps on")

# Generate a random curse
def generate_curse():
    adj1 = random.choice(adjectives)
    adj2 = random.choice(adjectives)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    return f"You {adj1} {adj2} {noun} who {verb}!"

# Home route
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    curse = generate_curse()
    return templates.TemplateResponse("index.html", {"request": request, "curse": curse})

# API endpoint to generate curses
@app.get("/generate_curse")
async def generate_curse_api():
    return {"curse": generate_curse()}

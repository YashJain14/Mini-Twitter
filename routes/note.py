from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from typing import Union
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates
from bson import ObjectId
from fastapi.responses import RedirectResponse

note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = list(conn.notes.notes.find({}))
    newDocs = [noteEntity(doc) for doc in docs]
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})

@note.post("/")
async def add_note(request: Request):
    form = await request.form()
    note = {"title": form.get("title"), "desc": form.get("desc")}
    conn.notes.notes.insert_one(note)
    # Redirect to the homepage or another specified route after adding the note
    return RedirectResponse(url="/", status_code=303)
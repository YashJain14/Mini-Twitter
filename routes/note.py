from fastapi import APIRouter, Request, Form
from models.note import Note, Comment
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from bson import ObjectId

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
    note = {"title": form.get("title"), "desc": form.get("desc"), "comments": []}
    conn.notes.notes.insert_one(note)
    return RedirectResponse(url="/", status_code=303)

@note.post("/{note_id}/comment")
async def add_comment(note_id: str, text: str = Form(...)):
    comment = {"text": text}
    conn.notes.notes.update_one({"_id": ObjectId(note_id)}, {"$push": {"comments": comment}})
    return RedirectResponse(url="/", status_code=303)

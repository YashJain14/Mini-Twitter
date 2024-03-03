def noteEntity(item) -> dict:
    return {
        "id": str(item["_id"]),  # Convert ObjectId to string
        "title": item["title"],
        "desc": item["desc"]
    }

def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]

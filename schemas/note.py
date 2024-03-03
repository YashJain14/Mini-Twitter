def noteEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "desc": item["desc"],
        "comments": [commentEntity(comment) for comment in item.get("comments", [])]
    }

def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]

def commentEntity(comment) -> dict:
    return {
        "user": comment.get("user", "Anonymous"),
        "text": comment["text"]
    }

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def read_root():
    return { "msg": "MJAU!", "v": "0.2000" }


@app.get("/items/{id}")
def read_item(item_id: int, q: str = None):
    return {"id": id, "q": q}

@app.get("/api/ip")
def get_ip(request: Request):
    return { "ID": request.client.host}

@app.get("/ip")
def get_ip(request: Request):
    return f"<h1>din ip är: {request.clinet.host}</h1>"

@app.get("/rooms")
def get_rooms():
    return [{"room":1,"beds":3},{"room":2,"beds":2},{"room":3,"beds":4}]
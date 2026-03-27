from fastapi import FastAPI, Request, Response

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

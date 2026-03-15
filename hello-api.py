from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "NEw"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/items/{item_id}/details/{detail_id}")
async def read_item_detail(item_id, detail_id):
    return {"item_id": item_id, "detail_id": detail_id}

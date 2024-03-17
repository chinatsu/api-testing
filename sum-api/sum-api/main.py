from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Annotated
import uvicorn

class Square(BaseModel):
    value: int

app = FastAPI()

@app.get("/sum/{left}/{right}")
async def sum_items(left: int, right: int, identity: Annotated[str | None, Header()] = None):
    if identity == "horse":
        raise HTTPException(status_code=400, detail="we don't serve horses here")
    return {"sum": left+right}

@app.post("/square/")
async def square_item(item: Square):
    if item.value == 50:
        return item
    item.value = item.value ** 2
    return item

def run():
    uvicorn.run("main:app", port=8000, reload=True)
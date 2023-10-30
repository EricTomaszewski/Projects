# https://fastapi.tiangolo.com/

from typing import Union

from fastapi import FastAPI

import uvicorn


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")
    
# runs on Docker
# but instead of a default link (0.0.0.0:8000) that will be given for a click
# change browser address to either:
# localhost:8000
# OR
# 127.0.0.1:8000
# then also try
# either of the 2 above ./items/5 (or any other number)
# -*- coding: utf-8 -*-

from fastapi import FastAPI

app = FastAPI()

#*********************************************************************
#* read_item - /items/{item_id}
#*********************************************************************

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id + 'AAA'}

#*********************************************************************
#* root - /
#*********************************************************************

@app.get("/")
async def root():
    return {"message": "Hello World - udało się"}

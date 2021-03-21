# -*- coding: utf-8 -*-

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

#*********************************************************************
#* class Utterance
#*********************************************************************

class Utterance(BaseModel):
    
    text: str

#*********************************************************************
#* app = FastAPI()
#*********************************************************************

app = FastAPI()

#*********************************************************************
#* route - /
#*********************************************************************

@app.get("/")
def root():
    
    a = "a"
    b = "b" + a
    
    return {"hello world": b}

#*********************************************************************
#* route - /alium-at/process_utterence/
#*********************************************************************

@app.post('/alium-at/process_utterance/')
async def process_utterance(utterance: Utterance):
    
    return utterance.text + ' ' + 'Pamparampa!'

#*********************************************************************
#* MAIN
#*********************************************************************

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
    

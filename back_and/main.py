from enum import Enum
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from Personagens import listPersonas,Personagem
import random

target:Personagem | None=None

app = FastAPI()

origins=[
      "http://localhost:3000",
]
app.add_middleware(
     CORSMiddleware,
    allow_origins=origins,        
    allow_credentials=True,
    allow_methods=["*"],          
    allow_headers=["*"],

)

app.mount("/imgs",StaticFiles(directory="imgs"),name="imgs")

@app.get("/")
async def ColetandoLista():
    ListaFinal={}
    
    for i in range(3):
          ListaFinal[i]={"Name":listPersonas[i].name,"clan":listPersonas[i].clan,"imagen":listPersonas[i].img}
          

    if len(ListaFinal)>0:
        return ListaFinal
    else:
          raise HTTPException(status_code=404, detail="Personagem não encontrado")

@app.get("/personagens/{personagem}")
async def LocalizandoPErsonagem(personagem:str):
        targetvalid=False
        for x in listPersonas:
               if x.name.lower()==personagem.lower():
                    targetvalid=True
                    target=x
                    break
                
        
        if targetvalid:
              return target
        else:
              raise HTTPException(status_code=404, detail="Personagem não encontrado")

  
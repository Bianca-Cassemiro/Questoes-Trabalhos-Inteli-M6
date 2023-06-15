from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from supabase import create_client, Client
from ultralytics import YOLO
from supabase.client import Client
import cv2
import base64
from pydantic import BaseModel

# Carregar imagem
crack = cv2.imread(filename="download1.jpeg")

# Inicializar o modelo YOLO
model = YOLO('best.pt')

# Realizar a detecção de objetos
result = model.predict(source=crack, show=True,conf=0.5, save=True)
app = FastAPI()
 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# URL e Chave de acesso 
url: str = "https://jtrbxmmbuwibuusemgpj.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imp0cmJ4bW1idXdpYnV1c2VtZ3BqIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODY0NDM5MjYsImV4cCI6MjAwMjAxOTkyNn0.V6cYf-5A4kpad2HgGtgWmcDkQLdG41yGKSicFbe77JA" #eu não ia deixar a minha porque é secreta né rs 
supabase: Client = create_client(url, key)


class Imagem(BaseModel):
    id: int
    imagem: str
   
schema_name = "public"  
table_name = "table"


@app.post("/images")
async def images(request: Request):
    supabase = create_client(url, key)
    with open("runs/detect/predict2/image0.jpg", 'rb+') as f:
        my_string = base64.b64encode(f.read()).decode('utf-8')

        response = supabase.table(table_name).insert({"image": my_string}).execute()
        print(response)
    return {"message": "Image uploaded successfully"}
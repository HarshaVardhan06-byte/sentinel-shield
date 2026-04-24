
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=["*"])

model=joblib.load("login_security_model.pkl")
vectorizer=joblib.load("vectorizer.pkl")
logs=[]

class LoginData(BaseModel):
    email:str
    password:str

@app.post("/login")
def login(data:LoginData):
    user_input=data.email+" "+data.password
    pred=model.predict(vectorizer.transform([user_input]))[0]
    status="BLOCKED" if pred=="hacker" else "SUCCESS"
    logs.append({"email":data.email,"status":status})
    return {"status":status}

@app.get("/logs")
def get_logs():
    return logs

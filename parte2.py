# Parte 2 construcción de API
# El patrón de diseño es porque puede ser email o sms

import os
from fastapi import FastAPI, HTTPException
from abc import ABC, abstractmethod
from pydantic import BaseModel #Es para el body

#Usando el patrón Factory
class NotificationChannel(ABC):
    @abstractmethod
    def send_notification(self, user_id, message):
        pass

class EmailNotificationChannel(NotificationChannel):
    def send_notification(self, user_id, message):
        print(f"Enviando email a {user_id}: {message}")

class SMSNotificationChannel(NotificationChannel):
    def send_notification(self, user_id, message):
        print(f"Enviando SMS a {user_id}: {message}")

def NotificationFactory(channel):
    if channel == "email":
        return EmailNotificationChannel()
    elif channel == "sms":
        return SMSNotificationChannel()
    else:
        raise ValueError(f"Canal no soportado: {channel}")


# API
#pydantic
class NotificationRequest(BaseModel):
    userId: str
    message: str
    channel: str

app = FastAPI()

@app.post("/notifications")
async def send_notification(body: NotificationRequest):
    # El body tiene userId, message, channel
    # print("Recibido:", body)
    user_id = body.userId
    message = body.message
    channel = body.channel
    try:
        notification_service = NotificationFactory(channel)
        notification_service.send_notification(user_id, message)
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))
    if not os.path.exists("logs"):
        os.makedirs("logs")
    #Y ahora lo guardamos en un txt porque es más simple
    with open("logs/notifications.txt", "a") as f:
        f.write(f"UserId: {user_id}, Message: {message}, Channel: {channel}\n")
    return {"status": "success"}


@app.get("/notifications")
async def get_notifications():
    # data es la lista con la información de las notificaciones
    data = []
    try:
        with open("logs/notifications.txt", "r") as f:
            for line in f:
                parts = line.strip().split(", ")
                notification = {}
                for part in parts:
                    key, value = part.split(": ")
                    notification[key] = value
                data.append(notification)
    except FileNotFoundError:
        return {"data": []} #retornar nada, porque no existe el archivo
    return {"data": data}



from fastapi.testclient import TestClient
from parte2 import app
import os

client = TestClient(app)

#TC1
def test_send_notification_valid():
    # Hacer POST a /notifications con el body que está en test data
    response = client.post("/notifications", json={
        "userId": "123",
        "message": "Hola",
        "channel": "sms"
    })
    # Verificar el código de respuesta HTTP
    assert response.status_code == 200

    # Abrir notifications.txt y leer el registro
    with open("logs/notifications.txt", "r") as f:
        lines = f.readlines()
        assert any("UserId: 123, Message: Hola, Channel: sms" in line for line in lines)

#TC2
def test_get_notifications():
    response = client.get("/notifications")
    assert response.status_code == 200
    data = response.json().get("data", [])
    assert isinstance(data, list)

#TC3
def test_send_notification_invalid_channel():
    response = client.post("/notifications", json={
        "userId": "123",
        "message": "Hola",
        "channel": "algo"
    })
    assert response.status_code == 500

    with open("logs/notifications.txt", "r") as f:
        lines = f.readlines()
        assert not any("UserId: 123, Message: Hola, Channel: algo" in line for line in lines)

#TC4
def test_get_notifications_no_file():
    #borramos el archivo
    if os.path.exists("logs/notifications.txt"):
        os.remove("logs/notifications.txt")

    response = client.get("/notifications")
    assert response.status_code == 200
    data = response.json().get("data", [])
    assert data == []

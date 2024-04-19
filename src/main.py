# filename: main.py in /src directory
from fastapi import FastAPI
from data_cls import IDGAF
app = FastAPI(title="Wheelchair Control API", version="1.0", description="An API for controlling a wheelchair's movement.")


@app.get("/on")
def power_on():
    """Turns the wheelchair on"""
    if not IDGAF.is_on:
        IDGAF.is_on = True
    else:
        raise Exception("YOU IDIOT")

    return {"status": "Wheelchair powered on. Ready for a ride to Mars?"}

@app.get("/off")
def power_off():
    """Turns the wheelchair off"""
    if IDGAF.is_on:
        IDGAF.is_on = False
    else:
        raise Exception("YOU IDIOT")
    return {"status": "Wheelchair powered off. Hope you enjoyed your little adventure!"}

@app.post("/forward")
def move_forward():
    """Moves the wheelchair forward"""
    return {"action": "Moving forward. Watch out for any alien invaders!"}

@app.post("/backward")
def move_backward():
    """Moves the wheelchair backward"""
    return {"action": "Moving backward. Beep... Beep... Beep..."}

@app.post("/left")
def turn_left():
    """Turns the wheelchair left"""
    return {"action": "Turning left. Wave goodbye to the Martians!"}

@app.post("/right")
def turn_right():
    """Turns the wheelchair right"""
    return {"action": "Turning right. Say hi to the Saturnians!"}

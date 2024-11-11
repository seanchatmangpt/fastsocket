# events/user_updated.py

from pydantic import BaseModel, EmailStr


# Define Pydantic model for validation
class UserUpdatedData(BaseModel):
    userId: str
    fullName: str
    email: EmailStr
    age: int


# Event handler function
async def handle_event(sid: str, data: UserUpdatedData, sio, logger):
    logger.info(f"Handling user update for SID '{sid}' with data: {data.dict()}")

    # Here you can add any logic, such as updating the user's information in a database
    # Emit a success acknowledgment back to the client
    await sio.emit("userUpdated_ack", {"status": "success", "message": "User profile updated successfully"}, room=sid)

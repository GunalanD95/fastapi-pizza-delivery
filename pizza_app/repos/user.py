from fastapi import HTTPException
from ..model import models
from werkzeug.security import generate_password_hash

# function to create a User
def create_user(request, db): # get db is used to make connection with our database
    user = db.query(models.User).filter(models.User.username == request.username).first()
    email = db.query(models.User).filter(models.User.email_id == request.email_id).first()
    if user or email:
        if user:
            raise HTTPException(status_code=409,detail=f'A user is already present with the name {request.username}')
        elif email:
            raise HTTPException(status_code=409,detail=f'A user is already present with the email {request.email_id}')
    
    newUser = models.User(
        username  = request.username,
        email_id  = request.email_id,
        password  = generate_password_hash(request.password),
        is_staff  = request.is_staff,
        logged_in = request.logged_in,
    )
    db.add(newUser)
    db.commit()
    db.refresh(newUser)

    return newUser

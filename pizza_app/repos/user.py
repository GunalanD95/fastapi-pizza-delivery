from fastapi import HTTPException
from ..model import models
from werkzeug.security import generate_password_hash , check_password_hash
from fastapi.encoders import jsonable_encoder

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


# function to login user
def login_user(request, Authorize, db):
    user = db.query(models.User).filter(models.User.username == request.username).first()

    if not user:
        raise HTTPException(status_code=404, detail='This User doesnt not exist in database')

    if check_password_hash(user.password, request.password):
        # subject identifier for who this token is for example id or username from database
        access_token = Authorize.create_access_token(subject=request.username)
        refresh_token = Authorize.create_refresh_token(subject=request.username)

        response = {
            'access': access_token,
            'refresh': refresh_token,
        }

        return jsonable_encoder(response)

    else:
        raise HTTPException(status_code=404, detail='The Password does not match')

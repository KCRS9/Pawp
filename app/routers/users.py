from fastapi import APIRouter, Depends, Header, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.models import UserIn, UserOut, UserDb, UserBase, UserRole
from app.auth.auth import create_access_token, Token, verify_password, oauth2_scheme, decode_token, TokenData
from app.database import insert_user, get_user_by_email, get_all_users
from pydantic import BaseModel

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def create_user(userIn: UserIn):
    userDb = get_user_by_email(userIn.email)
    if userDb:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists"
        )
    
    # Defaults
    if not userIn.role:
        userIn.role = UserRole.user
        
    insert_user(
        UserDb(
            name=userIn.name,
            email=userIn.email,
            password=userIn.password, 
            role=userIn.role,
            location=userIn.location
        )
    )

    from app.auth.auth import get_hash_password
    hashed = get_hash_password(userIn.password)
    
    # Overwriting the previous insert call idea
    insert_user(
        UserDb(
            name=userIn.name,
            email=userIn.email,
            password=hashed,
            role=userIn.role,
            location=userIn.location
        )
    )


@router.post("/login", response_model = Token, status_code = status.HTTP_200_OK)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    #1. Buscamos username y password en la petición HTTP
    # OAuth2PasswordRequestForm always has 'username' field, even if we use email
    username: str | None = form_data.username 
    password: str | None = form_data.password

    if username is None or password is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = "Email and/or password incorrect"
        )

    #2. Buscamos username en la bbdd
    user: UserDb = get_user_by_email(username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Email and/or password incorrect'
        )
    
    #3. Checkeamos contraseñas
    if not verify_password(password, user.password):
         raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Email and/or password incorrect'
        )
    
    token = create_access_token(
        UserBase(
            name=user.name,
            email=user.email,
            role=user.role,
            location=user.location
            )
        )
    
    return token

@router.get(
    "/me",
    response_model=UserOut,
    status_code=status.HTTP_200_OK
)
async def get_me(token: str = Depends(oauth2_scheme)):
    data: TokenData = decode_token(token)
    
    user = get_user_by_email(data.username) # data.username actually holds email
    if not user:
         raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    return user

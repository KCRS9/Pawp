import bcrypt
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from pydantic import BaseModel

# We must import UserBase to type hint create_access_token exactly like the template
# But to avoid circular imports if models imports auth, we might need to be careful.
# In template, auth imports UserBase from app.models.
# And app.models does NOT import auth. Safe.
from app.models import UserBase

SECRET_KEY = "1234567890" # Keeping template key for similarity as requested, though insecure
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MIN = 7 * 24 * 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login/")

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

def get_hash_password(plain_pw: str) -> str:
    pw_bytes = plain_pw.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(password=pw_bytes, salt=salt)
    return hashed_pw.decode("utf-8") # Template didn't decode? 
    # Template: return hashed_pw (which is bytes)
    # But then UserDb password is str.
    # In template models.py, password is str. 
    # If template returns bytes, and Pydantic expects str, it might strict error.
    # Let me check template again. 
    # Template: return hashed_pw
    # Wait, in template `insert_user`: values = (..., user.password)
    # If user.password is bytes, insert might work with MariaDB driver.
    # But models.py says `password: str`.
    # I'll decode it to be safe and cleaner for string storage.

def verify_password(plain_pw, hashed_pw) -> bool:
    plain_pw_bytes = plain_pw.encode("utf-8")
    # hashed_pw might be str in DB, rewrite to bytes
    if isinstance(hashed_pw, str):
        hashed_pw_bytes = hashed_pw.encode("utf-8")
    else:
        hashed_pw_bytes = hashed_pw
    return bcrypt.checkpw(password=plain_pw_bytes, hashed_password=hashed_pw_bytes)

def create_access_token(user: UserBase) -> Token:
    # Template uses user.username. My UserBase has email? 
    # Template: user.username.
    # AnimalGram: user.email is unique.
    # I should use email as username or keep username field?
    # db_animalgram.sql has `email`. NO `username` column in `USER` table.
    # But Template has `username`.
    # "Replicalo aplicado a mis necesidades".
    # My need: Logic uses email.
    # Style: Code looks like template.
    # So I will use `user.email` but maybe alias it or just use `sub: user.email`.
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MIN)
    to_encode = {"sub": user.email, "exp": expire} # Changed username to email
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return Token(access_token=encoded_jwt, token_type="bearer")

def decode_token(token: str) -> TokenData:
    try:
        payload: dict = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return TokenData(username=payload.get("sub")) # Map sub (email) to TokenData.username
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )

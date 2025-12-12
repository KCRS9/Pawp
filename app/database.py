import mariadb
import os
from app.models import UserDb, AnimalDb, ShelterDb, ShelterOut, AnimalOut
from typing import List, Optional

db_config = {
    "host": "animalgram_db",
    "port": 3306,
    "user": "animalgram",
    "password": "animalgram",
    "database": "animal_shelter_db"
}

# --- USERS ---

def insert_user(user: UserDb) -> int:
    with mariadb.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            sql = "INSERT INTO user (name, email, password, role, location) VALUES (%s, %s, %s, %s, %s)"
            values = (user.name, user.email, user.password, user.role, user.location)
            cursor.execute(sql, values)
            conn.commit()
            return cursor.lastrowid

def get_user_by_email(email: str) -> UserDb | None:
    with mariadb.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            sql = "SELECT id, name, email, password, role, location FROM user WHERE email = %s"
            cursor.execute(sql, (email,))
            result = cursor.fetchone()
            if result:
                return UserDb(
                    id=result[0],
                    name=result[1],
                    email=result[2],
                    password=result[3],
                    role=result[4],
                    location=result[5]
                )
            return None




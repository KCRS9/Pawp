import mariadb
import os
from app.models import UserDb, AnimalDb, ShelterDb, ShelterOut, AnimalOut
from typing import List, Optional

# Config dictionary as requested
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
            # Note: Table name 'user' 
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

def get_all_users() -> List[UserDb]:
    with mariadb.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            sql = "SELECT id, name, email, password, role, location FROM user"
            cursor.execute(sql)
            results = cursor.fetchall()
            users = []
            for row in results:
                users.append(UserDb(
                    id=row[0],
                    name=row[1],
                    email=row[2],
                    password=row[3],
                    role=row[4],
                    location=row[5]
                ))
            return users

# --- ANIMALS ---

def get_all_animals(skip: int = 0, limit: int = 100) -> List[AnimalDb]:
    with mariadb.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            sql = "SELECT id, name, species, breed, age, size, description, status, health, shelter FROM animal LIMIT %s OFFSET %s"
            cursor.execute(sql, (limit, skip))
            results = cursor.fetchall()
            animals = []
            for row in results:
                animals.append(AnimalDb(
                    id=row[0],
                    name=row[1],
                    species=row[2],
                    breed=row[3],
                    age=row[4],
                    size=row[5],
                    description=row[6],
                    status=row[7],
                    health=row[8],
                    shelter=row[9]
                ))
            return animals

def insert_animal(animal: AnimalDb) -> int:
    with mariadb.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            sql = """INSERT INTO animal 
                     (name, species, breed, age, size, description, status, health, shelter) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (
                animal.name, animal.species, animal.breed, animal.age, animal.size, 
                animal.description, animal.status, animal.health, animal.shelter
            )
            cursor.execute(sql, values)
            conn.commit()
            return cursor.lastrowid

def get_animal_by_id(id: int) -> AnimalDb | None:
    with mariadb.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            sql = "SELECT id, name, species, breed, age, size, description, status, health, shelter FROM animal WHERE id = %s"
            cursor.execute(sql, (id,))
            result = cursor.fetchone()
            if result:
                return AnimalDb(
                    id=result[0],
                    name=result[1],
                    species=result[2],
                    breed=result[3],
                    age=result[4],
                    size=result[5],
                    description=result[6],
                    status=result[7],
                    health=result[8],
                    shelter=result[9]
                )
            return None

# --- SHELTERS ---

def get_all_shelters(skip: int = 0, limit: int = 100) -> List[ShelterDb]:
    with mariadb.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            sql = "SELECT id, name, address, contact, website, description, admin FROM shelter LIMIT %s OFFSET %s"
            cursor.execute(sql, (limit, skip))
            results = cursor.fetchall()
            shelters = []
            for row in results:
                shelters.append(ShelterDb(
                    id=row[0],
                    name=row[1],
                    address=row[2],
                    contact=row[3],
                    website=row[4],
                    description=row[5],
                    admin=row[6]
                ))
            return shelters

def insert_shelter(shelter: ShelterDb) -> int:
    with mariadb.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            sql = """INSERT INTO shelter 
                     (name, address, contact, website, description, admin) 
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            values = (
                shelter.name, shelter.address, shelter.contact, 
                shelter.website, shelter.description, shelter.admin
            )
            cursor.execute(sql, values)
            conn.commit()
            return cursor.lastrowid

def get_shelter_by_id(id: int) -> ShelterDb | None:
    with mariadb.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            sql = "SELECT id, name, address, contact, website, description, admin FROM shelter WHERE id = %s"
            cursor.execute(sql, (id,))
            result = cursor.fetchone()
            if result:
                return ShelterDb(
                    id=result[0],
                    name=result[1],
                    address=result[2],
                    contact=result[3],
                    website=result[4],
                    description=result[5],
                    admin=result[6]
                )
            return None

def create_db_and_tables():
    pass

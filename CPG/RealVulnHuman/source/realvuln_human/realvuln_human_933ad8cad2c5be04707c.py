import binascii
import datetime

import pytz
from Crypto import Random
from django.core.management.base import BaseCommand

from app.models import User, PaidTimeOff, Retirement, Schedule, KeyManagement, WorkInfo, Performance, Message

users = [
    {
        "id": 1,
        "user_id": 1,
        "email": "admin@metacorp.com",
        "is_admin": True,
        "password": "admin1234",
        "first_name": "Admin",
        "last_name": "",
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "id": 2,
        "user_id": 2,
        "email": "jack@metacorp.com",
        "is_admin": False,
        "password": "yankeessuck",
        "first_name": "Jack",
        "last_name": "Mannino",
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "id": 3,
        "user_id": 3,
        "email": "jim@metacorp.com",
        "is_admin": False,
        "password": "alohaowasp",
        "first_name": "Jim",
        "last_name": "Manico",
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "id": 4, 
        "user_id": 4, 
        "email": "mike@metacorp.com",
        "is_admin": False,
        "password": "motocross1445",
        "first_name": "Mike",
        "last_name": "McCabe",
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "id": 5,
        "user_id": 5,
        "email": "ken@metacorp.com",
        "is_admin": False,
        "password": "citrusblend",
        "first_name": "Ken",
        "last_name": "Johnson",
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    }
]

retirements = [
    {
        "user_id": 2,
        "employee_contrib": "1000",
        "employer_contrib": "2000",
        "total": "4500",
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())

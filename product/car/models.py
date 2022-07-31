import string
from unicodedata import name
from django.db import models

# Create your models here.

class Specification:
    id: int
    name: string
    images2: string
    desc: string
    price: float

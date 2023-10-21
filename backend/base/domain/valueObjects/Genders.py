from django.db import models

class Genders( models.TextChoices ):
    M = 'Male',
    F = 'Female',
    X = 'Non-binary',

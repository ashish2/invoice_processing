from django.db import models

# Create your models here.
from basemodel.models import BaseModel
class Customer(BaseModel):
	name
	email
	user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

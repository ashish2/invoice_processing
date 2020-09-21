from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from basemodel.models import BaseModel

class Customer(BaseModel):
	name = models.CharField(max_length=256)
	email = models.CharField(max_length=256)
	user = models.OneToOneField(User, on_delete=models.CASCADE)


from django.db import models

# Create your models here.

class BaseModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)
	is_deleted = models.BooleanField(default=False) # status values: 1-Deleted, 0-Not Deleted
	class Meta:
		abstract = True
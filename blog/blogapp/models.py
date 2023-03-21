from django.db import models
from authentication.models import User
from helpers.models import TrackingModel

class Blog(TrackingModel):
    title = models.CharField(max_length=255)
    body = models.TextField()
    is_active = models.BooleanField(default=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

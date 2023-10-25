from django.db import models
from authentication.models import User
from helpers.models import TrackingModel
from markdownx.models import MarkdownxField
#from martor.models import MartorField

class Blog(TrackingModel):
    title = models.CharField(max_length=255)
    body = MarkdownxField() #MartorField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

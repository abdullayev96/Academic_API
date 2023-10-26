from django.db import models
from baseapp.models import BaseModel



class Message(BaseModel):
     name = models.CharField(max_length=300, verbose_name="Elon nomi")
     body  = models.TextField(verbose_name="Text haqida")
     image = models.ImageField(upload_to="mes/")


     def __str__(self):
          return self.name


     class Meta:
          verbose_name = "E'lonlar"




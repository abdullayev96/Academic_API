from django.db import models
from baseapp.models import BaseModel


class Images(models.Model):
     img = models.ImageField(upload_to="images/")

     class Meta:
          verbose_name = "Rasm"




class News(BaseModel):
     name = models.CharField(max_length=40, verbose_name="Yangilik nomi")
     title = models.TextField(verbose_name="yanlik haqida")
     images = models.ManyToManyField(Images, related_name="img", blank=True)


     def __str__(self):
         return self.name


     class Meta:
          verbose_name = "Yangilik"




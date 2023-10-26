from django.db import models
from baseapp.models import BaseModel



class Images(BaseModel):
     image = models.ImageField(upload_to="new/")

     class Meta:
          verbose_name = "Rasmlar"




class Users(models.Model):
      teacher = models.CharField(max_length=300, verbose_name="O'qituvchilar soni")
      student  = models.CharField(max_length=200, verbose_name="O'quvchilar soni")
      otm = models.CharField(max_length=40, verbose_name="OTM ga kirish ko'rsatkichi")
      acceptance  = models.CharField(max_length=40, verbose_name="Qabulga kelib tushgan arizalar soni")


      def __str__(self):
          return self.full_name


      class Meta:
          verbose_name = "O'zgartirish"


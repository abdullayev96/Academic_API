from django.db import models
from baseapp.models import BaseModel



class Chair(BaseModel):
      chair_name=models.CharField(max_length=200, verbose_name="Kafedra nomi")
      chair_full = models.CharField(max_length=100, verbose_name="Kafedra mudiri ismi")
      chair_result = models.CharField(max_length=100, verbose_name="Lavozimi")
      image = models.ImageField(upload_to='img/')
      title = models.TextField(verbose_name="Kafedra haqida")

      def __str__(self):
          return self.chair_name


      class Meta:
          verbose_name = "Kafedra"




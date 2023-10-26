from django.db import models
from baseapp.models import BaseModel


class Leader(BaseModel):
      full_name = models.CharField(max_length=300, verbose_name="Toliq ism va Familiya")
      position  = models.CharField(max_length=200, verbose_name="Lavozimi")
      image = models.ImageField(upload_to='img/')
      email  = models.EmailField(verbose_name="Email")
      number = models.CharField(max_length=40, verbose_name="Tel nomire")
      phone  = models.CharField(max_length=40, verbose_name="Tel nomire")
      rest   = models.CharField(max_length=50, verbose_name="Bosh vaqti")


      def __str__(self):
          return self.full_name


      class Meta:
          verbose_name = "Rahbar"


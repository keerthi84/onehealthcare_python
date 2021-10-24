from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from datetime import date
# Create your models here.
class Deparment(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.CharField(max_length=250, unique=True)
    img=models.ImageField(upload_to='image')
    desc=models.TextField()

    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='departments'

    def get_url(self):
        return reverse('dp_dc',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Doctor(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.CharField(max_length=250,unique=True)
    desig=models.CharField(max_length=250)
    img=models.ImageField(upload_to='image')
    dept=models.ForeignKey(Deparment,on_delete=models.CASCADE)

    def get_url(self):
        return reverse('dcdetails',args=[self.dept.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Appointments(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(choices=(('male', 'Male'), ('female', 'Female')), max_length=10, default=None)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    def get_absolute_url(self):
        return reverse('h')
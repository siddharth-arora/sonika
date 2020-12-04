from django.db import models
# import reverse
from django.urls import reverse

# Create your models here.
class school(models.Model):
    name = models.CharField(max_length=200)
    principal = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        #here, we need to define which url will the control go to once the submit button has been clicked
        # return reverse('name_of_url)
        return reverse('list')

class students(models.Model):
    name = models.CharField(max_length=200)
    clas = models.CharField(max_length=200, null=True)
    school = models.ForeignKey(school, related_name="students",on_delete=models.CASCADE, null=True)

    def __str__ (self):
        return self.name

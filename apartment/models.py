from django.db import models

# Create your models here.


class Apartment(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=10, blank=True)
    description = models.TextField()
    location = models.CharField(max_length=100)
    size = models.CharField(max_length=25, blank=True)
    num_of_beds = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return u"{} at {}".format(self.title, self.location)


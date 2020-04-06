from django.db import models

# Create your models here.

STF_GENDER = (('M', 'MALE'),
              ('F', 'FEMALE'),)


class StaffRegistration(models.Model):
    staffid = models.CharField(max_length=20, unique=True)
    staffname = models.CharField(max_length=30)
    staffgender = models.CharField(choices=STF_GENDER, max_length=1)
    staffposition = models.CharField(max_length=30)
    staffImage = models.ImageField(upload_to='static/images')

    def __str__(self):
        return self.staffname

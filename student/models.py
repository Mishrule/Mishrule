from django.db import models

# Create your models here.
S_GENDER = (('M', 'MALE'),
            ('F', 'FEMALE'),)

S_FORMS = (('form1', 'FORM ONE'),
           ('form2', 'FORM TWO'),
           ('form3', 'FORM THREE'),)


class StudentRegistration(models.Model):
    studentid = models.CharField(max_length=20, unique=True)
    studentname = models.CharField(max_length=30)
    studentgender = models.CharField(choices=S_GENDER, max_length=1)
    studentform = models.CharField(choices=S_FORMS, max_length=5)
    studentImage = models.ImageField(upload_to='static/images')
    parentName = models.CharField(max_length=30)
    parentContact = models.CharField(max_length=30)
    parentLocation = models.CharField(max_length=30)
    registrationDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.studentname

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
special=[
        ("GENERAL MEDICINE", 'general medicine'),
        ("CARDIOLOGIST" , 'cardiologist'),
        ("ORTHOPEDIC" , 'orthopedic'),
        ("DENTIST", 'dentist'),
        ("NEUROLOGIST", 'neurologist'),
        ("OTHERS", 'others')       # list of data for drop down menu 
    ]
class ALLDOCTORS(models.Model):

    name = models.CharField(max_length=100)
    specialisation=models.CharField(choices=special)  # drop down menu
    yoe=models.IntegerField()
    license_no=models.IntegerField()
    age=models.PositiveIntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    certificate=models.ImageField(upload_to='certificates/',blank=True,null=True)

    def __str__(self):
        return self.name
    
class TREATMENT_DETAILS (models.Model):
    treatment_name=models.CharField(max_length=200)
    category=models.CharField(choices=special)
    doctor_name= models.ForeignKey(ALLDOCTORS, on_delete=models.CASCADE)
    description=models.TextField()
    dos = models.TextField(help_text="What to do")
    donts = models.TextField(help_text="What to avoid")

    def __str__(self):
        return self.treatment_name

class Appointment(models.Model):
    TIME_SLOTS = [
        ('morning', '09:00 AM - 12:00 PM'),
        ('afternoon', '01:00 PM - 04:00 PM'),
        ('evening', '05:00 PM - 08:00 PM'),
    ]
    doctorname= models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    date=models.DateField()
    time = models.CharField(max_length=20, choices=TIME_SLOTS)
    consultation_charges= models.CharField(max_length=100,default=550)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments', null=True, blank=True)

    def __str__(self):
        return f"{self.doctorname} - {self.date}"





# hide phone number while displaying.
#treatment name, category, respective doctor name, and small description of the treatment, including the do's and don't.


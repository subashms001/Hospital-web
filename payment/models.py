from django.db import models
from doctors.models import ALLDOCTORS,TREATMENT_DETAILS
from django.contrib.auth.models import User
from django.utils.timezone import now

room_type=[

        ("COMMON WARD" , 'Common ward'),
        ("SEMI PRIVATE" , 'Semi private'),
        ("PRIVATE AC" , 'Private AC'),
        ("PRIVATE NON AC", 'Private non AC'),
        ("DELUX", 'Delux'),    
    ]


class DischargeSummary(models.Model):
    patient_name = models.ForeignKey(User,on_delete=models.CASCADE)
    doctor_name= models.ForeignKey(ALLDOCTORS,on_delete=models.CASCADE)
    treatment_name = models.ForeignKey(TREATMENT_DETAILS,on_delete=models.CASCADE)
    description = models.TextField(max_length=400)
    date_of_admit = models.DateField()
    date_of_discharge = models.DateField(auto_now_add=True)
    room_type = models.CharField(max_length=100,choices=room_type)
    food_required = models.BooleanField(default=False)
    total_days = models.IntegerField(blank=True,null=True)


    def save(self, *args, **kwargs):
        self.date_of_discharge = now().date()

        if self.date_of_admit:
            self.total_days = (self.date_of_discharge - self.date_of_admit).days

        super().save(*args, **kwargs)


from django.db import models
from django.contrib.auth.models import User
from doctors.models import ALLDOCTORS
from django.contrib.auth.models import User

all_lab_tests = [
    ('CBC', 'Complete Blood Count'),
    ('LFT', 'Liver Function Test'),
    ('URINE TOTAL TEST', 'Urine Total Test'),
    ('URINE MICROSCOPIC', 'Urine Microscopic Examination'),
    ('SERUM ROUTINE', 'Serum Routine Test'),
    ('THYROID', 'Thyroid Function Test')
]

test_result =[
    ('pending','pending'),
    ('ongoing','ongoing'),
    ('completed','completed')
]
test_range =[
    ('Nill','Nill'),
    ('positive','positive'),
    ('negative','negative'),
    ('normal','normal'),
    ('abnormal','abnormal')
]
class Lab_tech(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    emp_id = models.IntegerField()
    qualification = models.CharField(max_length=100)
    year_of_exp = models.IntegerField()
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username


class Lab_Tests(models.Model):
    reffered_by = models.ForeignKey(ALLDOCTORS,on_delete=models.CASCADE)
    patient_name = models.ForeignKey(User,on_delete=models.CASCADE)
    lab_test = models.CharField(max_length=100,choices=all_lab_tests)
    lab_result = models.CharField(max_length=100,choices=test_result,default='ongoing')
    created_at = models.DateTimeField(auto_now_add=True)
    result_range = models.CharField(max_length=100,choices=test_range,default='Nill')
    result_desc = models.TextField(max_length=400)
    test_cost = models.IntegerField()
    def __str__(self):
        return self.lab_test


















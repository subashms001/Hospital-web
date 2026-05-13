from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from labreports.models import Lab_tech,Lab_Tests


class LabtechRegisterationForm(UserCreationForm):
    emp_id = forms.IntegerField()
    qualification = forms.CharField(max_length=100)
    year_of_exp = forms.IntegerField()
    address = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def save(self):
        user = super().save(commit=False)
        user.save()

        emp_id = self.cleaned_data['emp_id']
        qualification = self.cleaned_data['qualification']
        year_of_exp = self.cleaned_data['year_of_exp']
        address = self.cleaned_data['address']

        Lab_tech.objects.create(
            user=user,
            emp_id=emp_id,
            qualification=qualification,
            year_of_exp=year_of_exp,
            address=address
        )

        return user
    

class AddLabTestsForm(forms.ModelForm):
    class Meta:
        model = Lab_Tests
        fields = "__all__"
    

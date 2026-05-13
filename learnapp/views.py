from django.shortcuts import render
from learnapp.forms import UserForm , UserProfileForm , UserUpdateForm , UserProfileUpdateForm
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from doctors.models import Appointment
from learnapp.models import UserDetails
from labreports.forms import Lab_tech,LabtechRegisterationForm

# Create your views here.
def registration(request):
    registered= False
    if request.method=='POST':  
        form1=UserForm(request.POST)
        form2=UserProfileForm(request.POST,request.FILES)  
        if form1.is_valid() and form2.is_valid():
            user=form1.save() 
            user.set_password(user.password)   
            user.save()     
           
            profile=form2.save(commit=False) 
            profile.user = user
            profile.save() 
            registered =True 


    else:
        form1=UserForm()
        form2=UserProfileForm()
    context={
            'form1':form1,
            'form2':form2,
            'registered': registered
        }
    return render(request,"registration.html",context)



def user_login(request): 
    if request.method== 'POST':  
        username=request.POST['username']  
        password=request.POST['password']
        user = authenticate(username=username, password=password) 

        if user:
            if user.is_active:
                login(request,user) 
                return redirect("home") 
            else:
                return HttpResponse("user not active...... ")        
        else:
            return HttpResponse("please check your credentials........ ")
       
    return render(request, "login.html",{})




@login_required(login_url="login")  
def home(request):
    role = None
    labtech = None
    if request.user.is_authenticated:
        if Lab_tech.objects.filter(user=request.user).exists():            
            role = 'labtech'
            labtech = Lab_tech.objects.get(user=request.user)
        else:
            role = 'user'


    return render(request, "home.html",{'role':role,'labtech':labtech})



@login_required(login_url="login")
def profile(request):

    user_appointments = Appointment.objects.filter(user=request.user).order_by('date')
    
    context = {
        'appointments': user_appointments,
    }
    return render(request, 'profile.html', context)
    


@login_required(login_url="login")
def user_logout(request):
    logout(request)
    return redirect("login")



@login_required(login_url="login")
def update(request):
    user = request.user
    user_details, created = UserDetails.objects.get_or_create(user=user)

    if request.method == 'POST':
        form1 = UserUpdateForm(request.POST, instance=user)
        form2 = UserProfileUpdateForm(request.POST, request.FILES, instance=user_details)

        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            profile = form2.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('profile')

    else:
        form1 = UserUpdateForm(instance=user)
        form2 = UserProfileUpdateForm(instance=user_details)

    return render(request, "update.html", {
        'form1': form1,
        'form2': form2,
    })
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Member
from .models import Emp



# Create your views here.
def index(request):
    return render(request,'index.html')

def reg_member(request):                       # create a member
    if request.method == "POST":
        member=Member()
        member.FirstName = request.POST.get('firstname')
        member.SecondName = request.POST.get('secondname')
        member.Surname = request.POST.get('surname')
        member.Contact = request.POST.get('phonenumber')
        member.Gender = request.POST.get('gender')
        member.NextofkinName = request.POST.get('nextofkin')
        member.NextofkinContact = request.POST.get('nextofkinph')
        member.Age = request.POST.get('age')
        member.Address = request.POST.get('address')
        member.District = request.POST['district']
        member.save()
        return render(request,'form_elements.html') 
    else:
        return render(request,'form_elements.html')

       
def view_members(request): # retrive members 
    members = Member.objects.all()
    context = {'members':members}
    
    return render(request,"tbl_bootstrap.html",context)

def deleteMember(request,pk):
    members = Member.objects.get(pk=id)
    members.delete()
    messages.success(request, "Member Deleted Successfully")
    return redirect(request, "tbl_bootstrap.html")
    
    
    


def signup(request):
    return render(request, 'auth-signup.html')

def signin(request):
    return render(request, 'auth-signin.html')

def resetpassword(request):
    return render(request,'auth-reset-password.html')

# testtview
def createView(request):
    return render(request,'testt.html')

#function storing 
def store(request):
    emp = Emp()
    emp.emp_name = request.POST.get('emp_name')
    emp.emp_email = request.POST.get('emp_email')
    emp.emp_mobile = request.POST.get('emp_mobile')
    emp.save()
    messages.success(request, "Employee Added Successfully")
    return redirect('/create')
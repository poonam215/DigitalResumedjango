from django.shortcuts import render

# Create your views here.
def home(request):
    contaxt={'home':'active'}
    return render(request,'myapp/home.html',contaxt)

def contact(request):
    conta={'contact':'active'}
    return render(request,'myapp/contact.html',conta)

def skill(request):
    skil={'skill':'active'}
    return render(request,'myapp/skill.html',skil)

def education(request):
    edu={'education':'active'}
    return render(request,'myapp/education.html',edu)





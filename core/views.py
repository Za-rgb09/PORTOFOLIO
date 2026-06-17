from django.shortcuts import render, redirect
from .models import *

def home(request):
    context = {
        'hero': Hero.objects.first(),
        'skills': Skill.objects.all(),
    }
    return render(request, 'core/index.html', context)


def about(request):
    hero = Hero.objects.first()

    context = {
        'hero': hero
    }

    return render(request, 'core/about.html', context)


def projects(request):
    context = {
        'projects': Project.objects.all()
    }

    return render(request, 'core/projects.html', context)


def certificates(request):
    context = {
        'certificates': Certificate.objects.all()
    }

    return render(request, 'core/certificates.html', context)


def contact(request):

    if request.method == "POST":

        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject='Portfolio Contact',
            message=request.POST.get('message')
        )

        return redirect('contact')

    return render(request, 'core/contact.html')

def skills(request):
    context = {
        'skills': Skill.objects.all()
    }

    return render(
        request,
        'core/skills.html',
        context
    )
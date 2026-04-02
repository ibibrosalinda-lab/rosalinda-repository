from django.shortcuts import render
from .models import HeroSection, Goal, SkillCategory, Project, Education, ContactInfo


def home(request):
    hero = HeroSection.objects.first()
    goals = Goal.objects.all()
    context = {'hero': hero, 'goals': goals}
    return render(request, 'home.html', context)


def about(request):
    hero = HeroSection.objects.first()
    goals = Goal.objects.all()
    return render(request, 'about.html', {'hero': hero, 'goals': goals})


def skills(request):
    categories = SkillCategory.objects.prefetch_related('skills').all()
    return render(request, 'skills.html', {'categories': categories})


def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})


def education(request):
    educations = Education.objects.all()
    return render(request, 'education.html', {'educations': educations})


def contact(request):
    contact_info = ContactInfo.objects.first()
    return render(request, 'contact.html', {'contact_info': contact_info})

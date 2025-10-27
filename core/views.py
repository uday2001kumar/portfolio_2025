# core/views.py
from django.shortcuts import render
from .models import Education, Skill, Project, Experience,Profile,Certification

def portfolio_view(request):
    profile = Profile.objects.first() 
    
    # Check if a profile exists to prevent errors
    if not profile:
        profile = {
            'name': '[Your Name]',
            'title': '[Your Title]',
            'photo': None,
        }
    context = {
        'profile': profile,
        'education_list': Education.objects.order_by('-start_date'),
        'skill_list': Skill.objects.all().order_by('id'),
        'certification_list':Certification.objects.all().order_by('-id'),
        'project_list': Project.objects.order_by('id'), # Newest first
        'experience_list': Experience.objects.order_by('-start_date'),

        # Static content for About/Contact (can be defined here or in settings)
        'about_me_text': "I am a passionate developer with a knack for building dynamic web applications using Python and Django. I enjoy solving complex problems and learning new technologies.",
        'contact_info': {
            'email': 'your.email@gmail.com',
            'whatsapp': '1234567890', # Replace with your number
            'linkedin_url': 'https://www.linkedin.com/in/yourprofile',
            'instagram_url': 'https://www.instagram.com/yourprofile',
        }
    }
    return render(request, 'portfolio.html', context)
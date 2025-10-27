# core/admin.py
from django.contrib import admin
from .models import Education, Skill, Project, Experience,Profile,Certification

admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Certification) 

from django.shortcuts import render
from .models import Experience, Education, Skill, Certification, Achievement

def home(request):
	experience = Experience.objects.all()
	education = Education.objects
	skills = Skill.objects
	certifications = Certification.objects
	achievements = Achievement.objects
	for exp in range(len(experience)):
		experience[exp].summary = experience[exp].summary.split("\n")
	return render(request, 'jobs/home.html', \
		{'experience': experience,\
		 'education': education,\
		 'skills': skills,\
		 'certifications': certifications,\
		 'achievements': achievements.all().order_by("-pk")})
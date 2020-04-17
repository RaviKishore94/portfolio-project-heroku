from django.contrib import admin
from .models import Experience, Education, Skill, Certification, Achievement

admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Certification)
admin.site.register(Achievement)
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import main,educations,skills,certifications,achievements,hobbies
# Register your models here.
admin.site.register(main)
admin.site.register(educations)
admin.site.register(skills)
admin.site.register(certifications)
admin.site.register(achievements)
admin.site.register(hobbies)

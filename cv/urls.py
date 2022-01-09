from django.urls import path
from cv import views

urlpatterns = [
   path('',views.index,name="index"),
   path('education/',views.education,name="education"),
   path('certification/',views.certification,name="certification"),
   path('skill/',views.skill,name="skill"),
   path('achievement/',views.achievement,name="achievement"),
   path('hobbie/',views.hobbie,name="hobbie")
]
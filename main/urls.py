from django.urls import path
from . import views

urlpatterns = [
    path('index', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('education/', views.education, name='education'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('resume/', views.resume_download, name='resume'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('achievements/', views.achievements, name='achievements'),
    path('certifications/', views.certifications, name='certifications'),
    path('experience/', views.experience, name='experience'),
    path('skills/', views.skills, name='skills'),
    path('blog/', views.blog, name='blog'),
    path('faq/', views.faq, name='faq'),
    path('hobbies/', views.hobbies, name='hobbies'), 
]

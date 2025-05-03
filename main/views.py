from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseRedirect
from django.contrib import messages
from urllib.parse import quote
from django.utils.http import urlencode
import requests
from django.core.mail import send_mail,BadHeaderError,EmailMessage

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        method = request.POST.get('method')
        message = request.POST.get('question')

        if method == "email":
            full_message = f"Name: {name}\nEmail: {email}\n\nQuestion:\n{message}"
            try :
                send_mail(
                    subject=subject,
                    message=full_message,
                    from_email=email,
                    recipient_list=['ydinu2854i@gmail.com'],
                    fail_silently=False,
                )
                messages.success(request, "✅ Your message was sent successfully!")
            except Exception as e:
                print("Email error:", e)
                messages.error(request, "❌ Something went wrong. Please try again.")
            return redirect('contact')

        elif method == "whatsapp":
            text = quote(f"Hi Dinu, I'm reaching out to connect with you through your portfolio. I have a query and would love to get in touch!:\n\n{message}\n\n- {name} ({email})")
            whatsapp_link = f"https://wa.me/+917995775924?text={text}"
            
            return HttpResponseRedirect(whatsapp_link)
             
    return render(request, 'contact.html')
def index (request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')

def skills(request):
    return render(request, 'skills.html')

def education(request):
    return render(request, 'education.html')

def experience(request):
    return render(request, 'experience.html')


def projects(request):
    # Project images stored in static/images
    projects = [
        { 'title': 'workforce', 'image': 'static/images/worker.jpg' },
        { 'title': 'helping-hands', 'image': 'static/images/Helping_Hands.png' },
        { 'title': 'ticket-exchange', 'image': 'static/images/tixexchange_logo.webp' },
        { 'title': 'portfolio', 'image': 'static/images/portfolio.jpg' },
    ]
    return render(request, 'projects.html', { 'projects': projects })

def resume_download(request):
    # Resume PDF stored in static/resume
    resume_url = 'static/resume/Dinesh_Resume.pdf'
    return render(request, 'resume.html', { 'resume_url': resume_url })


def certifications(request):
    return render(request, 'certifications.html')

def achievements(request):
    return render(request, 'achievements.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def blog(request):
    return render(request, 'blog.html')

def faq(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        method = request.POST.get('method')
        message = request.POST.get('question')

        if method == "email":
            full_message = f"Name: {name}\nEmail: {email}\n\nQuestion:\n{message}"
            try:
                send_mail(
                    subject="FAQ Submission from Portfolio",
                    message=full_message,
                    from_email=email,
                    recipient_list=['ydinu2854i@gmail.com'],
                    fail_silently=False,
                )
                messages.success(request, "✅ Your message was sent successfully!")
            except Exception as e:
                print("Email error:", e)
                messages.error(request, "❌ Something went wrong. Please try again.")
            return redirect('faq')

        elif method == "whatsapp":
            text = quote(f"Hi Dinu, I have a question from faq in your portfolio :\n\n{message}\n\n- {name} ({email})")
            whatsapp_link = f"https://wa.me/+917995775924?text={text}"
            return HttpResponseRedirect(whatsapp_link)

    return render(request, 'faq.html')

def hobbies(request):
    return render(request, 'hobbies.html')



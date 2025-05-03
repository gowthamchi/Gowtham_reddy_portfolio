
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),  # Including main app URLs
]

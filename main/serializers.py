from rest_framework import serializers
from .views import Portfolio, Project, Contact

class PortfolioSerializer(serializers.viewsSerializer):
    class Meta:
        views = Portfolio
        fields = '__all__'

class ProjectSerializer(serializers.viewsSerializer):
    class Meta:
        views = Project
        fields = '__all__'

class ContactMessageSerializer(serializers.viewsSerializer):
    class Meta:
        views = Contact
        fields = '__all__'

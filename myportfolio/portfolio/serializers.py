from rest_framework import serializers
from .models import Services, Projects, Packages, Reviews, FrontendTechnologies, BackendTechnologies


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class FrontendTechnologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontendTechnologies
        fields = '__all__'


class BackendTechnologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackendTechnologies
        fields = '__all__'


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class PackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

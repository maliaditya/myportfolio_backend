from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Services, Projects, Packages, Reviews ,FrontendTechnologies, BackendTechnologies
from .serializers import (ServicesSerializer, PackagesSerializer, ProjectsSerializer,
                          ReviewsSerializer , BackendTechnologiesSerializer, FrontendTechnologiesSerializer)


class ServicesList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class FrontendTechnologiesList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = FrontendTechnologies.objects.all()
    serializer_class = FrontendTechnologiesSerializer


class BackendTechnologiesList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = BackendTechnologies.objects.all()
    serializer_class = BackendTechnologiesSerializer


class ServicesDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ProjectsList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class ProjectsDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class PackagesList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Packages.objects.all()
    serializer_class = PackagesSerializer


class PackagesDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Packages.objects.all()
    serializer_class = PackagesSerializer


class ReviewsList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


class ReviewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

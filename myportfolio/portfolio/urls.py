from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (ServicesList, ServicesDetailView,
                    ProjectsList, ProjectsDetailView,
                    PackagesList, PackagesDetailView,
                    ReviewsList, ReviewsDetailView,
                    FrontendTechnologiesList, BackendTechnologiesList)

urlpatterns = [
    path('services/', ServicesList.as_view()),
    path('services/<int:pk>/', ServicesDetailView.as_view()),

    path('projects/', ProjectsList.as_view()),
    path('projects/<int:pk>/', ProjectsDetailView.as_view()),

    path('packages/', PackagesList.as_view()),
    path('packages/<int:pk>/', PackagesDetailView.as_view()),

    path('reviews/', ReviewsList.as_view()),
    path('reviews/<int:pk>/', ReviewsDetailView.as_view()),

    path('frontend/', FrontendTechnologiesList.as_view()),
    path('backend/', BackendTechnologiesList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)

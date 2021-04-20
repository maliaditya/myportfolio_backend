from django.contrib import admin
from .models import Services, Projects, Packages, Reviews, FrontendTechnologies, BackendTechnologies


# Register your models here.
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = 'service',


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = 'title',


@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    list_display = 'package',


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = 'f_name', 'l_name'


admin.site.register(FrontendTechnologies)
admin.site.register(BackendTechnologies)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from tracker.models import HealthData, CustomUser

# Customize the admin panel in article model
class ArticleAdmin(admin.ModelAdmin):
	list_display = ("first_name", "email", "is_staff", "is_active")

# Register your models here.
admin.site.register(CustomUser, ArticleAdmin)
admin.site.register(HealthData)
from django.urls import path
from tracker.views import HealthListView, HealthCreateView, HealthTemplateView, HealthUpdateView, HealthDeleteView, HealthProfileEdit

urlpatterns = [
	path("dashboard/", HealthListView.as_view(), name="dashboard"),
	path("register/", HealthCreateView.as_view(), name="register"),
	path("", HealthTemplateView.as_view(), name="home"),
	path("<int:pk>/update/", HealthUpdateView.as_view(), name="update_health_data"),
	path("<int:pk>/delete/", HealthDeleteView.as_view(), name="delete_health_data"),
	path("<int:pk>/update_profile/", HealthProfileEdit.as_view(), name="update_profile"),
]
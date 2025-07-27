from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from tracker.models import HealthData, CustomUser

# Create your views here.
class HealthTemplateView(TemplateView):
	template_name = "tracker/home.html"


class HealthListView(LoginRequiredMixin, ListView):
	model = HealthData
	template_name = "tracker/dashboard.html"
	context_object_name  = "trackers"

	# Get articles per User
	def get_queryset(self):
		return super().get_queryset().filter(creator=self.request.user).order_by('-date')


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		queryset = HealthData.objects.order_by('date')
		
		context['labels'] = [entry.date.strftime("%Y-%m-%y") for entry in queryset]
		context['exercise_data'] = [entry.exercise_minutes for entry in queryset]
		context['meditation_data'] = [entry.meditation_minutes for entry in queryset]
		context['sleep_data'] = [int(entry.sleep_hours) for entry in queryset]
		return context

class HealthCreateView(LoginRequiredMixin, CreateView):
	model = HealthData
	template_name = "tracker/create_healthtrack.html"
	fields = ["exercise_minutes", "meditation_minutes", "sleep_hours"]
	success_url = reverse_lazy("dashboard")

	def form_valid(self, form):
		if form.instance.sleep_hours > 24:
			form.add_error('sleep_hours', 'No puedes ingresar más de 24 horas.')
			return self.form_invalid(form)
		# Asign data to user
		form.instance.creator = self.request.user
		return super().form_valid(form)

class HealthUpdateView(LoginRequiredMixin, UpdateView):
	model = HealthData
	template_name = "tracker/update_healthtracker.html"
	fields = ["exercise_minutes",  "meditation_minutes", "sleep_hours"]
	success_url = reverse_lazy("dashboard")

class HealthDeleteView(LoginRequiredMixin, DeleteView):
	model = HealthData
	template_name = "tracker/delete_healthtrack.html"
	context_object_name = "track"
	success_url = reverse_lazy("dashboard")

class HealthProfileEdit(LoginRequiredMixin, UpdateView):
	model = CustomUser
	template_name = "tracker/profile_update.html"
	fields = ["first_name", "last_name", "email", "birth_date", "gender", "image"]
	success_url = reverse_lazy("dashboard")
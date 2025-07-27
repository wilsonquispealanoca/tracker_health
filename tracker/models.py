from django.db import models

from django.conf import settings

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
	image = models.ImageField(default="default.png")
	birth_date = models.DateField(null=True, blank=True)
	gender = models.CharField(
		max_length=10,
		choices=[("M", "Masculino"),("F", "Femenino"), ("O", "Otro")],
		null=True,
		blank=True
	)

	def __str__(self):
		return self.username

class HealthData(models.Model):
	date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")
	exercise_minutes = models.PositiveIntegerField(verbose_name="Ejercicio (min)", help_text="Minutos de ejercicio")
	meditation_minutes = models.PositiveIntegerField(verbose_name="Meditación (min)", help_text="Minutos de meditación")
	sleep_hours = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Horas de sueño", help_text="Horas dormidas (ej. 7.5)")

	creator = models.ForeignKey(
		settings.AUTH_USER_MODEL, 
		verbose_name = "Creador",	
		on_delete=models.CASCADE, 
		related_name="health_data"
	)

	def __str__(self):
		return f"{self.date.strftime('%Y-%m-%d')} - Ejercicio: {self.exercise_minutes} min"
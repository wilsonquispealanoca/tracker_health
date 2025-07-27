# signals.py
from allauth.socialaccount.signals import social_account_added, social_account_updated
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount
import urllib.request
from django.core.files.base import ContentFile

@receiver(social_account_added)
@receiver(social_account_updated)
def guardar_imagen_google(sender, request, sociallogin, **kwargs):
    user = sociallogin.user
    account = sociallogin.account  # instancia de SocialAccount

    # Obtener la URL de la imagen desde Google
    picture_url = account.extra_data.get("picture")

    if picture_url and not user.image:
        # Descargar la imagen
        try:
            result = urllib.request.urlopen(picture_url)
            image_data = result.read()
            # Guardar en el campo 'image'
            file_name = f"{user.username}_google.jpg"
            user.image.save(file_name, ContentFile(image_data))
            user.save()
        except Exception as e:
            print("Error al descargar imagen de Google:", e)

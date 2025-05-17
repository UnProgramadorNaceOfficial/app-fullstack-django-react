from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Reserva

@receiver(post_save, sender=Reserva)
def enviar_correo_reserva(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject='Confirmación de Reserva',
            message=f'Su reserva ha sido creada para el {instance.fecha} en el establecimiento {instance.establecimiento}.',
            from_email='django.apesta@gmail.com',
            recipient_list=[instance.email],
            fail_silently=False,
        )

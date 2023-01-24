from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Employer

@receiver(pre_save, sender=Employer) #pre_save - вызывается перед сохранением
def my_handler(sender, instance, **kwargs): #instance - передавать непосредственно объект Employer для взаимодействия с ним
    instance.changed_count += 1



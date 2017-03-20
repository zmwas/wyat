from actstream import action
from django.db.models.signals import post_save

from events.models import Event


def my_handler(sender,instance,created,**kwargs):
    action.send(instance,verb="added")


post_save.connect(my_handler,sender=Event)
from __future__ import unicode_literals

from django.apps import AppConfig


class EventsConfig(AppConfig):
    name = 'events'

    def ready(self):
        from actstream import registry
        registry.register(self.get_model('Event'))

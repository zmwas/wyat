from __future__ import unicode_literals

from django.apps import AppConfig


class GalleryConfig(AppConfig):
    name = 'gallery'


    def ready(self):
        from actstream import registry
        registry.register(self.get_model('Photo'),self.get_model('Album'))
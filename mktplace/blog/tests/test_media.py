from django.conf import settings
from django.conf.urls.static import static
from django.test import TestCase

from mktplace.urls import urlpatterns


class MediaTestUrl(TestCase):
    settings.DEBUG = True

    def setUp(self):
        self.urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    def test_debug(self):
        assert settings.DEBUG

    def test_media(self):
        assert self.urlpatterns

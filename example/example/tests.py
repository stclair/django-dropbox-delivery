from django import test

from django_dropbox_delivery.dropbox_delivery_client import DropboxDeliveryClient


class DropboxDeliveryClientTests(test.TestCase):

    def test_creates_dropbox_client_with_access_token_from_settings(self):
        sut = DropboxDeliveryClient()
        self.assertEqual("Django Delivery", sut.dropbox_client.account_info()['display_name'])

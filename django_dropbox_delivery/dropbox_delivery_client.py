from django.conf import settings
import dropbox


class DropboxDeliveryClient(object):

    def __init__(self):
        self.connect_dropbox_client()

    def connect_dropbox_client(self):
        self.dropbox_client = dropbox.client.DropboxClient(settings.DROPBOX_ACCESS_TOKEN)

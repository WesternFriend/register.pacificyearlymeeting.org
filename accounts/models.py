from authtools.models import AbstractEmailUser


class User(AbstractEmailUser):
    def get_username(self):
        return self.email

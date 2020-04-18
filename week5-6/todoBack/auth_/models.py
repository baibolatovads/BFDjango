from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
# Create your models here.


class MyUserManager(UserManager):
    def create_editor(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_editor', True)
        return self._create_user(username, email, password, **extra_fields)


class MyUser(AbstractUser):
    is_editor = models.BooleanField(False, default=False)

    objects = MyUserManager()

    def _try_create_profile_for_user(self, created):
        if created:
            Profile.objects.get_or_create(user=self)

    def save(self, *args, **kwargs):
        print('before saving')

        created = self.id is None

        self.username = 'demo_{}'.format(self.username)

        super(MyUser, self).save(*args, **kwargs)

        self._try_create_profile_for_user(created)

        print('after saving')


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.user.username







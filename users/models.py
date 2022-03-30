from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)),
                                                  null=True, blank=True)

    @property
    def is_activation_key_expired(self):
        try:
            if now() <= self.activation_key_expires:
                return False
        except Exception:
            pass
        return True

    def save_delete(self):
        self.is_active = False
        self.save()


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    )

    user = models.OneToOneField(User, null=False, db_index=True, on_delete=models.CASCADE)
    about = models.TextField(verbose_name='О себе', blank=True, null=True)
    gender = models.CharField(verbose_name='пол', choices=GENDER_CHOICES, blank=True, max_length=2)

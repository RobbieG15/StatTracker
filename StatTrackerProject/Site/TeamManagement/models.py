from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, firstName = "", lastName = "", password = None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            firstName = firstName,
            lastName = lastName,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, password=None):

        if password is None:
            raise TypeError("Password should not be none")

        user = self.create_user(email = email, password = password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name = 'email address',
        max_length = 255,
        unique = True
    )

    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    firstName = models.CharField(
        verbose_name = 'First Name',
        max_length = 255,
        null = True,
        blank = True,
    )

    lastName = models.CharField(
        verbose_name = 'Last Name',
        max_length = 255,
        null = True,
        blank = True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.firstName + ' ' + self.lastName

    def get_first_name(self):
        return self.firstName

    def get_email(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    objects = UserManager()
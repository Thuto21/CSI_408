from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import UserManager
from django.db import models


class Login(models.Model):
    staffid = models.IntegerField(unique=True)
    password = models.CharField(max_length=50, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'staffid'
    REQUIRED_FIELDS = ['password']

    objects = UserManager()

    def __str__(self):
        return self.staffid


class StaffManager(BaseUserManager):
    def create_user(self,staffid, password=None):
        if not staffid:
            raise ValueError('Users must have an staffid')

        user = self.model(
            staffid=self.normalize_staffid(staffid),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, staffid, password):
        user = self.create_user(
            staffid=self.normalize_staffid(staffid),
            password=password,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

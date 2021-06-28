from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

# =========================================== User ModelManager
class UserManager(BaseUserManager):
    """
    User model manager where mobile is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, mobile, password, **extra_fields):
        """
        Create and save a User with the given mobile and password.
        """
        user = self.model(mobile=mobile, **extra_fields)
        user.set_password(password)
        user.full_clean()
        user.save()
        return user

    def create_superuser(self, mobile, password, **extra_fields):
        """
        Create and save a SuperUser with the given mobile and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(mobile, password, **extra_fields)


# =========================================== User Model
class User(AbstractUser):
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    # Removed from base class
    first_name = None
    last_name = None
    username = None

    # required
    name = models.CharField(max_length=255, blank=True)
    mobile = models.IntegerField(unique=True)
    mail = models.EmailField(max_length=254, blank=True)

    # Settings
    USERNAME_FIELD = "mobile"
    REQUIRED_FIELDS = []

    # Model Managers
    objects = UserManager()


    def clean(self, *args, **kwargs):
        # custom validations here
        super().clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


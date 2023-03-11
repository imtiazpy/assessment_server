from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext as _

class CustomBaseUserManager(BaseUserManager):

    def create_user(self, email, name, type, password=None):
        """
        It creates a user with the given email, name, type, and password
        
        :param email: The email address of the user
        :param name: The name of the model
        :param type: This is the type of user. We'll use this to determine if the user is a student or a
        teacher
        :param password: The password for the user
        :return: The user object
        """
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, type=type)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, type, password=None):
        """
        It creates a user with the given email, name, type, and password, and then sets the user's
        is_admin, is_superuser, and is_staff attributes to True
        
        :param email: The email address of the user
        :param name: The name of the user
        :param type: This is the type of user. It can be either a student or a teacher
        :param password: The password for the user
        :return: The user object
        """
        user = self.create_user(email=email, name=name, type=type, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user
    

class CustomUser(AbstractBaseUser, PermissionsMixin):

    """
    This code defines a custom user model that extends AbstractBaseUser and PermissionsMixin. It has fields for type, avatar, email, name, is_active, and is_staff, and uses a custom manager CustomBaseUserManager. The type field has two choices, EMPLOYER and JOB_SEEKER, and is required along with the name field. The model also provides get_full_name() and __str__() methods for retrieving user information.
    """

    class Types(models.TextChoices):
        EMPLOYER = 'EMPLOYER', 'Employer'
        JOB_SEEKER = 'JOB_SEEKER', 'Job_Seeker'

    type = models.CharField(_('Type'), max_length=50, choices=Types.choices, null=True, blank=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(_('Name'), max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = CustomBaseUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'type']

    def get_full_name(self):
        return self.name

    def __str__(self):
        return f'{self.id}-{self.email}'
    

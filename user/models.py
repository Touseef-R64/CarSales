from django.db import models
import uuid
from user.utils import Util
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, email, name,contact ,address='',city='',profile_picture=None, password=None,):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            profile_picture=profile_picture,
            contact=contact,
            address=address,
            city=city
            )
     
        user.set_password(password)
        user.save(using=self._db)
       
        return user

    

    def create_superuser(self, email,contact, name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.model(
            email=email,
            contact=contact,
            name=name,
            
        )
        user.set_password(password)
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=20, unique=True,null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to=Util.custom_image_filename,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','contact']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the user have the specific permission?"
        return self.is_admin
    
    def has_module_perms(self, app_label):
        "Does the user have permission to view the app `app_label`? "
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin
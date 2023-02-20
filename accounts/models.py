from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinValueValidator
from multiselectfield import MultiSelectField
from django.urls import reverse

# Create your models here.
class MyAccountManager(BaseUserManager):  # normal user
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('the user need an email')
        if not username:
            raise ValueError('the user need a username')

        user = self.model(
            email=self.normalize_email(email),  # if you enter a capital letter it will make it smaller
            username=username,
            first_name=first_name,
            last_name=last_name,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # creating superuser
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

    # Account
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    username = models.CharField(max_length=70, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/accountenglish', blank=True,null=True)
    description = models.TextField(default=False)
    price_hour = models.IntegerField(default=5, validators=[MinValueValidator(5)])

    # Only can add number and alphabet to the short code
    # such as need make C++ to CPP
    LANGUAGE_CHOICE = (
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('Javascript', 'Javascript'),
        ('Css', 'Css'),
        ('Html', 'Html'),
        ('React', 'React'),
        ('C', 'C'),
    )
    languages_choice = models.SlugField(choices=LANGUAGE_CHOICE, default=False)
    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # login with the email
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):  # return the email
        return self.email

    def has_perm(self, perm, obj=None):  # is user is admin+all permissions
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

    def get_url(self):
        return reverse('accounts_by_category', args=[self.languages_choice])

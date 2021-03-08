from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class User(AbstractUser):
    """
        Extending User Model via AbstractUser then OneToOneField for each role
        Fields already on User :
            - username
            - first_name
            - last_name
            - email
            - password
            - groups
            - user_permissions
            - is_staff
            - is_active -> mettre un trigger sur cet attribut maide
            - is_superuser
            - last_login
            - date_joined
        Need to set AUTH_USER_MODEL = "user.User"
    """

    # Gender
    GENDER_CHOICES = (("F", "Femme"), ("M", "Male"))
    gender = models.CharField(
        default="M", max_length=1, choices=GENDER_CHOICES, verbose_name="gender"
    )
    age = models.IntegerField(blank=True, null=True)
    # Birthday
    birthday = models.DateField(blank=True, null=True, verbose_name="date of birth")

    # Mobile Phone
    phone_number = models.CharField(
        blank=True,
        max_length=13,
        verbose_name="phone number",
    )

    # Address definition
    address_part1 = models.CharField(blank=True, max_length=200, verbose_name="address")
    
    # Address second line
    address_part2 = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="complete address"
    )

    # Postal Code Regex
    pc_regex = RegexValidator(
        regex=r"^\d{5}$", message="Please use this format: 'XXXXX'."
    )

    # Postal code
    postal_code = models.IntegerField(blank=True, null=True, validators=[pc_regex])

    # City
    city = models.CharField(blank=True, max_length=30, verbose_name="city")

    # Country
    country = models.CharField(blank=True, max_length=30, verbose_name="country")

    email = models.EmailField(max_length=50)
    
    class Meta(object):
        unique_together = ("email",)


class Doctor(models.Model):
    """
        Here we define Doctor profile extending User Model
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="User",
        related_name="doctor",
    )
    #Qualification
    qualification = models.CharField(max_length=100, verbose_name="qualification")

    #Registration number
    registration_number = models.IntegerField(unique=True, verbose_name="registration number")

    # Date updated
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name="last modification date")

    class Meta:
        verbose_name = "doctor"
        verbose_name_plural = "doctors"

    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)


class Patient(models.Model):
    """
        Here we define Patient profile extending User Model
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="User",
        related_name="Patient",
    )
    # Date updated
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name="last modification date")
    # Date saved in the system
    date_created = models.DateTimeField(
        auto_now_add=True, auto_now=False, verbose_name="date added to the system"
    )
    date_of_consultant = models.DateField(null=True, blank=True, verbose_name="date when consult with doctor")

    class Meta:
        verbose_name = "patient"
        verbose_name_plural = "patients"

    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)
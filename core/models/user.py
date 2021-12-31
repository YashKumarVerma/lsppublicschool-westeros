# library imports
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.models import UserManager

# project imports 
from core.models.contact import Contact 
from core.validators import UsernameValidator
from westeros.settings.configuration import MAXIMUM_USERNAME_LENGTH, MINIMUM_USERNAME_LENGTH

"""
User Model

- used for authentication
- everyone is a user of the application, students, parents, teachers, etc.
"""
class User(AbstractBaseUser, PermissionsMixin):
    object = UserManager()

    """
    Basic profile details
    """
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    
    # username - required to log into application
    username = models.CharField(
        "username",
        max_length=150,
        unique=True,
        help_text=f"Required. min length: {MINIMUM_USERNAME_LENGTH}, max length: {MAXIMUM_USERNAME_LENGTH}",
        validators=[UsernameValidator()],
        error_messages={"unique": "A user with that username already exists."},
    )

    # primary contact number of user - used for OTP(if)
    primary_contact = models.OneToOneField(
        Contact, related_name="user", null=True, on_delete=models.CASCADE
    )

    """
    Genders Configurations
    """
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"
    NOT_SAY = "N"

    GENDERS = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other"),
        (NOT_SAY, "Rather not say"),
    )
    gender = models.CharField(
        max_length=1, blank=True, null=True, verbose_name="Gender", choices=GENDERS
    )

    """
    User Account Flag

    - quickly filter active and non-active users
    """
    is_active = models.BooleanField(
        verbose_name="Active",
        default=True,
        db_index=True,
        help_text="Designates whether this user should be treated as active. "
        "Unselect this instead of deleting accounts.",
    )


    is_staff = models.BooleanField(
        verbose_name="Staff Status",
        default=False,
        help_text="Designates whether the user can log into admin site.",
    )
    """
    Account Status : common operations that are possible for all users

    - keep them generic, valid for student, teacher, parent, etc.
    """
    STUDENT_PASSED_OUT = "001"
    STUDENT_TRANSFERRED_TO_ANOTHER_SCHOOL = "002"
    DEBARRED_FOR_MISCONDUCT = "003"
    DEBARRED_FOR_FEE_DUE = "004"
    DEBARRED_FOR_FRAUD = "005"
    INACTIVE_REASONS = (
        (STUDENT_PASSED_OUT, "Student passed out"),
        (STUDENT_TRANSFERRED_TO_ANOTHER_SCHOOL, "Student transferred to another school"),
        (DEBARRED_FOR_MISCONDUCT, "Debarred for misconduct"),
        (DEBARRED_FOR_FEE_DUE, "Debarred for fee due"),
        (DEBARRED_FOR_FRAUD, "Debarred for fraud"),
    )
    inactive_reason = models.CharField(
        choices=INACTIVE_REASONS, max_length=4, null=True, blank=True
    )


    USERNAME_FIELD = "username"

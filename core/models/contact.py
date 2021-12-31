
from common.models import CommonModel
from django.db import models
import uuid

"""
Contact Model

- all phone numbers in the application are stored in this model
"""
class Contact(CommonModel):
    UNVERIFIED = "unverified"
    OTP_SENT = "otp_sent"
    VERIFIED = "verified"
    BLOCKED = "blocked"

    STATUSES = [
        (UNVERIFIED, "Unverified"),
        (OTP_SENT, "OTP Sent"),
        (VERIFIED, "Verified"),
        (BLOCKED, "Blocked"),
    ]

    # phone number of the user
    phone_number = models.CharField(max_length=15, unique=True)
    
    # current status of account
    status = models.CharField(choices=STATUSES, default=UNVERIFIED, max_length=16)
    
    # unique id for external actions which cannot be predicted
    external_id = models.UUIDField(default=uuid.uuid4, unique=True)

    # change string representation of object to phone number
    def __str__(self):
        val = self.get_full_number()
        if hasattr(self, "user"):
            val += f" ({str(self.user)})"
        return val

    def get_full_number(self):
        return '+91' + self.phone_number

    # set descriptive model names 
    class Meta:
        verbose_name = "Contact Number"
        verbose_name_plural = "Contact Numbers"

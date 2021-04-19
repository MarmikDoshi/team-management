import uuid

from phonenumber_field.modelfields import PhoneNumberField

from django.db import models


class TeamMember(models.Model):
    """TeamMember represents the details of the member of a team."""

    ADMIN = 'AD'
    REGULAR = 'RE'
    TEAM_MEMBER_ROLES = (
        (ADMIN, 'Admin'),
        (REGULAR, 'Regular')
    )

    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField()
    role = models.CharField(max_length=2, choices=TEAM_MEMBER_ROLES, default=REGULAR)

    def __str__(self):
        return self.first_name

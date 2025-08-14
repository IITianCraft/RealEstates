from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("date_joined", timezone.now())
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, blank=True, null=True)
    user_type = models.CharField(max_length=20, default='normal')
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(blank=True)
    gender = models.CharField(
        max_length=10,
        blank=True,
        choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')]
    )
    birth_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email


PROPERTY_PURPOSE_CHOICES = [
    ('Buy', 'Buy'),
    ('Rent', 'Rent'),
]

FURNISHED_CHOICES = [
    ('Furnished', 'Furnished'),
    ('Unfurnished', 'Unfurnished'),
]

PROPERTY_TYPE_CHOICES = [
    ('Flat', 'Flat'),
    ('Villa', 'Villa'),
    ('Apartment', 'Apartment'),
]

PROPERTY_STATUS_CHOICES = [
    ('Active', 'Active'),
    ('Pending', 'Pending'),
    ('Inactive', 'Inactive'),
]


class Property(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=PROPERTY_PURPOSE_CHOICES)
    furnished = models.CharField(max_length=20, choices=FURNISHED_CHOICES)
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPE_CHOICES)
    bedrooms = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    bathrooms = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    area = models.PositiveIntegerField(help_text="Area in square feet", validators=[MinValueValidator(100)])
    description = models.TextField()
    contact_name = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=20)
    contact_email = models.EmailField()
    status = models.CharField(max_length=20, choices=PROPERTY_STATUS_CHOICES, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"Image for: {self.property.title}"


class SavedProperty(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="saved_properties")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="saved_by")
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "property")

    def __str__(self):
        return f"{self.user.email} saved {self.property.title}"


class MeetingRequest(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("completed", "Completed"),
        ("rejected", "Rejected"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="meeting_requests")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="meetings")
    proposed_time_slot = models.DateTimeField(
        help_text="The specific date and time proposed by the user for the meeting.",
        null=False, blank=False,
        default=timezone.now
    )
    meeting_purpose = models.TextField(
        help_text="The user's stated purpose for the meeting.",
        default="Not specified"
    )
    requested_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    class Meta:
        unique_together = ('user', 'property')

    def __str__(self):
        try:
            return f"{self.user.email} → {self.property.title} on {self.proposed_time_slot.strftime('%Y-%m-%d %H:%M')} ({self.status})"
        except Exception:
            return f"{self.user.email} → {self.property.title} ({self.status})"

    def clean(self):
        if self.user == self.property.user:
            raise ValidationError("You cannot create a meeting request for your own property.")


class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('meeting_request', 'Meeting Request'),
        ('meeting_response', 'Meeting Response'),
        ('announcement', 'Announcement'),
        ('booking_cancellation', 'Booking Cancellation'), # Added for clarity
        ('booking_update', 'Booking Update'), # Added for clarity
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications"
    )
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # Changed max_length from 20 to 50 to accommodate longer notification types
    notification_type = models.CharField(max_length=50, choices=NOTIFICATION_TYPES) 
    related_object_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"To: {self.user.email} | Type: {self.notification_type} | Message: {self.message[:40]}"


EVENT_PLACE_CATEGORY_CHOICES = [
    ('Indoor', 'Indoor'),
    ('Outdoor', 'Outdoor'),
    ('Rooftop', 'Rooftop'),
]

EVENT_PLACE_STATUS_CHOICES = [
    ('active', 'Active'),
    ('pending', 'Pending Review'),
    ('inactive', 'Inactive'),
]

class EventPlace(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='event_places')
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    capacity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Maximum number of guests this event place can accommodate."
    )
    category = models.CharField(max_length=20, choices=EVENT_PLACE_CATEGORY_CHOICES)
    is_available_now = models.BooleanField(default=True)
    contact_name = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=20)
    contact_email = models.EmailField()
    status = models.CharField(
        max_length=20,
        choices=EVENT_PLACE_STATUS_CHOICES,
        default='pending',
        help_text="Current status of the event place listing (e.g., active, pending review, inactive)."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class EventPlaceImage(models.Model):
    event_place = models.ForeignKey(EventPlace, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='event_place_images/')

    def __str__(self):
        return f"Image for: {self.event_place.name}"

class EventBooking(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
        ("completed", "Completed"),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="event_bookings")
    event_place = models.ForeignKey(EventPlace, on_delete=models.CASCADE, related_name="bookings")
    booking_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    number_of_guests = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    event_type = models.CharField(max_length=100)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="confirmed")
    booked_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError("End time must be after start time.")
        if self.number_of_guests > self.event_place.capacity:
            raise ValidationError(
                f"Number of guests ({self.number_of_guests}) exceeds the event place capacity ({self.event_place.capacity})."
            )

    def __str__(self):
        return f"Booking for {self.event_place.name} by {self.user.email} on {self.booking_date} ({self.status})"

    class Meta:
        pass
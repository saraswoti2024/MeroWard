from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    message = models.TextField()

class AppointmentForm(models.Model):
    REQUEST_CHOICES = [
        ('emergency', 'Emergency'),  # 'emergency' gets saved in DB, 'Emergency' is what user sees
        ('normal', 'Normal'),
    ]

    CERTIFICATE_CHOICES = [
        ('marriage', 'Marriage'),
        ('birth', 'Birth'),
        ('death', 'Death'),
    ]

    email = models.EmailField()
    ward = models.PositiveIntegerField(choices=[(i, f"Ward {i}") for i in range(1, 36)])
    certificates = models.JSONField()  # To store multiple selected checkboxes as a list
    request_type = models.BooleanField(default=False)
    iscomplete= models.BooleanField(default=False,null=True)

    def __str__(self):
        return f"{self.email} - Ward {self.ward}"

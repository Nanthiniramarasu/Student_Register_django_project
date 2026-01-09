from django.db import models

# ---------------------------
# Data Model for CRUD Operations
# ---------------------------
class Data(models.Model):
    name = models.CharField(max_length=100, verbose_name="Full Name")
    contact = models.CharField(max_length=15, verbose_name="Contact Number")
    address = models.TextField(verbose_name="Address")
    mail = models.EmailField(unique=True, verbose_name="Email")

    class Meta:
        db_table = "data"
        verbose_name = "User Data"
        verbose_name_plural = "User Data"

    def __str__(self):
        return self.name

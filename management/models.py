from django.db import models
from accounts.models import Student


class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Grade(models.Model):
    standard = models.PositiveIntegerField()
    section = models.CharField(max_length=10)
    in_charge = models.ForeignKey(
        "accounts.Staff", on_delete=models.SET_NULL, null=True, related_name="grade_in_charge"
    )

    class Meta:
        unique_together = ["standard", "section"]

    def __str__(self):
        return f"{self.standard} - {self.section}"


class FeeRecord(models.Model):
    STATUS_CHOICES = [("PENDING", "Pending"), ("PAID", "Paid")]
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    payment_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PENDING")
    remarks = models.TextField(blank=True)

    class Meta:
        ordering = ["-due_date"]

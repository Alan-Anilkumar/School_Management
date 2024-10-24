from django.db import models
from datetime import date


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    total_copies = models.PositiveIntegerField()
    available_copies = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} ({self.available_copies}/{self.total_copies})"

    def is_available(self):
        return self.available_copies > 0


class LibraryRecord(models.Model):
    STATUS_CHOICES = [
        ("BORROWED", "Borrowed"),
        ("RETURNED", "Returned"),
        ("OVERDUE", "Overdue"),
    ]

    grade = models.ForeignKey("management.Grade", on_delete=models.CASCADE)
    student = models.ForeignKey("accounts.Student", on_delete=models.CASCADE)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    borrowed_date = models.DateField(default=date.today)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="BORROWED")
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student} - {self.book}"

    class Meta:
        ordering = ["-borrowed_date"]

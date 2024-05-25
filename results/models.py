from django.db import models

# Create your models here.
from django.db import models

class Result(models.Model):
    # student = models.ForeignKey('admission.Student', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.student} - {self.subject}"

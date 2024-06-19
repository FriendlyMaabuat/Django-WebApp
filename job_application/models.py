from django.db import models


class Form(models.Model):
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=90)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subscription_status = models.CharField(
        max_length=20, choices=[('free', 'Free'), ('paid', 'Paid')]
    )

    def __str__(self):
        return self.username

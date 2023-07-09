from django.db import models

class user(models.Model):
    user_id = models.TextField()
    user_name = models.TextField()
    photo_url = models.TextField()
    date_of_login = models.DateField()
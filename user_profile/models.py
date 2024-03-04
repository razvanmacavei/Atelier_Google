from django.db import models

# Create your models here.

class Logs(models.Model):

    created_at = models.DateTimeField(auto_now_add = True, blank = True)
    updated_at = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    action = models.CharField(max_length = 10)
    url = models.CharField(max_length = 100)


class Pontaj(models.Model):

    user = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null = True)
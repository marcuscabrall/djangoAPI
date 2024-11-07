from django.db import models

class User(models.Model):
    user_nickname = models.CharField(max_length=80, default='', unique=True)
    user_name = models.CharField(max_length=100, default='')
    user_email = models.EmailField(max_length=100, default='')
    user_age = models.IntegerField(default=0)

    def __str__(self):
        return f'Nickname: {self.user_nickname} | E-mail: {self.user_email}'

class UserTasks(models.Model):
    user_nickname = models.CharField(max_length=80, default='')
    user_task = models.CharField(max_length=255, default='')
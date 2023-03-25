from django.db import models


# Create your models here.


class Log(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    messages = models.JSONField(default={'state': 0})


class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=128, null=True)
    first_name = models.CharField(max_length=128, null=True)
    name = models.CharField(max_length=128, null=True)
    phone = models.CharField(max_length=15, null=True)
    menu = models.IntegerField(null=True, default=0)
    lang = models.IntegerField(null=True, default=1)
    ctg = models.CharField(max_length=128, null=True)
    subctg = models.CharField(max_length=128, null=True)

    def __str__(self):
        return f"{self.user_id} {self.username}{self.name}"


class Category(models.Model):
    name_uz = models.CharField(max_length=256, null=True)
    name_ru = models.CharField(max_length=256, null=True)
    name_en = models.CharField(max_length=256, null=True)

    def __str__(self):
        return f"{self.name_uz}"


class Subctg(models.Model):
    name = models.CharField(max_length=256, null=True)
    ctg = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}"


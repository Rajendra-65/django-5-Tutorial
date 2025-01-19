from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length = 70)
    email = models.EmailField(max_length = 255)
    city = models.CharField(max_length = 70)
    roll = models.IntegerField()
    state = models.CharField(max_length = 70)
    comment = models.CharField(max_length=70,default='nothing')

    def __str__(self):
        # We can only provide the string data type.
        return self.name

class Result (models.Model):
    stu_class = models.CharField(max_length = 70)
    marks = models.IntegerField()

    def __str__(self):
        return self.stu_class
    
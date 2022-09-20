from django.db import models

class Fizz(models.Model):
    sport = models.CharField(max_length=200, default = '')
    completed = models.BooleanField(default = False, blank = True)
    # id = models.IntegerField(blank= False)
    
    def __str__(self):
        return self.name
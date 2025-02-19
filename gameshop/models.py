from django.db import models


class GameProducer(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=100)
    producer = models.ForeignKey(GameProducer, on_delete=models.PROTECT, related_name='game_producer')
    value = models.FloatField()
    bio = models.CharField(blank= True, null= True)
    year = models.IntegerField()
    photo = models.ImageField(upload_to = 'games/', blank= True, null= True)


    

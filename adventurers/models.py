from django.db import models

class Adventurer(models.Model):
    CLASSES = [
        ('WA', 'Warrior'),
        ('SC', 'Scout'),
        ('MA','Mage'),
        ('SH','Shaman')
    ]
    name = models.CharField(max_length = 50)
    char_class = models.CharField(max_length = 15, choices=CLASSES, default='WA')
    race = models.CharField(max_length = 15)
    attack = models.IntegerField()
    defense = models.IntegerField()
    hp = models.IntegerField()
    ac = models.IntegerField()
from django.db import models

class MyWatchlistItem(models.Model):
    title = models.CharField(max_length=255)
    review = models.TextField()
    watched = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()

    #

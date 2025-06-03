from djongo import models
from bson import ObjectId

# Placeholder for models

class User(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    # ...other fields...

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)
    # ...other fields...

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    # ...other fields...

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
    # ...other fields...

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # ...other fields...

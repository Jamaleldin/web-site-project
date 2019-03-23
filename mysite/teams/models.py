from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=250)
    team_description = models.CharField(max_length=500)
    team_link1 = models.CharField(max_length=500)
    team_link2 = models.CharField(max_length=500)
    team_logo = models.FileField()

    def __str__(self):
        return self.team_name

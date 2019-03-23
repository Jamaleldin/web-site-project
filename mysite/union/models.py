from django.db import models


class STUnion(models.Model):
    committee_name = models.CharField(max_length=250)
    committee_description = models.CharField(max_length=500)
    committee_logo = models.FileField()

    def __str__(self):
        return self.committee_name

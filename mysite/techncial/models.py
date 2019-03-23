from django.db import models


class Technical(models.Model):
    technical_name = models.CharField(max_length=250)
    technical_description = models.CharField(max_length=500)
    technical_link1 = models.CharField(max_length=500)
    technical_logo = models.FileField()

    def __str__(self):
        return self.technical_name

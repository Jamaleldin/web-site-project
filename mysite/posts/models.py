# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    image = models.FileField(null=True, blank=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True , auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False , auto_now_add=True)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/posts/%s/" %(self.id)
    
    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs
    
    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type
    
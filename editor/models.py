from turtle import title

from django.db import models


class RichEditor(models.Model):
    title=models.CharField(max_length=200)
    has_img=models.BooleanField(default=False)
    img=models.ImageField(blank=True,null=True)
    description=models.TextField()
    

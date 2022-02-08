from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse("blog:view-post", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title 

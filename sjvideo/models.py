from django.db import models
from django.urls import reverse 

class Video(models.Model):
    title = models.CharField(max_length=50)
    download_url = models.URLField()
    download_page = models.URLField()
    mf_email = models.EmailField(max_length=50)
    mf_password = models.CharField(max_length=10)
    notes = models.TextField(blank=True, null=True)
    def get_absolute_url(self):
        return reverse("sjvideo:view-lesson", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title


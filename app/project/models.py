from django.db import models

# Create your models here.
class Project(models.Model):
    title       = models.CharField(max_length=100)
    author      = models.CharField(max_length=100)
    url         = models.CharField(max_length=300)
    description = models.TextField()
    image       = models.ImageField(upload_to='images')
    updated     = models.DateField()

    def __unicode__(self):
        return '<Project %s>' % self.title

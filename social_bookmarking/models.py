from django.db import models

STATUS_CHOICES = (
    (1, 'Inactive'),
    (2, 'Active'),
)

class Bookmark(models.Model):
    title           = models.CharField(max_length=255, blank=False)
    status          = models.IntegerField(choices=STATUS_CHOICES, default=2)    
    description     = models.CharField(max_length=255, blank=True, help_text="Because some things want it")
    url             = models.CharField(blank=False, max_length=255, help_text="Not a formal URL field. This field has template formatting")
    image           = models.CharField(help_text="bookmark image", max_length=100, blank=False)
    js              = models.TextField(help_text="Javascript. Lines will be stripped so make sure that you end your code correctly.", blank=True)

    def __unicode__(self):
        return unicode(self.title)
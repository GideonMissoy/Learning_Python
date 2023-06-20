from django.db import models

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.text
class Book(models.Model):
    name = models.CharField(max_length=200)
    topic = models.models.ForeignKey(Topic, verbose_name=_("topic"), on_delete=models.CASCADE)
    
    
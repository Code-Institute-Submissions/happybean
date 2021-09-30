from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Thread(models.Model):
    """
    Model for threads in forum
    """
    title = models.CharField(max_length=60)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' by ' + str(self.creator)

    def get_absolute_url(self):
        return reverse('thread', kwargs={'pk': self.pk})


class Comment(models.Model):
    """
    Model for comments on a thread.
    """
    thread = models.ForeignKey(Thread, related_name="comments",
                               on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField(max_length=1200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        # https://pyformat.info/#simple
        return "On '%s' by %s" % (self.thread, self.creator)

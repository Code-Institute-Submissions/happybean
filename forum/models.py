from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# ------------------------------------------- #
#                THREAD MODEL                 #
# ------------------------------------------- #
class Thread(models.Model):
    """
    Model for threads in forum
    """
    title = models.CharField(max_length=60)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    # Represents the class objects as a string
    # To return a string of the thread title the creator of it
    # https://www.python-course.eu/python3_magic_methods.php
    def __str__(self):
        return self.title + ' by ' + str(self.creator)

    # To handle named arguments not yet defined from:
    # https://docs.python.org/2/tutorial/controlflow.html#keyword-arguments
    def get_absolute_url(self):
        return reverse('thread', kwargs={'pk': self.pk})


# ------------------------------------------- #
#                COMMENT MODEL                #
# ------------------------------------------- #
class Comment(models.Model):
    """
    Model for comments related a thread. There field that links to
    the Thread model by foreign key. It also links to the User
    model with foreign key. There is also a field for the date
    the comment was created and edited.
    """
    thread = models.ForeignKey(Thread, related_name="comments",
                               on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField(max_length=1200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        # From: https://www.geeksforgeeks.org/python-string-format-method/
        return 'On {} by {}'.format(self.thread, self.creator)

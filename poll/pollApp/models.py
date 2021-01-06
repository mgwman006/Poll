import datetime
from django.db import models
from django.utils import timezone

# Models are created here.

class PollQuestion(models.Model):

    title = models.CharField(max_length=200)
    def __str__(self):
      return self.title


class Option(models.Model):

    question = models.ForeignKey(PollQuestion, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

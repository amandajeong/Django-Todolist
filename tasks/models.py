from django.db import models
from datetime import date, timedelta


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField('due date', blank=True, null=True)

    def __str__(self):
        return self.title

    def in_the_past(self):
        if self.due_date is not None:
            return date.today() > self.due_date
        else:
            return False

    def urgent(self):
        if self.due_date is not None:
            remaining = self.due_date - date.today()
            return remaining == timedelta(days=1)
        else:
            return False

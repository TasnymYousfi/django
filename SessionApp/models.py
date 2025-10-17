from django.db import models
from ConfirencApp.models import Confirence

# Create your models here.


class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    session_day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    confirence = models.ForeignKey(
        Confirence,
        on_delete=models.CASCADE,
        related_name="sessions"
    )

    def __str__(self):
        return f"{self.title} - {self.session_day}"

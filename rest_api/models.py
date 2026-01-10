from django.db import models


class Child(models.Model):
    """A child profile. Uses Django's default primary key field `id`."""
    
    name = models.CharField(max_length=100, blank=True, default="")

    def __str__(self) -> str:
        return f"{self.name or f'Child {self.id}'}"


class SleepTime(models.Model):
    """One sleep entry for a child."""

    child = models.ForeignKey(
        Child,
        on_delete=models.CASCADE,
        related_name="sleep_times",
    )

    date = models.DateField()
    time = models.TimeField(help_text="Time when the sleep occurred", null=True, blank=True)
    length = models.PositiveIntegerField(help_text="Length in seconds")
    comment = models.TextField(blank=True, default="")

    def __str__(self) -> str:
        return f"SleepTime(child={self.child_id}, date={self.date}, time={self.time}, length={self.length}m)"

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


class Tag(models.Model):
    """A tag that can be attached to activities."""

    name = models.CharField(max_length=80, unique=True)

    def __str__(self) -> str:
        return self.name


class Activity(models.Model):
    """One activity entry for a child."""

    child = models.ForeignKey(
        Child,
        on_delete=models.CASCADE,
        related_name="activities",
    )

    date = models.DateTimeField(help_text="Date/time of the activity")
    length = models.PositiveIntegerField(help_text="Length in seconds")
    tags = models.ManyToManyField(Tag, related_name="activities", blank=True)

    def __str__(self) -> str:
        return f"Activity(child={self.child_id}, date={self.date}, length={self.length}s)"

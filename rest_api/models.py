from django.db import models


class Child(models.Model):
    """A child profile. Uses Django's default primary key field `id`."""

    def __str__(self) -> str:
        return f"Child {self.id}"


class SleepTime(models.Model):
    """One sleep entry for a child."""

    child = models.ForeignKey(
        Child,
        on_delete=models.CASCADE,
        related_name="sleep_times",
    )

    date = models.DateField()
    length = models.PositiveIntegerField(help_text="Length in minutes")
    comment = models.TextField(blank=True, default="")

    def __str__(self) -> str:
        return f"SleepTime(child={self.child_id}, date={self.date}, length={self.length}m)"

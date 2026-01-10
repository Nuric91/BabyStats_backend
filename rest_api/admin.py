from django.contrib import admin
from .models import Child, SleepTime


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ("id",)


@admin.register(SleepTime)
class SleepTimeAdmin(admin.ModelAdmin):
    list_display = ("id", "child", "date", "length")
    list_filter = ("date", "child")
    search_fields = ("comment",)

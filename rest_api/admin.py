from django.contrib import admin
from .models import Child, SleepTime, Activity, Tag


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(SleepTime)
class SleepTimeAdmin(admin.ModelAdmin):
    list_display = ("id", "child", "date", "length", "comment")
    list_filter = ("child", "date")
    search_fields = ("comment",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("id", "child", "date", "length")
    list_filter = ("child", "date", "tags")
    search_fields = ("child__name",)
    filter_horizontal = ("tags",)  # nice M2M selector in admin form

from rest_framework import serializers
from .models import Child, SleepTime


class SleepTimeSerializer(serializers.ModelSerializer):
    # child comes from URL in nested endpoints; we still expose it in responses
    child = serializers.IntegerField(source='child_id', read_only=True)

    class Meta:
        model = SleepTime
        fields = ["id", "child", "date", "length", "comment"]


class ChildListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for listing children (no nested data)"""
    class Meta:
        model = Child
        fields = ["id", "name"]


class ChildSerializer(serializers.ModelSerializer):
    # nested read-only list (handy for a "details" screen)
    sleep_times = SleepTimeSerializer(many=True, read_only=True)

    class Meta:
        model = Child
        fields = ["id", "name", "sleep_times"]

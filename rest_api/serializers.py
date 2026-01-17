from rest_framework import serializers
from .models import Child, SleepTime, Activity, Tag


class SleepTimeSerializer(serializers.ModelSerializer):
    # child comes from URL in nested endpoints; we still expose it in responses
    child = serializers.IntegerField(source='child_id', read_only=True)

    class Meta:
        model = SleepTime
        fields = ["id", "child", "date", "time", "length", "comment"]


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


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class ActivitySerializer(serializers.ModelSerializer):
    # expose child id in responses, allow writing via child_id
    child = serializers.IntegerField(source='child_id', read_only=True)
    child_id = serializers.PrimaryKeyRelatedField(
        queryset=Child.objects.all(),
        write_only=True,
        required=False,
        source='child',
    )

    # read nested tags, write with tag_ids
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        write_only=True,
        required=False,
        source="tags",
    )

    class Meta:
        model = Activity
        fields = ["id", "child", "child_id", "date", "length", "tags", "tag_ids"]

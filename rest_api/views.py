from rest_framework import generics, viewsets
from .models import Child, SleepTime, Activity, Tag
from .serializers import (
    ChildSerializer,
    ChildListSerializer,
    SleepTimeSerializer,
    ActivitySerializer,
    TagSerializer,
)


class ChildViewSet(viewsets.ModelViewSet):
    """CRUD for children."""
    queryset = Child.objects.all().order_by("id")
    serializer_class = ChildSerializer
    
    def get_serializer_class(self):
        # Use lightweight serializer for list action
        if self.action == 'list':
            return ChildListSerializer
        return ChildSerializer


class ChildSleepTimeListCreateView(generics.ListCreateAPIView):
    """List/Create SleepTime entries for a specific child."""
    serializer_class = SleepTimeSerializer

    def get_queryset(self):
        child_id = self.kwargs["child_id"]
        return SleepTime.objects.filter(child_id=child_id).order_by("-date", "-id")

    def perform_create(self, serializer):
        child_id = self.kwargs["child_id"]
        serializer.save(child_id=child_id)


class ChildSleepTimeDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve/Update/Delete one SleepTime entry for a specific child."""
    serializer_class = SleepTimeSerializer

    def get_queryset(self):
        child_id = self.kwargs["child_id"]
        return SleepTime.objects.filter(child_id=child_id)


class TagViewSet(viewsets.ModelViewSet):
    """CRUD for tags."""
    queryset = Tag.objects.all().order_by("name", "id")
    serializer_class = TagSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """CRUD for activities (all children)."""
    queryset = Activity.objects.all().select_related("child").prefetch_related("tags").order_by("-date", "-id")
    serializer_class = ActivitySerializer


class ChildActivityListCreateView(generics.ListCreateAPIView):
    """List/Create Activity entries for a specific child."""
    serializer_class = ActivitySerializer

    def get_queryset(self):
        child_id = self.kwargs["child_id"]
        return (
            Activity.objects.filter(child_id=child_id)
            .select_related("child")
            .prefetch_related("tags")
            .order_by("-date", "-id")
        )

    def perform_create(self, serializer):
        child_id = self.kwargs["child_id"]
        # enforce the child from URL (frontend doesn't need to send it)
        serializer.save(child_id=child_id)


class ChildActivityDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve/Update/Delete one Activity entry for a specific child."""
    serializer_class = ActivitySerializer

    def get_queryset(self):
        child_id = self.kwargs["child_id"]
        return (
            Activity.objects.filter(child_id=child_id)
            .select_related("child")
            .prefetch_related("tags")
        )

from rest_framework import generics, viewsets
from .models import Child, SleepTime
from .serializers import ChildSerializer, ChildListSerializer, SleepTimeSerializer


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

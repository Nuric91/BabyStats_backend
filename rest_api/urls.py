from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    ChildViewSet,
    ChildSleepTimeListCreateView,
    ChildSleepTimeDetailView,
    TagViewSet,
    ActivityViewSet,
    ChildActivityListCreateView,
    ChildActivityDetailView,
)

router = DefaultRouter()
router.register(r"children", ChildViewSet, basename="child")
router.register(r"tags", TagViewSet, basename="tag")
router.register(r"activities", ActivityViewSet, basename="activity")

urlpatterns = [
    # /api/children/  (CRUD)
    path("", include(router.urls)),

    # /api/children/<child_id>/sleep-times/ (CRUD scoped to a child)
    path(
        "children/<int:child_id>/sleep-times/",
        ChildSleepTimeListCreateView.as_view(),
        name="child-sleep-time-list-create",
    ),
    path(
        "children/<int:child_id>/sleep-times/<int:pk>/",
        ChildSleepTimeDetailView.as_view(),
        name="child-sleep-time-detail",
    ),

    # /api/children/<child_id>/activities/ (CRUD scoped to a child)
    path(
        "children/<int:child_id>/activities/",
        ChildActivityListCreateView.as_view(),
        name="child-activity-list-create",
    ),
    path(
        "children/<int:child_id>/activities/<int:pk>/",
        ChildActivityDetailView.as_view(),
        name="child-activity-detail",
    ),
]

from django.urls import path
from habbits.views import HabbitListView, HabbitDetailView, HabbitCreateView, HabbitUpdateView, HabbitDeleteView, \
    ShareHabbitListView

app_name = "habbits"


urlpatterns = [
    path("habits/", HabbitListView.as_view(), name="show_all_habits"),
    path("habit/<int:pk>/", HabbitDetailView.as_view(), name="habit_show"),
    path("habit/create/", HabbitCreateView.as_view(), name="habit_create"),
    path("habit/update/<int:pk>/", HabbitUpdateView.as_view(), name="habit_update"),
    path("habit/delete/<int:pk>/", HabbitDeleteView.as_view(), name="habit_delete"),
    path("share_habits/", ShareHabbitListView.as_view(), name="share_habits"),
]

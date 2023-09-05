from django.urls import path
from habbits.views import HabitListView, HabitDetailView, HabitCreateView, HabitUpdateView, HabitDeleteView, \
    ShareHabitListView

app_name = "habbits"


urlpatterns = [
    path("habits/", HabitListView.as_view(), name="show_all_habits"),
    path("habit/<int:pk>/", HabitDetailView.as_view(), name="habit_show"),
    path("habit/create/", HabitCreateView.as_view(), name="habit_create"),
    path("habit/update/<int:pk>/", HabitUpdateView.as_view(), name="habit_update"),
    path("habit/delete/<int:pk>/", HabitDeleteView.as_view(), name="habit_delete"),
    path("share_habits/", ShareHabitListView.as_view(), name="share_habits"),
]

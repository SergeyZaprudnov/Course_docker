from django.urls import path
from habbits.views import HabbitListView, HabbitDetailView, HabbitCreateView, HabbitUpdateView, HabbitDeleteView, \
    ShareHabbitListView

app_name = "habbits"

urlpatterns = [
    path('habbits/', HabbitListView.as_view(), name='show_all_habbits'),
    path('habbit/<int:pk>/', HabbitDetailView.as_view(), name='habbit_show'),
    path('habbit/create/', HabbitCreateView.as_view(), name='habbit_create'),
    path('habbit/update/<int:pk>/', HabbitUpdateView.as_view(), name='habbit_update'),
    path('habbit/delete/<int:pk>/', HabbitDeleteView.as_view(), name='habbit_delete'),
    path('share_habbits/', ShareHabbitListView.as_view(), name='share_habbits'),
]

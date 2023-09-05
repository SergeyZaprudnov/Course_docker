from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UsersListView, UsersDetailView, UsersUpdateView, UsersDeleteView, \
    UsersRegistrationView

app_name = 'users'

urlpatterns = [
    path("user/", UsersListView.as_view(), name='user_list'),
    path("user/<int:pk>/", UsersDetailView.as_view(), name='user_get'),
    path("user/update/<int:pk>/", UsersUpdateView.as_view(), name='user_update'),
    path("user/delete/<int:pk>/", UsersDeleteView.as_view(), name='user_delete'),
    path("user/registration/", UsersRegistrationView.as_view(), name='user_registration'),
    path('token/', TokenObtainPairView.as_view(), name="take_token"),
    path('token/refresh/', TokenRefreshView.as_view(), name="refresh_token"),

]

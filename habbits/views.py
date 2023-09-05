from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from habbits.models import Habbit
from habbits.pagination import DataPaginator
from habbits.serializers.habbit import HabbitSerializer
from habbits.permissions import IsOwner


class HabbitListView(ListAPIView):
    queryset = Habbit.objects.all()
    serializer_class = HabbitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = DataPaginator

    def get_queryset(self):
        # check_habit_time()
        user = self.request.user
        search_owners = []
        owners = Habbit.objects.filter()
        # find and filter users habits
        for find_owner in owners:
            if find_owner.is_public is True:
                search_owners.append(find_owner)
            else:
                if find_owner.owner == user:
                    search_owners.append(find_owner)
        return search_owners


class HabbitDetailView(RetrieveAPIView):
    queryset = Habbit.objects.all()
    serializer_class = HabbitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabbitCreateView(CreateAPIView):
    queryset = Habbit.objects.all()
    serializer_class = HabbitSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()


class HabbitUpdateView(UpdateAPIView):
    queryset = Habbit.objects.all()
    serializer_class = HabbitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabbitDeleteView(DestroyAPIView):
    queryset = Habbit.objects.all()
    serializer_class = HabbitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class ShareHabbitListView(ListAPIView):
    queryset = Habbit.objects.all()
    serializer_class = HabbitSerializer

    def get_queryset(self):
        owners = Habbit.objects.filter(is_public=True)
        return owners

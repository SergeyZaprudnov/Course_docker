from rest_framework import serializers
from habbits.models import Habbit


class HabitSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        new_habbit = Habbit.objects.create(**validated_data)

        if new_habbit.duration > 120:
            raise serializers.ValidationError("Duration greater than 120 minutes!")

        if new_habbit.is_pleasant is False:
            if not new_habbit.award:
                if not new_habbit.link_pleasant:
                    raise serializers.ValidationError("Usual habit must has award or pleasant habit!")
            else:
                if new_habbit.link_pleasant:
                    raise serializers.ValidationError(
                        "Usual habit must not has award and pleasant habit simultaneously!")

            return new_habbit

        else:
            if new_habbit.award:
                raise serializers.ValidationError("Pleasant habit can not has award!")
            return new_habbit

    class Meta:
        model = Habbit
        fields = "__all__"

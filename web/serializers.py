from rest_framework import serializers

from .models import ToDo


# class ToDoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ToDo
#         fields = ('name', 'description', 'dateTime', 'attachments')


class ToDoSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    date = serializers.DateTimeField()
    userID = serializers.IntegerField()
    # attachments = serializers.CharField(allow_blank=True)

    def create(self, validated_data):
        return ToDo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.dateTime = validated_data.get('date', instance.dateTime)
        # instance.attachments = validated_data.get('attachments', instance.attachments)
        instance.save()
        return instance


# from rest_framework import serializers
#
# from urls.models import Url
#
#
# class UrlSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Url
#         fields = ('id', 'url',)

from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    short_url = serializers.ReadOnlyField()

    class Meta:
        model = Link
        fields = ('id', 'origin_url', 'short_url', 'created',)
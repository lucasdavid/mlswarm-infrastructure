from rest_framework import serializers

from .models import CSVParser, JSONParser
from ...serializers import ServiceSerializerMixin


class BaseParserSerializer(ServiceSerializerMixin,
                           serializers.Serializer):
    to_lowercase = serializers.BooleanField(
        default=False,
        help_text='Lowercase all strings in {content}.')
    ignore_features = serializers.ListField(
        default=(),
        help_text='Features in content to ignore, separated by the {delimiter}.')


class CSVParserSerializer(BaseParserSerializer):
    service_cls = CSVParser

    content = serializers.CharField(
        required=True,
        allow_null=False,
        allow_blank=False,
        help_text='The data or a valid path to it.')

    delimiter = serializers.CharField(
        max_length=1,
        default=',',
        help_text='The {content} delimiter.')


class JSONParserSerializer(BaseParserSerializer):
    service_cls = JSONParser

    content = serializers.JSONField(
        required=True,
        allow_null=False,
        help_text='The data or a valid path to it.')

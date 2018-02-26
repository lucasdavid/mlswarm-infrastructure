from rest_framework import serializers
from rest_framework.serializers import Serializer

from . import models
from ...serializers import ServiceSerializerMixin


class IEstimator(ServiceSerializerMixin,
                 Serializer):
    target = serializers.CharField(required=False)


class SimpleDenseNetworkClassifier(IEstimator):
    class Task(Serializer):
        batch_size = serializers.IntegerField(
            min_value=1,
            max_value=8192,
            help_text='Sample count in a processing batch.')

    class Training(Task):
        learning_rate = serializers.FloatField(
            min_value=0,
            default=0.01,
            help_text='Learning rate used by the optimizer when adjusting '
                      'weights.')
        optimizer = serializers.CharField(
            max_length=32,
            default='adam',
            help_text='Optimizer used to train the network.')
        dropout = serializers.FloatField(
            min_value=0,
            max_value=1,
            default=0.5,
            help_text='Dropout probability rate used in the dropout layers. '
                      '0 means no dropout at all.')

    class Testing(Task):
        metrics = serializers.ListField(
            child=serializers.CharField(),
            min_length=1,
            help_text='Metrics to be computed in this test.')

    class Prediction(Task):
        pass

    input_units = serializers.IntegerField(min_value=1, required=True)
    inner_units = serializers.IntegerField(min_value=1, required=True)
    output_units = serializers.IntegerField(min_value=1, required=True)
    inner_layers = serializers.IntegerField(min_value=0, required=True)
    activations = serializers.CharField(max_length=32, default='relu')

    service_cls = models.SimpleDenseNetworkClassifier


class SimpleRegressor(IEstimator):
    class Training(Serializer):
        max_iterations = serializers.IntegerField(min_value=-1)

    class Prediction(Serializer):
        pass

    input_units = serializers.IntegerField(min_value=1, required=True)
    output_units = serializers.IntegerField(min_value=1, required=True)

    service_cls = models.SimpleRegressor
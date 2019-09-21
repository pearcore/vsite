from rest_framework import serializers
from finance.models import FinanceType


class FinanceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinanceType
        fields = ('id', 'Name', 'CreateDate')
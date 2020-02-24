from rest_framework import serializers
from hrm.models import Users


class UsersSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    phone = serializers.IntegerField(required=False)
    birth = serializers.DateField(required=False)
    class Meta:
        model = Users
        # fields = ('name', 'employee_id')
        fields = '__all__'

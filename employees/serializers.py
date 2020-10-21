from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Employee
		fields = ('idcode', 'url', 'name', 'emptype', 'empstatus', 'datejoin', 'jobdescrp', 'branch', 'photo')


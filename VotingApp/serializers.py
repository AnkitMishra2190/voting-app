from rest_framework import serializers
from VotingApp.models  import *


class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"




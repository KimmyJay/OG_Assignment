from rest_framework import serializers
from base.models import ArtistApplication as ArtistApplicationModel

class ArtistApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistApplicationModel
        fields = "__all__"
from rest_framework import serializers
from .models import Comics



class ComicsSerializer(serializers.ModelSerializer):
    """Comics serializer. """

    class Meta:
        model = Comics
        fields = (
            'id',
            'title',
            'published',
            'episode',
            'description'
        )
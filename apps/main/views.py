from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Comics
from .serializers import ComicsSerializer




class ComicsView(APIView):
    """ComicsView"""

    def get(
        self,
        request,
        *args,
        **kwargs
    ) -> Response:
        queryset = Comics.objects.all()
        serializer: ComicsSerializer = ComicsSerializer(
            queryset,
            many=True
        )
        return Response({
            'data': {
                'comics': serializer.data
            }
        })
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from foods.models import Food, FoodCategory
from foods.serializers import FoodListSerializer, FoodSerializer


class FoodListAPIView(APIView):
    def get(self, request):
        categories = FoodCategory.objects.prefetch_related('food').filter(
            food__is_publish=True).distinct().order_by('id')
        serializer = FoodListSerializer(categories, many=True)
        return Response(serializer.data)


class FoodDetail(generics.RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

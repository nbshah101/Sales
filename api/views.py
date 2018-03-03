import django_filters.rest_framework
from rest_framework import generics
from .serializers import SalesListSerializer
from .models import Sales
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class GetView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    #queryset = Sales.objects.all()
    serializer_class = SalesListSerializer

    def get_queryset(self):
        queryset = Sales.objects.all()
        vin = self.request.query_params.get('vin')
        make = self.request.query_params.get('make')
        model = self.request.query_params.get('model')
        seller = self.request.query_params.get('seller')

        if vin:
            queryset = queryset.filter(vin=vin)
        elif make:
            queryset = queryset.filter(make=make)
        elif model:
            queryset = queryset.filter(model=model)
        elif seller:
            queryset = queryset.filter(seller=seller)

        return queryset


@method_decorator(csrf_exempt, name='dispatch')
class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Sales.objects.all()[:5]
    serializer_class = SalesListSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


@method_decorator(csrf_exempt, name='dispatch')
class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT requests."""

    queryset = Sales.objects.all()
    serializer_class = SalesListSerializer
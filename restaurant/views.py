from django.shortcuts import render
from rest_framework import viewsets, routers
from rest_framework import generics
from rest_framework.response import Response
from .models import MenuItem, Booking  # Import your MenuItem model
from .serializers import MenuItemSerializer, BookingSerializer  # Import your MenuItemSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def index(request):
  return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


# Create a router and register the viewset with URL routes
router = routers.DefaultRouter()
router.register(r'bookings', BookingViewSet)

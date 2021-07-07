from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from .serializers import CartSerializer
from .models import Cart
from rest_framework import viewsets


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', ]

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        # qs = self.get_queryset()
        qs = qs.filter(user=user)
        return qs

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}

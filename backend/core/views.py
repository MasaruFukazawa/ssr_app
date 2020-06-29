#-*- coding: utf-8 -*-

from rest_framework import viewsets
from .serializers import RecipeSerializer
from .models import Recipe

from rest_framework.permissions import IsAuthenticated


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    #permission_classes = [IsAuthenticated]

from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .services import generate_shopping_list

class ShoppingListView(APIView):
    def get(self, request):
        data = generate_shopping_list()
        response = [
            {"ingredient": k, "quantity": v}
            for k, v in data.items()
        ]
        return Response(response)

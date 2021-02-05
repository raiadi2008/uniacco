from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, HttpResponse
from .serializers import UserSerializer
from .models import User

class RegisterView(GenericAPIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'username':serializer.data.get('username')}, status=HTTP_201_CREATED )
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

class LoginView(GenericAPIView):
    def post(self,request):
        data = JSONParser().parse(request)
        user_name = data['username']
        pass_word = data['password']

        try:
            user = User.objects.get(username=user_name, password = pass_word, )
            return JsonResponse(user.token(), status=HTTP_200_OK)

        except :
            return HttpResponse(status=400)



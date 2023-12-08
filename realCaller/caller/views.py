from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from .models import Contacts
from django.shortcuts import render,redirect,get_object_or_404

User = get_user_model()

@api_view(['POST'])
def user_registration(request):
    if request.method == 'POST':
        username = request.data.get('username')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        phone = request.data.get('phone')
        password1 = request.data.get('pass1')
        password2 = request.data.get('pass2')

        if not username:
            return Response({"message": "Username can't be empty"}, status=status.HTTP_400_BAD_REQUEST)

        if not password1:
            return Response({"message": "Password can't be empty"}, status=status.HTTP_400_BAD_REQUEST)

        if not password2:
            return Response({"message": "Password can't be empty"}, status=status.HTTP_400_BAD_REQUEST)

        if not first_name:
            return Response({"message": "First name can't be empty"}, status=status.HTTP_400_BAD_REQUEST)

        if not last_name:
            return Response({"message": "Last name can't be empty"}, status=status.HTTP_400_BAD_REQUEST)

        if not phone:
            return Response({"message": "Phone number can't be empty"}, status=status.HTTP_400_BAD_REQUEST)

        if password1 != password2:
            return Response({"message": "Password Mismatch"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"message": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(phone=phone).exists():
            return Response({"message": "Number is already registered"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password1, email=email, phone=phone, first_name=first_name, last_name=last_name)
        user.save()
        contact = Contacts.objects.create(name=f"{first_name} {last_name}", phone=phone, registered_user=True, email=email)
        contact.save()
        return Response({"message": "User Created"}, status=status.HTTP_201_CREATED)
    


@api_view(['POST'])
def report_spam(request):
    if request.method == 'POST':
        phone_number = request.data.get('phone_number')

        if not phone_number:
            return Response({"message": "Phone number is required"}, status=status.HTTP_400_BAD_REQUEST)

        contact = get_object_or_404(Contacts, phone=phone_number)
        contact.spam_count += 1
        contact.save()

        return Response({"message": f"Phone number {phone_number} reported as spam"}, status=status.HTTP_200_OK)



@api_view(['GET'])
def search_person_by_name(request):
        name_query = request.query_params.get('name', '')
        if not name_query:
            return Response({"message": "Name query is required"}, status=status.HTTP_400_BAD_REQUEST)
        results = Contacts.objects.filter(name__icontains=name_query)
        serialized_results = [
            {
                "name": result.name,
                "phone_number": result.phone,
                "spam_count": result.spam_count
            }
            for result in results
        ]

        return Response(serialized_results, status=status.HTTP_200_OK)





@api_view(['GET'])
def search_person_by_phone(request):
    phone_query = request.query_params.get('phone', '')
    if not phone_query:
        return Response({"message": "Phone number query is required"}, status=status.HTTP_400_BAD_REQUEST)
    results = Contacts.objects.filter(phone=phone_query)
    registered_user_results = results.filter(registered_user=True)
    if registered_user_results.exists():
        serialized_results = [
            {
                "name": result.name,
                "phone_number": result.phone,
                "spam_count": result.spam_count
            }
            for result in registered_user_results
        ]
        return Response(serialized_results, status=status.HTTP_200_OK)
    else:
        serialized_results = [
            {
                "name": result.name,
                "phone_number": result.phone,
                "spam_count": result.spam_count
            }
            for result in results
        ]
        return Response(serialized_results, status=status.HTTP_200_OK) 
    



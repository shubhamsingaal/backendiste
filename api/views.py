from datetime import datetime
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Alumni, blog, Event, Student, gallery, sponsers , Contact
from .serializers import AlumniSerializer,blogSerializer, EventsSerializer, StudentSerializer, gallerySerializer, sponsersSerializer , ContactSerializer
from rest_framework.generics import ListAPIView
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # def get_queryset(self):
    #   final = Student.objects.all().filter(year__gte=4)
    #   others = Student.objects.all()

    #   return final.union(others, all=True)


class AlumniList(ListAPIView):
    queryset = Alumni.objects.all()
    serializer_class = AlumniSerializer


class EventsList(ListAPIView):
    queryset = Event.objects.all().order_by('-StartDate')
    serializer_class = EventsSerializer

class galleryList(ListAPIView):
    queryset = gallery.objects.all().order_by('-imgDate')
    serializer_class = gallerySerializer

class blogList(ListAPIView):
    queryset = blog.objects.all().order_by('-StartDate')
    serializer_class = blogSerializer

class sponsersList(ListAPIView):
    queryset = sponsers.objects.all()
    serializer_class = sponsersSerializer


@api_view(['POST'])
def messages(request):
    if request.method == 'POST':
        contact_data = JSONParser().parse(request)
        contact_serializer = ContactSerializer(data=contact_data)
        if contact_serializer.is_valid():
            # contact_serializer.save()
            send_mail(
                "Message from "+contact_data["name"] + " on ISTE Website",
                contact_data["message"],
                settings.EMAIL_HOST_USER,
                ['jnvomprakash121@gmail.com'],
                fail_silently=False
            )
            send_mail(
                "Welcome to ISTE NIT Durgapur",
                "we have got your message, Our team will reply you as soon as possible.😊",
                settings.EMAIL_HOST_USER,
                [contact_data["email"]],
                fail_silently=False
            )
            return JsonResponse(contact_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(contact_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

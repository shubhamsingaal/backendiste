from rest_framework import serializers


from .models import Alumni, Event, Student, gallery, sponsers , blog, Contact

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['id', 'name','image','phoneno', 'email','facebook','instagram','linkedin','post','year','order']

class AlumniSerializer(serializers.ModelSerializer):
  class Meta:
    model = Alumni
    fields = ['id', 'name','image','phoneno', 'email','facebook','instagram','linkedin','passyear']

class EventsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ['id', 'EventName','Image','StartDate','EndDate','Location','Link','Description','EventTense']

class gallerySerializer(serializers.ModelSerializer):
  class Meta:
    model = gallery
    fields = ['id','Image','eventName','imgDate']

class blogSerializer(serializers.ModelSerializer):
  class Meta:
    model = blog
    fields = ['id', 'blogName', 'Image', 'Link', 'Description','StartDate']

class sponsersSerializer(serializers.ModelSerializer):
  class Meta:
    model = sponsers
    fields = ['id','Image','Link']


class ContactSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Contact
        fields = ('id',
                  'name',
                  'email',
                  'phone','message')
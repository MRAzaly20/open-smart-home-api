from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from django.contrib.auth.hashers import make_password
from rest_framework.generics import CreateAPIView,GenericAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from .models import  (Author, Publisher, Customer, Store, Purchase, Book, Device,
Sensor, Action, Event, Room, Schedule, UserSetting, DeviceSetting, Notification,
AutomationRule, EnergyUsage, Firmware, UserGroup, GroupMember)
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework import status, views
from rest_framework import viewsets
from django.contrib.auth.models import User
from . import serializers
from .serializers import (TodoSerializer, AuthorSerializer, UserSerializer,
LoginSerializer, PublisherSerializer,
UpdateUserSerializer,UserProfileSerializer, UpdatePassSerializer,
CustomerSerializer, StoreSerializer, BookSerializer, PurchaseSerializer,
LogoutSerializer ,MyTokenObtainPairSerializer, DeviceSerializer,
SensorSerializer, ActionSerializer, EventSerializer, RoomSerializer,
ScheduleSerializer, UserSettingSerializer, DeviceSettingSerializer,
NotificationSerializer, AutomationRuleSerializer, GetRoomSerializer, EnergyUsageSerializer,
FirmwareSerializer, UserGroupSerializer, GroupMemberSerializer)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class MyTokenRefreshView(TokenRefreshView):
    # Anda bisa menambahkan custom logic jika diperlukan
    pass

class RestrictedView(APIView):
  permission = (IsAuthenticated,)
  
  def get(self, request, format=None):
    print(request)
    return JsonResponse({"response":"access granted"})

class UpdatePassView(APIView):
    
    #def put(self, request):
    #queryset = User.objects.all()
    permission = (IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        print(request.user)
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        
        # Pastikan bahwa request.user adalah user yang sama dengan yang ingin di-update
        if not user:
            return Response({"authorize": "You don't have permission for this user."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = UpdatePassSerializer(user, data=request.data, context={'user_id': user_id})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UpdateProfileView(APIView):
    
    permission = (IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        print(request.user)
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        
        # Pastikan bahwa request.user adalah user yang sama dengan yang ingin di-update
        if not user:
            return Response({"authorize": "You don't have permission for this user."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer_user = UpdateUserSerializer(user, data=request.data, context={'user_id': user_id})
        serializer_custom = UserProfileSerializer(user, data=request.data, context={'user_id': user_id})
        if serializer_user.is_valid() and serializer_custom.is_valid():
            serializer_user.save()
            serializer_custom.save()
            return Response({"message": "Profile updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer_custom.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class RegisterView(views.APIView):
    def post(self, request):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(views.APIView):
    def post(self, request):
        serializer_data = LoginSerializer(data=request.data)
        if serializer_data.is_valid():
            user = serializer_data.validated_data
            print("user :" , user)
            #token = user.auth_token
            return Response({"tokens": user})
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LogoutAPIView(GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            return Response(TodoSerializer(user).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

# View untuk User

class TodoCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        password = make_password(self.request.data.get('password'))
        serializer.save(password=password)
        
class TodoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    read_serializer = TodoSerializer(queryset, many=True)
    #print(read_serializer.data)
    serializer_class = TodoSerializer

# View untuk Author
class AuthorCreateView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# View untuk Publisher
class PublisherCreateView(CreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class PublisherDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

# View untuk Customer
class CustomerCreateView(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class StoreCreateView(CreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class StoreDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    
class PurchaseCreateView(CreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class PurchaseDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    
class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class TodoListView(
  APIView, 
  UpdateModelMixin, 
  DestroyModelMixin,
):

  def get(self, request, id=None):
    if id:
      try:
        queryset = User.objects.get(id=id)
      except User.DoesNotExist:
        return Response({'errors': 'This User item does not exist.'}, status=400)
      read_serializer = TodoSerializer(queryset)

    else:
      queryset = User.objects.all()
      read_serializer = TodoSerializer(queryset, many=True)

    return Response(read_serializer.data)


  def post(self, request):
    create_serializer = TodoSerializer(data=request.data)

    if create_serializer.is_valid():
      todo_item_object = create_serializer.save()
      read_serializer = TodoSerializer(todo_item_object)
      return Response(read_serializer.data, status=201)

    return Response(create_serializer.errors, status=400)


  def put(self, request, id=None):
    try:
      todo_item = User.objects.get(id=id)
    except User.DoesNotExist:
      return Response({'errors': 'This User item does not exist.'}, status=400)

    update_serializer = TodoSerializer(todo_item, data=request.data)

    if update_serializer.is_valid():
      todo_item_object = update_serializer.save()
      read_serializer = TodoSerializer(todo_item_object)
      return Response(read_serializer.data, status=200)

    return Response(update_serializer.errors, status=400)


  def delete(self, request, id=None):
    try:
      todo_item = User.objects.get(id=id)
    except User.DoesNotExist:
      return Response({'errors': 'This User item does not exist.'}, status=400)

    todo_item.delete()

    return Response(status=204)

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [IsAuthenticated]

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    permission_classes = [IsAuthenticated]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]
    
class GetRoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = GetRoomSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        user = self.request.data.get('user')
        name = request.data.get('name')
        print("user :", self.request)
        print("name :", name)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        for room in serializer.data:
            room_id = room['id']
            room['total_device_count'] = Room.objects.get(id=room_id).device_set.count()
        return Response(serializer.data)

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]

class UserSettingViewSet(viewsets.ModelViewSet):
    queryset = UserSetting.objects.all()
    serializer_class = UserSettingSerializer
    permission_classes = [IsAuthenticated]

class DeviceSettingViewSet(viewsets.ModelViewSet):
    queryset = DeviceSetting.objects.all()
    serializer_class = DeviceSettingSerializer
    permission_classes = [IsAuthenticated]

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

class AutomationRuleViewSet(viewsets.ModelViewSet):
    queryset = AutomationRule.objects.all()
    serializer_class = AutomationRuleSerializer
    permission_classes = [IsAuthenticated]

class EnergyUsageViewSet(viewsets.ModelViewSet):
    queryset = EnergyUsage.objects.all()
    serializer_class = EnergyUsageSerializer
    permission_classes = [IsAuthenticated]

class FirmwareViewSet(viewsets.ModelViewSet):
    queryset = Firmware.objects.all()
    serializer_class = FirmwareSerializer
    permission_classes = [IsAuthenticated]

class UserGroupViewSet(viewsets.ModelViewSet):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer
    permission_classes = [IsAuthenticated]

class GroupMemberViewSet(viewsets.ModelViewSet):
    queryset = GroupMember.objects.all()
    serializer_class = GroupMemberSerializer
    permission_classes = [IsAuthenticated]
    
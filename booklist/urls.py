from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import (TodoCreateView, TodoDetailView, AuthorCreateView,
AuthorDetailView, PublisherCreateView, PublisherDetailView, CustomerCreateView,
CustomerDetailView, TodoListView, StoreDetailView, StoreCreateView,
PurchaseDetailView, PurchaseCreateView, BookCreateView, BookDetailView,
LoginView, RegisterView, LoginAPIView, RestrictedView,
UpdateProfileView,LogoutAPIView, UpdatePassView, MyTokenObtainPairView)

from django.urls import path
from .views import (
     DeviceViewSet, GetRoomViewSet, SensorViewSet, ActionViewSet, EventViewSet,
    RoomViewSet, ScheduleViewSet, UserSettingViewSet, DeviceSettingViewSet,
    NotificationViewSet, AutomationRuleViewSet, EnergyUsageViewSet,
    FirmwareViewSet, UserGroupViewSet, GroupMemberViewSet,
    TodoCreateView, TodoDetailView, AuthorCreateView,
AuthorDetailView, PublisherCreateView, PublisherDetailView, CustomerCreateView,
CustomerDetailView, TodoListView, StoreDetailView, StoreCreateView,
PurchaseDetailView, PurchaseCreateView, BookCreateView, BookDetailView,
LoginView, RegisterView, LoginAPIView, RestrictedView,
UpdateProfileView,LogoutAPIView, UpdatePassView, MyTokenObtainPairView
)

urlpatterns = [
    # Todos
    path('todos/', TodoCreateView.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('todos/all/', TodoListView.as_view(), name='todo-all-detail'),

    # Authors
    path('authors/', AuthorCreateView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

    # Publishers
    path('publishers/', PublisherCreateView.as_view(), name='publisher-list'),
    path('publishers/<int:pk>/', PublisherDetailView.as_view(), name='publisher-detail'),

    # Customers
    path('customers/', CustomerCreateView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),

    # Stores
    path('store/', StoreCreateView.as_view(), name='store-list'),
    path('store/<int:pk>/', StoreDetailView.as_view(), name='store-detail'),

    # Purchases
    path('purchase/', PurchaseCreateView.as_view(), name='purchase-list'),
    path('purchase/<int:pk>/', PurchaseDetailView.as_view(), name='purchase-detail'),
    
    # Books
    path('book/', BookCreateView.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Authentication
    path('api/login/', LoginView.as_view(), name='api_login'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/update/password/<int:pk>/', UpdatePassView.as_view(), name='update-pass'),
    path('api/update/profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('api/restricted/', RestrictedView.as_view(), name='access'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', LogoutAPIView.as_view(), name="logout"),

    # Smart Home
    path('api/all/get/put/rooms/', GetRoomViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='room-list'),
    path('api/test/get/put/rooms/<uuid:pk>/', GetRoomViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='room-detail'),
    path('api/create/devices/', DeviceViewSet.as_view({'get': 'list', 'post': 'create'}), name='device-list'),
    path('api/get/put/devices/<uuid:pk>/', DeviceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='device-detail'),
    path('api/create/sensors/', SensorViewSet.as_view({'get': 'list', 'post': 'create'}), name='sensor-list'),
    path('api/get/put/sensors/<uuid:pk>/', SensorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='sensor-detail'),
    path('api/create/actions/', ActionViewSet.as_view({'get': 'list', 'post': 'create'}), name='action-list'),
    path('api/get/put/actions/<uuid:pk>/', ActionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='action-detail'),
    path('api/create/events/', EventViewSet.as_view({'get': 'list', 'post': 'create'}), name='event-list'),
    path('api/get/put/events/<uuid:pk>/', EventViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='event-detail'),
    path('api/create/rooms/', GetRoomViewSet.as_view({'get': 'list', 'post': 'create'}), name='room-list'),
    path('api/get/put/rooms/<uuid:pk>/', GetRoomViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='room-detail'),
    path('api/create/schedules/', ScheduleViewSet.as_view({'get': 'list', 'post': 'create'}), name='schedule-list'),
    path('api/get/put/schedules/<uuid:pk>/', ScheduleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='schedule-detail'),
    path('api/create/user-settings/', UserSettingViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-setting-list'),
    path('api/get/put/user-settings/<uuid:pk>/', UserSettingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-setting-detail'),
    path('api/create/device-settings/', DeviceSettingViewSet.as_view({'get': 'list', 'post': 'create'}), name='device-setting-list'),
    path('api/get/put/device-settings/<uuid:pk>/', DeviceSettingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='device-setting-detail'),
    path('api/create/notifications/', NotificationViewSet.as_view({'get': 'list', 'post': 'create'}), name='notification-list'),
    path('api/get/put/notifications/<uuid:pk>/', NotificationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='notification-detail'),
    path('api/create/automation-rules/', AutomationRuleViewSet.as_view({'get': 'list', 'post': 'create'}), name='automation-rule-list'),
    path('api/get/put/automation-rules/<uuid:pk>/', AutomationRuleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='automation-rule-detail'),
    path('api/create/energy-usage/', EnergyUsageViewSet.as_view({'get': 'list', 'post': 'create'}), name='energy-usage-list'),
    path('api/get/put/energy-usage/<uuid:pk>/', EnergyUsageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='energy-usage-detail'),
    path('api/create/firmware/', FirmwareViewSet.as_view({'get': 'list', 'post': 'create'}), name='firmware-list'),
    path('api/get/put/firmware/<uuid:pk>/', FirmwareViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='firmware-detail'),
    path('api/create/user-groups/', UserGroupViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-group-list'),
    path('api/get/put/user-groups/<uuid:pk>/', UserGroupViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-group-detail'),
    path('api/create/group-members/', GroupMemberViewSet.as_view({'get': 'list', 'post': 'create'}), name='group-member-list'),
    path('api/get/put/group-members/<uuid:pk>/', GroupMemberViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='group-member-detail'),
]

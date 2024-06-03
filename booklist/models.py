from django.db import models
from django.db.models.fields import AutoField
from django.db.models.fields import checks
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.contrib.auth.models import User
import uuid


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
    related_name='user_profile')
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    class Meta:
        db_table = 'user_profile' 
        ordering = ['phone_number']  
        verbose_name = 'user_profile' 
        verbose_name_plural = 'user_profile'  
        
        
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField( max_length=105)
    birthdate = models.DateField()

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'author' 
        ordering = ['name'] 
        verbose_name = 'Author' 
        verbose_name_plural = 'Authors' 
        
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
        
    class Meta:
        db_table = 'publisher'
        ordering = ['name']
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'

class Book(models.Model):
    id = models.AutoField(primary_key= True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'book'
        ordering = ['-publication_date', 'title'] 
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        

class Store(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=110)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book,related_name='booklist_lu_groups')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'store'
        ordering = ['name']
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField( max_length=110)
    purchased_books = models.ManyToManyField(Book,related_name='booklist_lu2_groups',  through='Purchase')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'customer'
        ordering = ['name']
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    purchase_date = models.DateField()

    def __str__(self):
        return f"{self.customer.name} purchased {self.book.title}"
    
    class Meta:
        db_table = 'purchase'
        ordering = ['purchase_date']
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'     

# Model User yang diperluas dari AbstractUser
#class User(AbstractUser):
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

# Model Room
class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=255, blank=True, unique=True)
    total_device_count = models.CharField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
    class Meta:
        db_table = 'Room' 
        ordering = ['name']  
        verbose_name = 'Room' 
        verbose_name_plural = 'Room'  
# Model Device

class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    room = models.ForeignKey(Room, on_delete=models.CASCADE,
    default=uuid.uuid4, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=10, choices=[('online', 'Online'), ('offline', 'Offline'), ('error', 'Error')])
    device_type = models.CharField(max_length=255)
    io_address = models.CharField(max_length=255, default='0.0.0.0')  
    data_type = models.CharField(max_length=255, blank=True)  
    protocol = models.CharField(max_length=255, default='opc ua')  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    digital_value = models.BooleanField(null=True, blank=True)   
    analog_value = models.FloatField(null=True, blank=True)     
    
    def __str__(self):
        return self.user.username
    class Meta:
        db_table = 'Device' 
        ordering = ['name']  
        verbose_name = 'Device' 
        verbose_name_plural = 'Device'  
# Model Sensor
class Sensor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sensor_type = models.CharField(max_length=255)
    unit = models.CharField(max_length=255, blank=True)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'Sensor' 
        ordering = ['name']  
        verbose_name = 'Sensor' 
        verbose_name_plural = 'Sensor'  
        
# Model Action
class Action(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    command = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Model Event
class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=255)
    value = models.FloatField()
    action = models.ForeignKey(Action, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField()


# Model Schedule
class Schedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()
    repeat = models.CharField(max_length=10, choices=[('none', 'None'), ('daily', 'Daily'), ('weekly', 'Weekly'), ('custom', 'Custom')])
    active = models.BooleanField(default=True)

# Model UserSetting
class UserSetting(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    setting_key = models.CharField(max_length=255)
    setting_value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Model DeviceSetting
class DeviceSetting(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    setting_key = models.CharField(max_length=255)
    setting_value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Model Notification
class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    message = models.TextField()
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField()

# Model AutomationRule
class AutomationRule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    trigger = models.ForeignKey(Event, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    condition = models.JSONField()
    active = models.BooleanField(default=True)

# Model EnergyUsage
class EnergyUsage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    energy_consumed = models.FloatField()

# Model Firmware
class Firmware(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device_type = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    release_notes = models.TextField(blank=True)
    url = models.URLField()
    released_at = models.DateTimeField()

# Model UserGroup
class UserGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Model GroupMember
class GroupMember(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('member', 'Member')])
    joined_at = models.DateTimeField()


'''
class User(AbstractUser):
    class Meta:
      permissions = (('can_drive', 'Can drive'),)
  
class TodoManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Todo(AbstractBaseUser):
    username = models.CharField( max_length=110, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False) # Tambahkan ini untuk kontrol admin
    is_staff = models.BooleanField(default=False) # Tambahkan ini untuk memenuhi kebutuhan Django admin
    is_superuser = models.BooleanField(default=False) # Tambahkan ini untuk superuser

    objects = TodoManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
  
    class Meta:
        db_table = 'todo'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
'''

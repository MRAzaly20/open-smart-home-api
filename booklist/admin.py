from django.contrib import admin
from .models import UserProfile
from django.contrib import admin
from .models import (
    Device, Sensor, Action, Event, Room, Schedule,
    UserSetting, DeviceSetting, Notification, AutomationRule,
    EnergyUsage, Firmware, UserGroup, GroupMember,
    Author, Publisher, Customer, Purchase, Store, Book
)

# Daftar semua model Anda secara otomatis
models = [Device, Sensor, Action, Event, Room, Schedule,
          UserSetting, DeviceSetting, Notification, AutomationRule,
          EnergyUsage, Firmware, UserGroup, GroupMember,
          Author, Publisher, Customer, Purchase, Store, Book, UserProfile]

for model in models:
    admin.site.register(model)


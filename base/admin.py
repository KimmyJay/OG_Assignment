from django.contrib import admin
from .models import (
    User as UserModel,
    UserType as UserTypeModel
)

admin.site.register(UserModel)
admin.site.register(UserTypeModel)
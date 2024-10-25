from django.contrib import admin
from adminpanel.models import *
# Register your models here.
admin.site.register(Estado)
admin.site.register(Rol)
admin.site.register(Permiso)
admin.site.register(RolPermiso)
admin.site.register(Usuario)
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class Estado(models.Model):
    estado = models.CharField(max_length= 15, unique=True)
    descripcion = models.CharField(max_length= 30, blank=True)

    def __str__(self):
        return self.estado
    
    class Meta:
        verbose_name_plural = "Estados"
    
class Rol(models.Model):
    rol = models.CharField(max_length=50, unique=True)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return self.rol
    
    class Meta:
        verbose_name_plural = "Roles"

class Permiso(models.Model):
    permiso = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.permiso
    
    class Meta:
        verbose_name_plural = "Permisos"

class RolPermiso(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)
    permiso = models.ForeignKey(Permiso, on_delete=models.PROTECT)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    fecha_asignacion = models.DateTimeField(auto_now_add=True) #Este campo indica cuando se asigno el registro

    class Meta:
        unique_together = ('rol', 'permiso')  # Garantiza que no haya duplicados
        verbose_name_plural = "roles y permisos"

    def __str__(self):
        return f"{self.rol} - {self.permiso}"
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    usuario = models.CharField(max_length=20, unique=True)
    contrasena = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.usuario
    
    def save(self, *args, **kwargs):
        # Si la contraseña no está en hash, la convertimos en hash antes de guardar
        if not self.contrasena.startswith('pbkdf2_sha256$'):  # Verifica si ya está hasheada
            self.contrasena = make_password(self.contrasena)
        super(Usuario, self).save(*args, **kwargs)

    def set_contrasena(self, raw_password):
        #Convierte la contraseña en un hash seguro antes de guardarla.
        self.contrasena = make_password(raw_password)

    def verificar_contrasena(self, raw_password):
        #Verifica si la contraseña en texto plano coincide con el hash almacenado.
        return check_password(raw_password, self.contrasena)

    def obtener_permisos(self):
        #Obtiene todos los permisos activos asociados al rol del usuario.
        return Permiso.objects.filter(
            rolpermiso__rol=self.rol,
            estado__estado="activo",
            rolpermiso__estado__estado="activo"
        )
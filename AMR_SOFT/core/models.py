from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from AMR_SOFT import settings

# Create your models here.
#MODELOS PARA EL APARTADO DE ROLES, USUARIOS, PERMISOS Y ESTADO
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
    
#Los siguientes modelos son los que comprenden en si la logica del negocio.
class Pais(models.Model):
    pais = models.CharField(max_length=30)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return self.pais
    
    class Meta:
        verbose_name_plural = "Paises"

class Club(models.Model):
    club = models.CharField(max_length=30)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return self.club
    
    class Meta:
        verbose_name_plural = "Clubes"

class Posicion(models.Model):
    posicion = models.CharField(max_length=10, unique=True)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return self.posicion
    
    class Meta:
        verbose_name_plural = "Posiciones"

class Puesto(models.Model):
    puesto = models.CharField(max_length=30, unique=True)
    abreviatura = models.CharField(max_length=5, unique=True)
    posicion = models.ForeignKey(Posicion, on_delete=models.PROTECT)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return self.puesto
    
    class Meta:
        verbose_name_plural = "Puestos"

class TipoCualidad(models.Model):
    tipo_cualidad = models.CharField(max_length=30, unique=True)
    descripcion = models.CharField(max_length=128)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return self.tipo_cualidad
    
    class Meta:
        verbose_name_plural = "Tipo Cualidades"

class Cualidad(models.Model):
    cualidad = models.CharField(max_length=30, unique=True)
    descripcion = models.CharField(max_length=128)
    tipo_cualidad = models.ForeignKey(TipoCualidad, on_delete=models.PROTECT)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return self.cualidad
    
    class Meta:
        verbose_name_plural = "Cualidades"

class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    puesto = models.ForeignKey(Puesto, on_delete=models.PROTECT)
    fecha_nac = models.DateField()
    altura = models.IntegerField() #la altura del jugador en centimetros
    peso = models.DecimalField(max_digits=5, decimal_places=2) #el peso del jugador en kg, acepta maximo de 5 digitos entre ellos 2 decimales
    pierna_habil = models.CharField(max_length=3)
    foto = models.ImageField(upload_to='fotos/')
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    
    create_at =models.DateTimeField(auto_now_add=True)
    uploaded_at =models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Usuario, related_name='jugadores_creados', on_delete=models.PROTECT)
    uploaded_by = models.ForeignKey(Usuario, related_name='jugadores_actualizados', on_delete=models.PROTECT, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey(Usuario, related_name='jugadores_eliminados', on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}" 
    
    def get_image(self):
        if self.imagen:
            return '{}{}'.format(settings.MEDIA_URL, self.imagen)
        return '{}{}'.format(settings.STATIC_URL, 'static/img/default/empty.jpg')

    class Meta:
        verbose_name_plural = "Jugadores"
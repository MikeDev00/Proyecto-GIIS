from django.urls import reverse
from djongo import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from ckeditor.fields import RichTextField 
from autoslug import AutoSlugField


class Usuario(models.Model):
    pass

class PruebaBit(models.Model):

    class params:
        db = 'default'
 
    fecha= models.CharField('Fecha', max_length=100, blank=True, null= True)
    hour= models.CharField('Hora', max_length=100, blank=True, null = True)
    place= models.CharField( max_length=100, blank=True, null = True)
    operator= models.CharField('Operador',max_length=100, blank=True, null = True)
    latitude= models.FloatField('Latitud',max_length=100, blank=True, null = True)
    longitude= models.FloatField('Longitud',max_length=100, null=True, blank=True, default=None)
    altitud= models.DecimalField('Altitud', null=True,blank=True, default =None, max_digits=8, decimal_places=2,)
    statype =  models.CharField('Tipo de Estación',max_length=100, blank=True, null = True)
    senstype = models.CharField('Tipo de Sensor',max_length=100, blank=True, null = True)
    statnum  = models.CharField('# de Estación',max_length=100, blank=True, null = True)
    sensnum = models.CharField('# de Sensor',max_length=100, blank=True, null = True)
    freq = models.FloatField('Frecuencia (Hz)',max_length=100, blank=True, null = True)
    freq2 = models.FloatField('Frecuencia (Hz)',max_length=100, blank=True, null = True)
    duration  = models.FloatField('Duración',max_length=100, blank=True, null = True)
    windopts  = models.CharField('Condiciones de Viento',max_length=100, blank=True, null = True)
    rainopts = models.CharField('Condiciones de Lluvia',max_length=100, blank=True, null = True)
    temperatura= models.DecimalField('Temperatura', null=True,blank=True, default =None, max_digits=8, decimal_places=2,)
    remarkstemp = models.CharField('Observaciones de temperatura',max_length=100, blank=True, null = True)
    groundtyp = models.CharField('Tipo de Suelo',max_length=100, blank=True, null = True)
    remarksgro = models.CharField('Observaciones de Tierra',max_length=100, blank=True, null = True)
    observations = models.TextField('Observaciones',max_length=100, blank=True, null = True)
    is_completed = models.BooleanField('Publicado',default=False)
    revisado= models.CharField('Revisado por',max_length=100, blank=True, null = True)
    nombre = models.CharField('Nombre de Archivo',max_length=100, blank=True, null = True)
    autor = models.CharField('Autor del archivo',max_length=100, blank=True, null = True)  
    medtype = models.CharField(max_length=100, blank=True, null = True)
    medición = models.DecimalField(null=True,blank=True, default =None, max_digits=8, decimal_places=2,)
    unidad = models.CharField(max_length=100, blank=True, null = True)
    clima= models.CharField('Clima',max_length=100, blank=True, null = True)
    Estruc= models.CharField('Estructura',max_length=100, blank=True, null = True)
    Traf= models.CharField('Trafico',max_length=100, blank=True, null = True)
    documento = models.FileField( upload_to='bitacora/', blank=True, null = False)
    dateNow=models.DateTimeField(default=now)

    author= models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.altitude,


class Registros(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_no = models.IntegerField(blank=True, null=True)
    centro = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    observaciones = models.TextField(max_length=100, blank=True, null = True)
    revisado = models.BooleanField('Revisado',default=False)


    
    def __str__(self):
        return str(self.user)

class BlogPost(models.Model):
    title=models.CharField('Titulo',max_length=255)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title')
    #content=models.TextField("Contenido")
    content = RichTextField('Contenido',null=True, blank=True)
    image = models.ImageField("Imagen",upload_to="profile_pics", blank=True, null=True)
    dateTime=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.author) +  " Blog Title: " + self.title
    
    #inv
    def get_absolute_url(self):
        return reverse('blogs')


    



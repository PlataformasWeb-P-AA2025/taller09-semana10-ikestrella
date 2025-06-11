from django.contrib import admin

# Register your models here.
from futbolec.models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class EquipoResource(resources.ModelResource):
    class Meta:
        model = Equipo
        exclude = ('user_name_twitter',)

class EquipoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = EquipoResource
    list_display = ('nombre', 'siglas', 'user_name_twitter')
    search_fields = ('nombre', 'siglas')

admin.site.register(Equipo, EquipoAdmin)




class JugadorResource(resources.ModelResource):
    class Meta:
        model = Jugador
        exclude = ('equipo',)

class JugadorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = JugadorResource
    list_display = ('nombre', 'posicion', 'numero_camiseta', 'sueldo', 'equipo_nombre')
    search_fields = ('nombre', 'posicion', 'numero_camiseta', 'equipo__nombre')
    def equipo_nombre(self, obj):
        return obj.equipo.nombre

admin.site.register(Jugador, JugadorAdmin)




class CampeonatoResource(resources.ModelResource):
    class Meta:
        model = Campeonato
        exclude = ('auspiciante',)
class CampeonatoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CampeonatoResource
    list_display = ('nombre', 'auspiciante')
    search_fields = ('nombre',)

admin.site.register(Campeonato, CampeonatoAdmin)





class CampeonatoEquiposResource(resources.ModelResource):
    class Meta:
        model = CampeonatoEquipos
        exclude = ('campeonato', 'equipo',)
class CampeonatoEquiposAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CampeonatoEquiposResource
    list_display = ('anio', 'campeonato_nombre', 'equipo_nombre')
    search_fields = ('anio', 'campeonato__nombre', 'equipo__nombre')
    
    def equipo_nombre(self, obj):
        return obj.equipo.nombre
    
    def campeonato_nombre(self, obj):
        return obj.equipo.nombre
    
admin.site.register(CampeonatoEquipos, CampeonatoEquiposAdmin)


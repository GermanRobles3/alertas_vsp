from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    path('login/',views.login),
    path('salir/',views.salir,name='salir'),
    path('', views.home,name='home'),

    #BROTES 
    path('brotes/', views.brotes,name='brotes'),   
    path('brotes/crearBrote/',views.crearBrote),   
    path('creacionBrote/',views.creacionBrote), 
    path('brotes/editarBrote/<id>',views.editarBrote),
    path('edicionBrote/<id>',views.edicionBrote),
    path('eliminarBrote/<id>',views.eliminarBrote),
    path('reporteBrotes/',views.reporteBrotes, name='reporteBrotes'), 

    #MEDIOS 
    path('medios/',views.medios,name="medios"),
    path('medios/crearMedio/',views.crearMedio), 
    path('creacionMedio/',views.creacionMedio),
    path('medios/editarMedio/<id>',views.editarMedio),
    path('edicionMedio/<id>',views.edicionMedio),
    path('medios/eliminarMedio/<id>',views.eliminarMedio),  
    path('reporteMedios/',views.reporteMedios, name='reporteMedios'),
    
    #SAT 
    path('alertas/',views.alertas,name="alertas"),
    path('alertas/crearAlerta/',views.crearAlerta), 
    path('creacionAlerta/',views.creacionAlerta),
    path('alertas/editarAlerta/<id>',views.editarAlerta),
    path('edicionAlerta/<id>',views.edicionAlerta),
    path('alertas/eliminarAlerta/<id>',views.eliminarAlerta),  
    path('reporteAlertas/',views.reporteAlertas, name='reporteAlertas'),

    #EVENTOS
    path('eventos',views.evento_home),
    path('crearEvento/',views.crearEvento),
    
]
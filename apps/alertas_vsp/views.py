from contextvars import copy_context
from django.shortcuts import redirect, render
from .models import Brote, Evento,Medio , Alerta
from django.http.response import HttpResponse
import pandas as pd
import sqlite3
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


#LOGIN---------------------------------------------
def login(request):
    #brotesListados= Brote.objects.all()
    #eventosListados= Evento.objects.all()
    return render(request,"login.html")
    #return render(request,"gestionalertas.html",{"brotes":brotesListados,"eventos":eventosListados})
#LOGOUT-----------------------------------------------
def salir(request):
    logout(request)
    return redirect('/')
#HOME-------------------------------------------------
@login_required
def home(request):
    brotesListados= Brote.objects.all()
    eventosListados= Evento.objects.all()
    return render(request,"brotes/brotes.html",{"brotes":brotesListados,"eventos":eventosListados})

#----------------------BROTES----------------------------------------------------------
#-------LISTAR BROTES---------
@login_required
def brotes(request):
    brotesListados= Brote.objects.all()
    eventosListados= Evento.objects.all()
    return render(request,"brotes/brotes.html",{"brotes":brotesListados,"eventos":eventosListados})

#------CREAR BROTES-------------
@login_required
def crearBrote(request):
    eventosListados= Evento.objects.all()
    return render(request, "brotes/crearBrote.html",{"eventos":eventosListados})

@login_required
def creacionBrote(request):
    profesional=request.POST['txtProfesional']
    fechaIngreso=request.POST['txtFechaIngreso']
    semana=request.POST['txtSemana']
    periodo=request.POST ['txtPeriodo'] 
    fechaOcurrencia=request.POST ['txtFechaOcurrencia']
    fechaNotificacion=request.POST ['txtFechaNotificacion']
    fuenteNotificacion=request.POST['optFuenteNotificacion']                  
    deptoOcurrencia=request.POST['optDeptoOcurrencia']
    municipioOcurrencia=request.POST['optMunOcurrencia']
    lugarOcurrencia=request.POST['txtLugarOcurrencia']
    direccion=request.POST['txtDireccion']
    situacionReportada=request.POST['optSituacionReportada']
    evento=request.POST['optEvento']
    grupoFuncional=request.POST['optGrupoFuncional']  
    poblacionAfectada=request.POST['optPoblacionAfectada']
    criterioRiesgo=request.POST['optCriterioRiesgo']     
    informeIec=request.POST['optInformeIec']
    fechaIec=request.POST['txtFechaIec']
    numeroContactos=request.POST['txtNumeroContactos']
    numeroEnfermos=request.POST['txtNumeroEnfermos']
    tasaAtaque=request.POST['txtTasaAtaque']
    numeroExpuestos=request.POST['txtNumeroExpuestos']
    numeroFallecidos=request.POST['txtNumeroFallecidos']
    muestras=request.POST ["optMuestras"]
    numeroMuestras=request.POST ['txtNumeroMuestras']
    fechaTomaMuestras=request.POST['txtFechaTomaMuestras']
    fechaEnvioMuestras=request.POST['txtFechaEnvioMuestras']
    tipoMuestra=request.POST['optTipoMuestra']
    decision=request.POST['optDecision']
    fechaEnvioIns=request.POST['txtFechaEnvioIns']
    seRealizaSar=request.POST['optSeRealizaSar']
    sitrep=request.POST['optSitrep']
    estado=request.POST['optEstado']
    fechaCierre=request.POST['txtFechaCierre']
    conclusion=request.POST['optConclusion']
    recomendacion=request.POST['optRecomendacion']
    seguimiento=request.POST ['txtSeguimiento']

    brote=Brote.objects.create(
    profesional=profesional,
    fecha_ingreso=fechaIngreso,
    semana=semana,
    periodo=periodo,
    fecha_ocurrencia=fechaOcurrencia,
    fecha_notificacion=fechaNotificacion,
    fuente_notificacion=fuenteNotificacion,
    depto_ocurrencia=deptoOcurrencia,
    mun_ocurrencia=municipioOcurrencia,
    lugar_ocurrencia=lugarOcurrencia,
    direccion=direccion,
    situacion_reportada=situacionReportada,
    evento=evento,
    grupo_funcional=grupoFuncional,
    poblacion_afectada=poblacionAfectada,
    criterio_riesgo=criterioRiesgo,
    informe_iec=informeIec,
    fecha_iec=fechaIec,
    numero_de_contactos=numeroContactos,
    numero_de_enfermos=numeroEnfermos,
    tasa_de_ataque=int(numeroContactos)/int(numeroEnfermos),
    numero_de_expuestos=numeroExpuestos,
    numero_de_fallecidos=numeroFallecidos,
    muestras=muestras,
    numero_de_muestras=numeroMuestras,
    fecha_toma_de_muestras=fechaTomaMuestras,
    fecha_envio_de_muestras=fechaEnvioMuestras,
    tipo_de_muestra=tipoMuestra,
    decision=decision,
    fecha_envio_al_ins=fechaEnvioIns,
    se_realiza_sar=seRealizaSar,
    sitrep=sitrep,
    estado=estado,
    fecha_de_cierre=fechaCierre,
    conclusion=conclusion,
    recomendacion=recomendacion,
    seguimiento=seguimiento)
    return redirect('/')

#-------------------EDITAR BROTES--------------------------------
@login_required
def editarBrote(request,id):
    brote=Brote.objects.get(id=id)
    eventosListados= Evento.objects.all()
    return render(request, "brotes/editarBrote2.html",{"brote":brote,"eventos":eventosListados})

@login_required
def edicionBrote(request,id):
    profesional=request.POST['txtProfesional']
    fechaIngreso=request.POST['txtFechaIngreso']
    semana=request.POST['txtSemana']
    periodo=request.POST ['txtPeriodo'] 
    fechaOcurrencia=request.POST ['txtFechaOcurrencia']
    fechaNotificacion=request.POST ['txtFechaNotificacion']
    fuenteNotificacion=request.POST['optFuenteNotificacion']                  
    deptoOcurrencia=request.POST['optDeptoOcurrencia']
    municipioOcurrencia=request.POST['optMunOcurrencia']
    lugarOcurrencia=request.POST['txtLugarOcurrencia']
    direccion=request.POST['txtDireccion']
    situacionReportada=request.POST['optSituacionReportada']
    evento=request.POST['optEvento']
    grupoFuncional=request.POST['optGrupoFuncional']  
    poblacionAfectada=request.POST['optPoblacionAfectada']
    criterioRiesgo=request.POST['optCriterioRiesgo']     
    informeIec=request.POST['optInformeIec']
    fechaIec=request.POST['txtFechaIec']
    numeroContactos=request.POST['txtNumeroContactos']
    numeroEnfermos=request.POST['txtNumeroEnfermos']
    tasaAtaque=request.POST['txtTasaAtaque']
    numeroExpuestos=request.POST['txtNumeroExpuestos']
    numeroFallecidos=request.POST['txtNumeroFallecidos']
    muestras=request.POST ["optMuestras"]
    numeroMuestras=request.POST ['txtNumeroMuestras']
    fechaTomaMuestras=request.POST['txtFechaTomaMuestras']
    fechaEnvioMuestras=request.POST['txtFechaEnvioMuestras']
    tipoMuestra=request.POST['optTipoMuestra']
    decision=request.POST['optDecision']
    fechaEnvioIns=request.POST['txtFechaEnvioIns']
    seRealizaSar=request.POST['optSeRealizaSar']
    sitrep=request.POST['optSitrep']
    estado=request.POST['optEstado']
    fechaCierre=request.POST['txtFechaCierre']
    conclusion=request.POST['optConclusion']
    recomendacion=request.POST['optRecomendacion']
    seguimiento=request.POST ['txtSeguimiento']

    brote=Brote.objects.get(id=id)
    brote.profesional=profesional
    brote.fecha_ingreso=fechaIngreso
    brote.semana=semana
    brote.periodo=periodo
    brote.fecha_ocurrencia=fechaOcurrencia
    brote.fecha_notificacion=fechaNotificacion
    brote.fuente_notificacion=  fuenteNotificacion              
    brote.depto_ocurrencia=deptoOcurrencia
    brote.mun_ocurrencia=municipioOcurrencia
    brote.lugar_ocurrencia=lugarOcurrencia
    brote.direccion=direccion
    brote.situacion_reportada=situacionReportada
    brote.evento=evento
    brote.grupo_funcional=grupoFuncional
    brote.poblacion_afectada=poblacionAfectada
    brote.criterio_riesgo=criterioRiesgo 
    brote.informe_iec=informeIec
    brote.fecha_iec=fechaIec
    brote.numero_de_contactos=numeroContactos
    brote.numero_de_enfermos=numeroEnfermos
    brote.tasa_de_ataque=tasaAtaque
    brote.numero_de_expuestos=numeroExpuestos
    brote.numero_de_fallecidos=numeroFallecidos
    brote.muestras=muestras
    brote.numero_de_muestras=numeroMuestras
    brote.fecha_toma_de_muestras=fechaTomaMuestras
    brote.fecha_envio_de_muestras=fechaEnvioMuestras
    brote.tipo_de_muestra=tipoMuestra
    brote.decision=decision
    brote.fecha_envio_al_ins=fechaEnvioIns
    brote.se_realiza_sar=seRealizaSar
    brote.sitrep=sitrep
    brote.estado=estado
    brote.fecha_de_cierre=fechaCierre
    brote.conclusion=conclusion
    brote.recomendacion=recomendacion
    brote.seguimiento=seguimiento
    brote.save()
    return redirect('/')
#-------------------ELIMINAR BROTES--------------------------
@login_required
def eliminarBrote(request, id):
    brote= Brote.objects.get(id=id)
    brote.delete()
    return redirect('/')
#--------------------REPORTE EN EXCEL BROTES-----------------------------
@login_required
def reporteBrotes(request):
    # Crea una conexión a la base de datos SQLite
    con = sqlite3.connect("C:/Users/Secretariavsp/Desktop/alertas/alertas.db")
    # Usa read_sql_query de pandas para extraer el resultado
    # de la consulta a un DataFrame
    df = pd.read_sql_query("SELECT * from alertas_vsp_brote", con)
    # Verifica que el resultado de la consulta SQL está
    # almacenado en el DataFrame
    print(df.head())
    # No te olvides de cerrar la conexión
    con.close()
    df1=df
    #df1 = pd.DataFrame({'a':[0,1,2], 'b':[1,2,3], 'c':[2,3,4]})
    df2 = pd.DataFrame({'aa':[10,11,12], 'bb':[11,12,13],'cc':[12,13,14]})

    #PARA GUARDAR EN EL PC
    #with pd.ExcelWriter('test.xlsx') as writer:
        #for i, df in enumerate([df1, df2]):
            #df.to_excel(writer,sheet_name=f'sheet_{i}', index=False)

    #PARA DESCARGAR EN EXCEL
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="ReporteBrotes.xlsx"'                                        
    df1.to_excel(response)
    return response
#----------------------EVENTOS----------------------------    

@login_required
def evento_home(request):
    eventosListados= Evento.objects.all()
    return render(request,"eventos/eventos.html",{"eventos":eventosListados})

@login_required
def crearEvento(request):
    codigo_evento=request.POST['txtCodigoEvento']
    nombre_evento=request.POST['txtNombreEvento']

    evento=Evento.objects.create(codigo_evento=codigo_evento,
    nombre_evento=nombre_evento)
    return redirect('/eventos')
   


#----------------------MEDIOS----------------------------------------------------------
#-------LISTAR MEDIOS---------
@login_required
def medios(request):
    mediosListados= Medio.objects.all()
    eventosListados= Evento.objects.all()
    return render(request,"medios/medios.html",{"medios":mediosListados,"eventos":eventosListados})

#------CREAR MEDIOS-------------
@login_required
def crearMedio(request):
    eventosListados= Evento.objects.all()
    return render(request, "medios/crearMedio.html",{"eventos":eventosListados})

@login_required
def creacionMedio(request):
    profesional=request.POST['txtProfesional']
    fechaIngreso=request.POST['txtFechaIngreso']
    semana=request.POST['txtSemana']
    periodo=request.POST ['txtPeriodo'] 
    tituloNoticia=request.POST['txtTituloNoticia']
    fechaOcurrencia=request.POST ['txtFechaOcurrencia'] 
    resumenNoticia=request.POST['txtResumenNoticia']   
    fuenteNotificacion=request.POST['optFuenteNotificacion'] 
    enlaceNoticia=request.POST['txtEnlaceNoticia']  
    
    evento=request.POST['optEvento']
    grupoFuncional=request.POST['optGrupoFuncional']  
    deptoOcurrencia=request.POST['optDeptoOcurrencia']
    municipioOcurrencia=request.POST['optMunOcurrencia']
        
    poblacionAfectada=request.POST['optPoblacionAfectada']
    criterioRiesgo=request.POST['optCriterioRiesgo']     
    confirmacion=request.POST['optConfirmacion']
    seguimiento=request.POST ['txtSeguimiento']

    medio=Medio.objects.create(
    profesional=profesional,
    fecha_ingreso=fechaIngreso,
    semana=semana,
    periodo=periodo,

    titulo_noticia=tituloNoticia,
    fecha_ocurrencia=fechaOcurrencia,
    resumen_noticia=resumenNoticia,
    fuente_notificacion=fuenteNotificacion,
    enlace_noticia=enlaceNoticia,

    evento=evento,
    grupo_funcional=grupoFuncional,
    depto_ocurrencia=deptoOcurrencia,
    mun_ocurrencia=municipioOcurrencia,
    
    poblacion_afectada=poblacionAfectada,
    criterio_riesgo=criterioRiesgo,
    confirmacion=confirmacion,
    seguimiento=seguimiento)
    return redirect('/medios')

#-------------------EDITAR MEDIOS--------------------------------
@login_required
def editarMedio(request,id):
    medio=Medio.objects.get(id=id)
    eventosListados= Evento.objects.all()
    return render(request, "medios/editarMedio.html",{"medio":medio,"eventos":eventosListados})

@login_required
def edicionMedio(request,id):
    profesional=request.POST['txtProfesional']
    fechaIngreso=request.POST['txtFechaIngreso']
    semana=request.POST['txtSemana']
    periodo=request.POST ['txtPeriodo'] 
    tituloNoticia=request.POST['txtTituloNoticia']
    fechaOcurrencia=request.POST ['txtFechaOcurrencia'] 
    resumenNoticia=request.POST['txtResumenNoticia']   
    fuenteNotificacion=request.POST['optFuenteNotificacion'] 
    enlaceNoticia=request.POST['txtEnlaceNoticia']  
    
    evento=request.POST['optEvento']
    grupoFuncional=request.POST['optGrupoFuncional']  
    deptoOcurrencia=request.POST['optDeptoOcurrencia']
    municipioOcurrencia=request.POST['optMunOcurrencia']
        
    poblacionAfectada=request.POST['optPoblacionAfectada']
    criterioRiesgo=request.POST['optCriterioRiesgo']     
    confirmacion=request.POST['optConfirmacion']
    seguimiento=request.POST ['txtSeguimiento']

    medio=Medio.objects.get(id=id)
    medio.profesional=profesional
    medio.fecha_ingreso=fechaIngreso
    medio.semana=semana
    medio.periodo=periodo

    medio.titulo_noticia=tituloNoticia
    medio.fecha_ocurrencia=fechaOcurrencia
    medio.resumen_noticia=resumenNoticia
    medio.fuente_notificacion=fuenteNotificacion
    medio.enlace_noticia=enlaceNoticia

    medio.evento=evento
    medio.grupo_funcional=grupoFuncional
    medio.depto_ocurrencia=deptoOcurrencia
    medio.mun_ocurrencia=municipioOcurrencia
    
    medio.poblacion_afectada=poblacionAfectada
    medio.criterio_riesgo=criterioRiesgo
    medio.confirmacion=confirmacion
    medio.seguimiento=seguimiento
    medio.save()
    return redirect('/medios')
#-------------------ELIMINAR MEDIOS --------------------------
@login_required
def eliminarMedio(request, id):
    medio= Medio.objects.get(id=id)
    medio.delete()
    return redirect('/medios')
#--------------------REPORTE EN EXCEL MEDIOS-----------------------------
@login_required
def reporteMedios(request):
    # Crea una conexión a la base de datos SQLite
    con = sqlite3.connect("C:/Users/Secretariavsp/Desktop/alertas/alertas.db")
    # Usa read_sql_query de pandas para extraer el resultado
    # de la consulta a un DataFrame
    df = pd.read_sql_query("SELECT * from alertas_vsp_medio", con)
    # Verifica que el resultado de la consulta SQL está
    # almacenado en el DataFrame
    print(df.head())
    # No te olvides de cerrar la conexión
    con.close()
    df1=df
   
    df2 = pd.DataFrame({'aa':[10,11,12], 'bb':[11,12,13],'cc':[12,13,14]})



    #PARA DESCARGAR EN EXCEL
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="ReporteMedios.xlsx"'                                        
    df1.to_excel(response)
    return response




















































#----------------------ALERTAS----------------------------------------------------------
#-------LISTAR Alertas---------

@login_required
def alertas(request):
    alertasListadas= Alerta.objects.all()
    eventosListados= Evento.objects.all()
    return render(request,"alertas/alertas.html",{"alertas":alertasListadas,"eventos":eventosListados})
#------CREAR alertaS-------------
@login_required
def crearAlerta(request):
    eventosListados= Evento.objects.all()
    return render(request, "alertas/crearAlerta.html",{"eventos":eventosListados})

@login_required
def creacionAlerta(request):
    profesional=request.POST['txtProfesional']
    year=request.POST['txtYear']
    deptoOcurrencia=request.POST['optDeptoOcurrencia']
    evento=request.POST['optEvento']
    fechaIngreso=request.POST['txtFechaIngreso']
    fuenteNotificacion=request.POST['optFuenteNotificacion'] 
    municipioOcurrencia=request.POST['optMunOcurrencia']
    numero=request.POST['txtNumero']
    numeroSituaciones=request.POST['txtNumeroSituaciones']
    referencia=request.POST['txtReferencia']  
    seguimiento=request.POST ['txtSeguimiento']
    situacionReportada=request.POST['optSituacionReportada']
    url=request.POST['txtUrl']
    archivosAdjuntos=request.POST['fileAlerta']

    alerta=Alerta.objects.create(
    profesional=profesional,
    year=year,
    depto_ocurrencia=deptoOcurrencia,
    evento=evento,
    fecha_ingreso=fechaIngreso,
    fuente_notificacion=fuenteNotificacion,
    mun_ocurrencia=municipioOcurrencia,
    numero=numero,
    numero_situaciones=numeroSituaciones,
    referencia=referencia,
    seguimiento=seguimiento,
    situacion_reportada=situacionReportada,
    url=url,
    archivos_adjuntos=archivosAdjuntos)
    return redirect('/alertas')

#-------------------EDITAR alertaS--------------------------------

@login_required
def editarAlerta(request,id):
    alerta=Alerta.objects.get(id=id)
    eventosListados= Evento.objects.all()
    return render(request, "alertas/editarAlerta.html",{"alerta":alerta,"eventos":eventosListados})

@login_required
def edicionAlerta(request,id):
    profesional=request.POST['txtProfesional']
    year=request.POST['txtYear']
    deptoOcurrencia=request.POST['optDeptoOcurrencia']
    evento=request.POST['optEvento']
    fechaIngreso=request.POST['txtFechaIngreso']
    fuenteNotificacion=request.POST['optFuenteNotificacion'] 
    municipioOcurrencia=request.POST['optMunOcurrencia']
    numero=request.POST['txtNumero']
    numeroSituaciones=request.POST['txtNumeroSituaciones']
    referencia=request.POST['txtReferencia']  
    seguimiento=request.POST ['txtSeguimiento']
    situacionReportada=request.POST['optSituacionReportada']
    url=request.POST['txtUrl']
    archivosAdjuntos=request.POST['fileAlerta']

    alerta=Alerta.objects.get(id=id)
    alerta.profesional=profesional
    alerta.year=year
    alerta.depto_ocurrencia=deptoOcurrencia
    alerta.evento=evento
    alerta.fecha_ingreso=fechaIngreso
    alerta.fuente_notificacion=fuenteNotificacion
    alerta.mun_ocurrencia=municipioOcurrencia
    alerta.numero=numero
    alerta.numero_situaciones=numeroSituaciones
    alerta.referencia=referencia
    alerta.seguimiento=seguimiento
    alerta.situacion_reportada=situacionReportada
    alerta.url=url
    alerta.archivos_adjuntos=archivosAdjuntos
    alerta.save()
    return redirect('/alertas')
#-------------------ELIMINAR alertaS --------------------------
@login_required
def eliminarAlerta(request, id):
    alerta= Alerta.objects.get(id=id)
    alerta.delete()
    return redirect('/alertas')
#--------------------REPORTE EN EXCEL alertaS-----------------------------
@login_required
def reporteAlertas(request):
    # Crea una conexión a la base de datos SQLite
    con = sqlite3.connect("C:/Users/Secretariavsp/Desktop/alertas/alertas.db")
    # Usa read_sql_query de pandas para extraer el resultado
    # de la consulta a un DataFrame
    df = pd.read_sql_query("SELECT * from alertas_vsp_alerta", con)
    # Verifica que el resultado de la consulta SQL está
    # almacenado en el DataFrame
    print(df.head())
    # No te olvides de cerrar la conexión
    con.close()
    df1=df
   
    df2 = pd.DataFrame({'aa':[10,11,12], 'bb':[11,12,13],'cc':[12,13,14]})



    #PARA DESCARGAR EN EXCEL
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="ReporteAlertas.xlsx"'                                        
    df1.to_excel(response)
    return response


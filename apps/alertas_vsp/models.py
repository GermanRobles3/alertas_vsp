from django.db import models

# Create your models here.

class Brote(models.Model):
    profesional=models.CharField(max_length=50) #ENITH,  YONEIRA
    fecha_ingreso=models.DateField()
    semana=models.IntegerField()
    periodo=models.IntegerField()
    fecha_ocurrencia=models.DateField()
    fecha_notificacion=models.DateField()
    fuente_notificacion=models.CharField(max_length=50) #centro nacional de enlace, comunidad, externa a salud publica, externas al programa de vigilancia, instituto nacional de salud, laboratorio de salud publica departamental, monitoreo de medios, secretaria de salud municipal,sivigila
    depto_ocurrencia=models.CharField(max_length=50)
    mun_ocurrencia=models.CharField(max_length=50)
    lugar_ocurrencia=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    situacion_reportada=models.CharField(max_length=50) #Alerta medios, alertas, brote, brote eta, caso, conglomerado, foco, noticia o rumor, otro
    evento=models.CharField(max_length=50)
    grupo_funcional=models.CharField(max_length=50) #Laboratorio de salud publica departamental, programa ampliado de inmunizaciones, programa ira, programa maternidad segura, programa salud ambiental,programa vectores, programa zoonosis, vigilancia en salud publica
    poblacion_afectada=models.CharField(max_length=50) #centro de proteccion, comunidad en general, FM-militares, IPS-instituciones prestadoras de salud, min poblacion minera, otros,PE- poblacion escolarizada, PI- poblacion indigena, PM- poblacion migrante, PN- policia, PPL-Poblacion privada de la libertad
    criterio_riesgo=models.CharField(max_length=50) #Gobernanza, poblacion intrahospitalaria, poblaciones especiales, reglamento sanitario internacional - EISP, situacion con afectacion al personal sanitario, situacion con muertes, situacion con riesgo reputacional
    informe_iec=models.CharField(max_length=5) #si No
    fecha_iec=models.DateField()
    numero_de_contactos=models.IntegerField()
    numero_de_enfermos=models.IntegerField()
    tasa_de_ataque=models.IntegerField()
    numero_de_expuestos=models.IntegerField()
    numero_de_fallecidos=models.IntegerField()
    muestras=models.CharField(max_length=10) #Si, no , no aplica
    numero_de_muestras=models.IntegerField()
    fecha_toma_de_muestras=models.DateField()
    fecha_envio_de_muestras=models.DateField()
    tipo_de_muestra=models.CharField(max_length=50) #Alimentos, ambiental, animal, humana, humana-alimento, humana-ambiental, humana-superficie, no aplica, sin muestra
    decision=models.CharField(max_length=50) #Cerrado sar, cerrado sar cerrado GGRRI referente,seguimiento GGRRI, seguimiento por el referente del evento, seguimiento referente y GGRRI, seguimiento SAR
    fecha_envio_al_ins=models.DateField()
    se_realiza_sar=models.CharField(max_length=50)#sar departamental, sar municipal, sar nacional, no
    sitrep=models.CharField(max_length=20) #si, no, no aplica
    estado=models.CharField(max_length=20) #abierto, cerrado
    fecha_de_cierre=models.DateField()
    conclusion=models.CharField(max_length=20) #espii, espil, espin, espir,ninguna
    recomendacion=models.CharField(max_length=50) #cierre, referente, sar, trabajo conjunto con referente
    seguimiento=models.CharField(max_length=200)

    def __str__(self):
        texto="{0}-{1}({2})"
        return texto.format(self.evento,self.mun_ocurrencia,self.fecha_ocurrencia)

    

class Evento(models.Model):
    codigo_evento=models.CharField(primary_key=True,max_length=6)
    nombre_evento=models.CharField(max_length=250)

    def __str__(self):
        texto="{0}-{1}"
        return texto.format(self.codigo_evento,self.nombre_evento)
   


class Medio(models.Model):
    profesional=models.CharField(max_length=50) #ENITH,  YONEIRA
    fecha_ingreso=models.DateField()
    semana=models.IntegerField()
    periodo=models.IntegerField()
    #------------------------------------------
    titulo_noticia=models.CharField(max_length=200)
    fecha_ocurrencia=models.DateField()
    resumen_noticia=models.CharField(max_length=1000)
    fuente_notificacion=models.CharField(max_length=50) #centro nacional de enlace, comunidad, externa a salud publica, externas al programa de vigilancia, instituto nacional de salud, laboratorio de salud publica departamental, monitoreo de medios, secretaria de salud municipal,sivigila
    enlace_noticia=models.CharField(max_length=200)
    #------------------------------------------
    evento=models.CharField(max_length=50)
    grupo_funcional=models.CharField(max_length=50) #Laboratorio de salud publica departamental, programa ampliado de inmunizaciones, programa ira, programa maternidad segura, programa salud ambiental,programa vectores, programa zoonosis, vigilancia en salud publica
    depto_ocurrencia=models.CharField(max_length=50)
    mun_ocurrencia=models.CharField(max_length=50)    
    poblacion_afectada=models.CharField(max_length=50) #centro de proteccion, comunidad en general, FM-militares, IPS-instituciones prestadoras de salud, min poblacion minera, otros,PE- poblacion escolarizada, PI- poblacion indigena, PM- poblacion migrante, PN- policia, PPL-Poblacion privada de la libertad
    criterio_riesgo=models.CharField(max_length=50) #Gobernanza, poblacion intrahospitalaria, poblaciones especiales, reglamento sanitario internacional - EISP, situacion con afectacion al personal sanitario, situacion con muertes, situacion con riesgo reputacional   
    confirmacion=models.CharField(max_length=5) #si No
    seguimiento=models.CharField(max_length=200)

    def __str__(self):
        texto="{0}-{1}({2})"
        return texto.format(self.evento,self.mun_ocurrencia,self.fecha_ocurrencia)

class Alerta(models.Model):
    profesional=models.CharField(max_length=50) #ENITH,YONEIRA
    year=models.IntegerField()
    depto_ocurrencia=models.CharField(max_length=50)
    evento=models.CharField(max_length=50)
    fecha_ingreso=models.DateField()
    fuente_notificacion=models.CharField(max_length=50) #centro nacional de enlace, comunidad, externa a salud publica, externas al programa de vigilancia, instituto nacional de salud, laboratorio de salud publica departamental, monitoreo de medios, secretaria de salud municipal,sivigila
    mun_ocurrencia=models.CharField(max_length=50)
    numero=models.IntegerField()
    numero_situaciones=models.IntegerField()
    referencia=models.CharField(max_length=50)
    seguimiento=models.CharField(max_length=200)
    situacion_reportada=models.CharField(max_length=50) #Alerta medios, alertas, brote, brote eta, caso, conglomerado, foco, noticia o rumor, otro
    url=models.CharField(max_length=50)
    archivos_adjuntos=models.CharField(max_length=50) 
        
    def __str__(self):
            texto="{0}-{1}({2})"
            return texto.format(self.evento,self.mun_ocurrencia,self.fecha_ingreso)
        

    
    
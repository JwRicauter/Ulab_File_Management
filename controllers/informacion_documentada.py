###################################################################################
##																				 ##
##		Controladores del módulo de información documentada 					 ##
##																				 ##
## 			» Andre Corcuera													 ##
## 			» Angel Morante														 ##
##			» Jawil Ricauter													 ##
## 			» Jonathan Bandes													 ##
## 			» Nairelys Hernandez												 ##
## 			» Rosana Garcia														 ##
##																				 ##
###################################################################################


import time
import datetime

## Pagina de Inicio del modulo de Gestion de Informacion Documentada
def index(): 
	return dict(message="hello from informacion_documentada.py")


@auth.requires_login(otherwise=URL('modulos', 'login'))
def lista_documentos():


	if auth.has_membership("WEBMASTER") or auth.has_membership("DIRECTOR") or auth.user.email=='ulab-calidad@usb.ve':
		documentos = db().select(db.documentos.ALL)
	else:
		print (auth.user.first_name=='Unidad de Administración')
		documentos = db(db.documentos.responsable==auth.user.first_name).select()

	unaDependencia = request.post_vars.codigo
		
	dic = {

		##### Planificación
		"usuario":auth.user.first_name,
		"nombre_doc": request.post_vars.nombre_documento,
		"tipo_doc":request.post_vars.tipo,
		"responsable": request.post_vars.responsable,

		##### Elaboración
		"codigo": unaDependencia,
		"objetivo": request.post_vars.objetivos,
		"periodo_rev":request.post_vars.periodo,
		"fecha_prox_rev": request.post_vars.fecha_prox_rev,
		"anexo_code1": request.post_vars.anexo_code1,
		"anexo_name1": request.post_vars.anexo_name1,
		"anexo_code2": request.post_vars.anexo_code2,
		"anexo_name2": request.post_vars.anexo_name2,
		"anexo_code3": request.post_vars.anexo_code3,
		"anexo_name3": request.post_vars.anexo_name3,
		"anexo_code4": request.post_vars.anexo_code4,
		"anexo_name4": request.post_vars.anexo_name4,
		"anexo_code5": request.post_vars.anexo_code5,
		"anexo_name5": request.post_vars.anexo_name5,
		"elaborado1": request.post_vars.elaborado1,
		"elaborado2": request.post_vars.elaborado2,
		"elaborado3": request.post_vars.elaborado3,
		"elaborado4": request.post_vars.elaborado4,
		"elaborado5": request.post_vars.elaborado5,


		##### Revisión
		"rev_contenido_realizado_por": request.post_vars.revision_contenido,
		"fecha_rev_contenido": request.post_vars.fecha_revision_contenidos,
		"rev_especficaciones_doc_realizado_por": request.post_vars.revision_especificaciones,		
		"fecha_rev_especificaciones_doc":  request.post_vars.fecha_revision_especificaciones,
		"fecha_rev_por_consejo_asesor": request.post_vars.fecha_revision_consejo,


		##### Aprobación
		"aprobado_por": request.post_vars.aprobado,
		"fecha_aprob": request.post_vars.fechaAprobacion,
		"cod_aprob": request.post_vars.cod_registro,
		"ubicacion_fisica": request.post_vars.ubicacion_fisica,
		"ubicacion_electronica": request.post_vars.ubicacion_electronica,
		"cod_control_cambio": request.post_vars.cod_control_cambio,
		"fecha_control_cambio": request.post_vars.fecha_control_cambio,
		"ccelaborado": request.post_vars.ccelaborado,
		"registro_fisico": request.post_vars.registro_fisico,
		"registro_electronico": request.post_vars.registro_electronico,

		##### Estatus inicial
		"estatus":"Planificado"
			
		
	}



	planificado = {
		"tipo_doc": dic["tipo_doc"]=='',
		"responsable":dic["responsable"],
		"nombre_doc":dic["nombre_doc"]
	}

	elaborado = { 
		"codigo": dic["codigo"],
		"objetivo": dic["objetivo"],
		"periodo_rev": dic["periodo_rev"],
		"fecha_prox_rev": dic["fecha_prox_rev"]
	}

	revisado = {
		"rev_contenido_realizado_por":dic["rev_contenido_realizado_por"],
		"fecha_rev_contenido":dic["fecha_rev_contenido"],
		"rev_especficaciones_doc_realizado_por":dic["rev_especficaciones_doc_realizado_por"],
		"fecha_rev_especificaciones_doc":dic["fecha_rev_especificaciones_doc"],
		"fecha_rev_por_consejo_asesor":dic["fecha_rev_por_consejo_asesor"],
	}

	aprobado = {
		"aprobado_por":dic["aprobado_por"],
		"fecha_aprob":dic["fecha_aprob"],
		"cod_aprob":dic["cod_aprob"],
	}


	if(not('' in elaborado.values())):
		dic["estatus"] = "Elaborado"

	if(not('' in revisado.values())):
		dic["estatus"] = "Revisado"

	if(not('' in aprobado.values())):
		dic["estatus"] = "Aprobado"


	##### Agregamos el documento
	if(dic["codigo"]!=None):
		db.documentos.insert(

			usuario=dic["usuario"],
			nombre_doc=dic["nombre_doc"],
			tipo_doc=dic["tipo_doc"],
			responsable=dic["responsable"],
			codigo=dic["codigo"],
			objetivo=dic["objetivo"],
			periodo_rev=dic["periodo_rev"],
			fecha_prox_rev=dic["fecha_prox_rev"],
			anexo_code1=dic["anexo_code1"],
			anexo_name1=dic["anexo_name1"],
			anexo_code2=dic["anexo_code2"],
			anexo_name2=dic["anexo_name2"],
			anexo_code3=dic["anexo_code3"],
			anexo_name3=dic["anexo_name3"],
			anexo_code4=dic["anexo_code4"],
			anexo_name4=dic["anexo_name4"],						
			anexo_code5=dic["anexo_code5"],
			anexo_name5=dic["anexo_name5"],
			elaborado1=dic["elaborado1"],
			elaborado2=dic["elaborado2"],
			elaborado3=dic["elaborado3"],
			elaborado4=dic["elaborado4"],
			elaborado5=dic["elaborado5"],
			rev_contenido_realizado_por=dic["rev_contenido_realizado_por"],
			fecha_rev_contenido=dic["fecha_rev_contenido"],
			rev_especficaciones_doc_realizado_por=dic["rev_especficaciones_doc_realizado_por"],
			fecha_rev_especificaciones_doc=dic["fecha_rev_especificaciones_doc"],
			fecha_rev_por_consejo_asesor=dic["fecha_rev_por_consejo_asesor"],
			aprobado_por=dic["aprobado_por"],
			fecha_aprob=dic["fecha_aprob"],
			cod_aprob=dic["cod_aprob"],
			ubicacion_fisica=dic["ubicacion_fisica"],
			ubicacion_electronica=dic["ubicacion_electronica"],
			cod_control_cambio=dic["cod_control_cambio"],
			fecha_control_cambio=dic["fecha_control_cambio"],
			ccelaborado=dic["ccelaborado"],
			registro_fisico=dic["registro_fisico"],
			registro_electronico=dic["registro_electronico"],
			estatus=dic["estatus"]
			
		
		)

		# strings = time.strftime("%Y,%m,%d,%H,%M,%S")
		# t = strings.split(',')
		# year = t[0]
		# year = year[2:]
		# fecha = t[2] + "/" + t[1] + "/" + t[0]
		# contador = db(db.registros.usuario == auth.user.first_name).count(),

		# contador = contador[0]
		# contador = int(contador) + 1
		# if (contador < 10):
		# 	contador = "00" + str(contador)
		# elif (contador < 100):
		# 	contador = "0" + str(contador)
		# else:
		# 	contador = str(contador) 		

		# print(unaDependencia)
		# print(year)
		# cod = unaDependencia[:3] + "/" + year + "-" + contador

		# dic2 = {
		# 	"usuario":auth.user.first_name,
		# 	"codigo": cod,
		# 	"remitente": auth.user.first_name
		# }


		# if(dic2["remitente"]!=None):
		# 	db.registros.insert(
		# 		usuario=dic2["usuario"],
		# 		codigo=dic2["codigo"],
		# 		remitente=dic2["remitente"]
		# 	)




	return dict(
	    documentos=db().select(db.documentos.ALL),
		doc_aprobado=db(db.documentos.estatus=="Aprobado").count(),
		doc_revision=db(db.documentos.estatus=="Revisado").count(),
		doc_elaboracion=db(db.documentos.estatus=="Elaborado").count(),
		doc_planificacion=db(db.documentos.estatus=="Planificado").count(),
		dependencias = db().select(db.dependencias.nombre, db.dependencias.codigo_registro),
		usuarios = db().select(db.auth_user.first_name)
	)






@auth.requires_login(otherwise=URL('modulos', 'login'))
def lista_registros():

	# strings = time.strftime("%Y,%m,%d,%H,%M,%S")
	# t = strings.split(',')
	# year = t[0]
	# year = year[2:]

	dic = {
		"usuario":auth.user.first_name,
		"codigo": request.post_vars.codigo,
		"fecha_creacion": request.post_vars.fecha_creacion,
		"descripcion": request.post_vars.descripcion,
		"destinatario": request.post_vars.destinatario,
		"remitente": request.post_vars.remitente,
		"doc_electronico": request.post_vars.doc_electronico,
		"archivo_fisico": request.post_vars.archivo_fisico,
	}


	if(dic["descripcion"]!=None):
		db.registros.insert(
			usuario=dic["usuario"],
			codigo=dic["codigo"],
			fecha_creacion=dic["fecha_creacion"],
			descripcion=dic["descripcion"],
			destinatario=dic["destinatario"],
			remitente=dic["remitente"],
			doc_electronico=dic["doc_electronico"],
			archivo_fisico=dic["archivo_fisico"],
		)


	a = dict(
	    registros=db().select(db.registros.ALL),
	    codigo_reg=db(db.registros.codigo).count(),
	    #year=year,
		contador=db(db.registros.usuario == auth.user.first_name).count(),
		dependencias = db().select(db.dependencias.nombre, db.dependencias.codigo_registro),
	)

	return a





def ficha_reg():
	print(request.args[0])
	uname = request.args[0]
	row = db(db.documentos.codigo==uname).select()


	dic = {
	"codigo": request.post_vars.codigo,
	"fecha_creacion": request.post_vars.fecha_creacion,
	"descripcion": request.post_vars.descripcion,
	"destinatario": request.post_vars.destinatario,
	"remitente": request.post_vars.remitente,
	"doc_electronico": request.post_vars.doc_electronico,
	"archivo_fisico": request.post_vars.archivo_fisico,
	}

	registro =  db(db.registros.codigo==uname)

	if(request.post_vars.eliminar=="eliminar"):
		db(db.registros.codigo==uname).delete()
		redirect(URL('..', 'sigulab2','informacion_documentada',''))

	### END ###
	return dict(message=row	)


	
def ficha():

	uname = request.args[0]
	row = db(db.documentos.codigo==uname).select()



	documento =  db(db.documentos.codigo==uname)

	# 	documento.update(

	# 			objetivo=dic["objetivo"],
	# 			ubicacion_electronica=dic["ubicacion_electronica"],
	# 			ubicacion_fisica=dic["ubicacion_fisica"],
	# 			# cod_anexo=dic["cod_anexo"],
	# 			# nombre_anexo=dic["nombre_anexo"],
	# 			#responsable=dic["responsable"],
	# 			nombre_doc=dic["nombre_doc"],
	# 			#estatus=dic["estatus"],
	# 			periodo_rev=dic["periodo_rev"],
	# 			aprobado_por=dic["aprobado_por"],
	# 			elaborado_actualizado_por=dic["elaborado_actualizado_por"],

	# 			fecha_aprob=dic["fecha_aprob"],
	# 			fecha_prox_rev=dic["fecha_prox_rev"],
	# 			fecha_control_cambio=dic["fecha_control_cambio"],
	# 			cod_control_cambio=dic["cod_control_cambio"],
	# 			cod_aprob=dic["cod_aprob"],
	# 			fecha_rev_por_consejo_asesor=dic["fecha_rev_por_consejo_asesor"],
	# 			rev_por_consejo_asesor=dic["rev_por_consejo_asesor"],
	# 			fecha_rev_especificaciones_doc=dic["fecha_rev_especificaciones_doc"],
	# 			fecha_rev_contenido=dic["fecha_rev_contenido"],
	# 			rev_especficaciones_doc_realizado_por=dic["rev_especficaciones_doc_realizado_por"],
	# 			rev_contenido_realizado_por=dic["rev_contenido_realizado_por"],
	# 			tipo_doc= dic["tipo_doc"],
	# 		)
	# if(request.post_vars.eliminar=="eliminar"):
	# 	db(db.documentos.codigo==uname).delete()
	# 	redirect(URL('..', 'sigulab2','informacion_documentada',''))

	### END ###
	if(request.post_vars.elaborado=="edicion"):

		documento.update(estatus="Elaborado",
			periodo_rev=request.post_vars.periodo,
			objetivo=request.post_vars.objetivos,
			fecha_prox_rev= request.post_vars.fecha_prox_rev 
		)
	elif (request.post_vars.revisado=="revisado"):

		print("revisado")
		documento.update(estatus="Revisado",
			periodo_rev=request.post_vars.periodo,
			objetivo=request.post_vars.objetivos,
			fecha_prox_rev= request.post_vars.fecha_prox_rev,
			rev_contenido_realizado_por = request.post_vars.revision_contenido,
        	fecha_rev_contenido = request.post_vars.fecha_revision_contenidos,
        	rev_especficaciones_doc_realizado_por = request.post_vars.revision_especificaciones,
       		fecha_rev_especificaciones_doc = request.post_vars.fecha_revision_especificaciones,
       		rev_por_consejo_asesor = request.post_vars.revision_consejo,
       		fecha_rev_por_consejo_asesor = 	request.post_vars.fecha_revision_consejo)
	elif(request.post_vars.aprobado=="aprobado"):
		print("aprobado")
		documento.update(estatus="Revisado",
			periodo_rev=request.post_vars.periodo,
			objetivo=request.post_vars.objetivos,
			fecha_prox_rev= request.post_vars.fecha_prox_rev,
			rev_contenido_realizado_por = request.post_vars.revision_contenido,
        	fecha_rev_contenido = request.post_vars.fecha_revision_contenidos,
        	rev_especficaciones_doc_realizado_por = request.post_vars.revision_especificaciones,
       		fecha_rev_especificaciones_doc = request.post_vars.fecha_revision_especificaciones,
       		rev_por_consejo_asesor = request.post_vars.revision_consejo,
       		fecha_rev_por_consejo_asesor = 	request.post_vars.fecha_revision_consejo,
       		aprobado_por = request.post_vars.aprobado,
        	fecha_aprob = request.post_vars.fechaAprobacion,
        	cod_aprob = request.post_vars.cod_registro,
        	cod_control_cambio = request.post_vars.cod_controlCambios,
        	fecha_control_cambio = request.post_vars.fechaControlCambios,
        	ubicacion_fisica = request.post_vars.ubicacion_fisica,
        	ubicacion_electronica = request.post_vars.ubicacion_electronica
        )###
	if(request.post_vars.eliminar=="eliminar"):
		db(db.documentos.codigo==uname).delete()
		redirect(URL('lista_documentos'))



	return dict(documentos=row,
				dependencias = db().select(db.dependencias.nombre, db.dependencias.codigo_registro)) #row	)

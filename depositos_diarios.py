# -*- coding: utf-8 -*-
"""DEPOSITOS_DIARIOS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14pz7G3wS5faQWYKI9JnKSKP9eQnU2rbx

# Elaboración de los Depósitos Diarios
Esta extración se hace a cada pdf reporte reenviado por la Superintendencia.

* Asegurarse que los archivos estén guardados en el directorio.

* Los datos extraídos se almacenarán en la nube de Google Drive en el correspondiente formato de GoogleSheet.
"""
# %%
#from google.colab import drive
#drive.mount('/content/drive', force_remount=True)

# %%
#!pip install pygsheets
#!pip install tabula-py==1.4.3
#!pip install tabula-py

# %%
########################################################
#########################################################
########################################################
# Definiendo parámetros
#          https://docs.google.com/spreadsheets/d/169gGlDXYPoJEoAudZXo-PdIX1z2i9DFBhyZMFAwwzD8/edit?usp=sharing
## Ubicación de los cuadros
    ## area1 = Depósitos en Córdobas
#area1 = [183.218,9.563,261.248,600.908]   #Activar si contiene a Bancorp solo informativo
#area1 = [187.043,15.683,284.198,597.848]  #Activar si no hay Bancorp 
#area1 = [184.748,10.328,248.243,606.263]  #Activar si no hay Avanz
#area1 = [184.748,12.623,249.008,603.968]   #Tabla deforme
#area1 = [184.748, 12.623, 262.013, 607.793]   #Tabla deforme
area1 = [183.983,11.858,272.723,596.318]   #Tabla con Banco Atlántida
cols1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # Definiendo columnas
#cols1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # Definiendo columnas en deforme


    ## area1 = Depósitos en Dólares
#area2 = [356.873,11.858,432.608,600.908]   #Activar si contiene a Bancorp solo informativo
#area2 = [346.928,14.153,441.788,597.848]  #Activar si no hay Bancorp
#area2 = [333.158,12.623,396.653,602.438]  #Activar si no hay Avanz
#area2 = [345.398,12.623,408.12,8,604.733]   #Tabla deforme
#area2 = [356.873, 11.858, 432.608, 607.793]   #Tabla deforme
area2 = [356.108,12.623,444.848,599.378]   #Tabla con Banco Atlántida
cols2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # Definiendo columnas
#cols2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Definiendo columnas en deforme


    ## area1 = Depósitos Consolidados
#area3 = [528.233,11.858,603.968,599.378]   #Activar si contiene a Bancorp solo informativo
#area3 = [506.813,14.153,602.438,597.083]  #Activar si no hay Bancorp
#area3 = [480.038,11.093,545.063,605.498]  #Activar si no hay Avanz
#area3 = [504.518,12.623,567.248,600.908]   #Tabla deforme
#area3 = [528.233, 11.858, 604.733, 601.673]   #Tabla deforme
area3 = [528.233,11.093,616.208,597.848]   #Tabla con Banco Atlántida
cols3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # Definiendo columnas
#cols3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # Definiendo columnas en deforme


## Cantidades de Bancos -1 por la enumeración de Python.
#instituciones = ["BANPRO", "LAFISE", "BAC", "BDF", "FICOHSA", "AVANZ", "BANCORP"] # Con Bancorp
#instituciones = ["BANPRO", "LAFISE", "BAC", "BDF", "FICOHSA", "AVANZ"] # Sin Bancorp
instituciones = ["BANPRO", "LAFISE", "BAC", "BDF", "FICOHSA", "AVANZ", "ATLANTIDA"] # Con Atlántida


#canti = '0:%s' % (len(instituciones)-1)
canti = len(instituciones)-1

## PDF, la dirección de ubicación
#pdf = r'C:\Users\Deybi.Morales\Google Drive\Depositos_diarios_reportes\Reporte Diario Depositos y Liquidez FOGADE-es-ni_161119.pdf'
##pdf = '/content/drive/My Drive/Depositos_diarios_reportes/Reporte Diario Depositos y Liquidez FOGADE-es-ni_080920.pdf'
pdf = "https://drive.google.com/uc?id=18Bg6gST9sFBhCtyV5opmXEby5utaccDt"

import urllib.request

url = pdf

archivo_tmp, header = urllib.request.urlretrieve(url)

with open('C:/Users/JENNY/Desktop/BORRAR HOY/Hackers-finanzas/data_07082020/prueba.pdf', 'wb') as archivo:
     with open(archivo_tmp, 'rb') as tmp:
         archivo.write(tmp.read())



## Nombre del GoogleSheets en Google drive
googleSheet = "DEPOSITOSDIARIOS"

## Tipo de Cambio de la fecha
TIPO = 34.5338
 
FECHA = '08/09/2020' #domingo de octubre 19

## Linea que completar en GoogleSheets
linea = 665
#####################################################################
####################################################################################
####################################################################################

## Depósitos al cierre, Lineas

# Mes anterior 

# (31 de Agosto 2020) 
dt_C1_mes  = [1335.4,	1057.9,	1142.6,	340.5,	314.3,	118.2,	3.8]
dt_CS1_mes = [452.9765441,	272.0426524,	292.2822827,	56.72312128,	44.23163293,	20.72642453,	0.1999333555]
dt_S1_mes  = [882.4,	785.8,	850.3,	283.8,	270.1,	97.4,	3.6]

dp_C1_mes  = [1257.9,	1008.1,	1047.6,	306.2,	256.3,	102.1,	2.4]
dp_CS1_mes = [443.2667372,	265.1377077,	282.2566391,	55.80458688,	33.76265882,	20.68006317,	0.1043130551]
dp_S1_mes  = [814.7,	742.9,	765.3,	250.4,	222.5,	81.3,	2.3]

# (31 de Julio 2020) 
#dt_C1_mes  = [1293.3,	1018.9,	1142.9,	336.2,	309.2,	116.4,	3.1]
#dt_CS1_mes = [431.387472,	276.6026051,	279.8705599,	59.38963318,	44.02588801,	21.75441247,	0.0435727316]
#dt_S1_mes  = [861.9,	742.3,	863,	276.8,	265.1,	94.7,	3]

#dp_C1_mes  = [1213.5,	962.2,	1048.3,	303.2,	252.6,	100.4,	1.8]
#dp_CS1_mes = [420.0237036,	265.2591706,	271.4203549,	56.36859045,	35.45658413,	21.73407852,	0.04066788283]
#dp_S1_mes  = [793.4,	697,	776.8,	246.8,	217,	78.7,	1.7]

# (30 de Junio 2020) 
#dt_C1_mes  = [1288.2,	1010,	1111.2,	334.7,	308,	119.8,	2.3]
#dt_CS1_mes = [443.6953793,	277.2699343,	265.8165182,	62.07792283,	45.85152203,	22.14385351,	0.04076985128]
#dt_S1_mes  = [844.5,	732.8,	845.3,	272.6,	262.2,	97.7,	2.2]

#dp_C1_mes  = [1215,	961.9,	1000.3,	304.4,	255.4,	102.8,	1.5]
#dp_CS1_mes = [432.0584989,	268.6179894,	256.0171932,	59.83266888,	36.04346066,	22.12346858,	0.03494558681]
#dp_S1_mes  = [782.9,	693.4,	744.2,	244.5,	219.4,	80.8,	1.4]



# (31 de Mayo 2020) 
#dt_C1_mes  = [1300.92,	1003.83,	1099.11,	332.56,	297.85,	121.68,	1.48]
#dt_CS1_mes = [456.41,	276.02,	251.50,	60.85,	42.49,	22.60,	0.04]
#dt_S1_mes  = [844.51,	727.80,	847.61,	271.71,	255.36,	99.08,	1.44]

#dp_C1_mes  = [1237.85,	957.04,	968.48,	302.88,	239.52,	102.77,	1.15]
#dp_CS1_mes = [449.85,	268.78,	243.57,	58.73,	35.79,	21.56,	0.04]
#dp_S1_mes  = [788.00,	688.26,	724.91,	244.14,	203.74,	81.21,	1.11]


# (Abril 2020)
#dt_C1_mes  = [1282.8,	990.5,	1089,	331.1,	298,	120.8,	1.2]
#dt_CS1_mes = [458.1128696,	262.7420223,	239.3972561,	62.28490155,	40.24828507,	21.97223328,	0.04975066139]
#dt_S1_mes  = [824.7,	727.9,	849.7,	268.9,	257.8,	98.8,	1.1]

#dp_C1_mes  = [1222.1,	944.2,	962.2,	301.5,	245.3,	102.1,	0.9]
#dp_CS1_mes = [450.9663334,	254.9955517,	230.6996699,	59.99929764,	33.88020041,	20.94502845,	0.0438976424]
#dp_S1_mes  = [771.2,	689.4,	731.6,	241.6,	211.5,	81.1,	0.8]

# (Marzo 2020)
#dt_C1_mes  = [1272,	1002.2,	1091.1,	340.6,	277.9,	119.9,	1.5]
#dt_CS1_mes = [450.5261429,	279.8898136,	242.4628238,	63.21048355,	36.18900659,	21.85245704,	0.04693775174]
#dt_S1_mes  = [821.5,	722.3,	848.7,	277.4,	241.7,	98.1,	1.4]

#dp_C1_mes  = [1210,	954.5,	950.2,	304,	226.7,	104.3,	0.9]
#dp_CS1_mes = [444.1103389,	272.4707152,	234.8559744,	61.09535111,	30.47140171,	21.83192178,	0.04107053277]
#dp_S1_mes  = [765.9,	682,	715.4,	243,	196.2,	82.6,	0.8]


# (Febrero 2020)
#dt_C1_mes  = [1285.6,	1047.4,	1090.5,	338.1,	269.8,	120.6,	1.5]
#dt_CS1_mes = [481.8748088,	310.563372,	253.9938357,	60.90746536,	32.55358445,	24.20123285,	0.09999294167]
#dt_S1_mes  = [803.7,	736.9,	836.5,	277.2,	237.3,	96.4,	1.4]

#dp_C1_mes  = [1221.7,	1000.2,	948.4,	302.4,	221.3,	105,	0.8]
#dp_CS1_mes = [475.9458156,	303.3932899,	246.3208479,	58.60468673,	27.01574007,	24.18064607,	0.06176034633]
#dp_S1_mes  = [745.7,	696.9,	702,	243.8,	194.4,	80.8,	0.7]


# (Enero 2020)
#dt_C1_mes  = [1248.5,	1037.7,	1046.3,	329.2,	262.8,	118.7,	0.3]
#dt_CS1_mes = [455.7717648,	312.0399494,	244.3865353,	56.76401487,	32.27318419,	23.50329718,	0.04716577887]
#dt_S1_mes  = [792.7,	725.7,	801.9,	272.5,	230.5,	95.2,	0.2]

#dp_C1_mes  = [1186.5,	962.2,	909,	295.5,	215.7,	103.4,	0.3]
#dp_CS1_mes = [450.309378,	275.6810296,	236.9991952,	54.02545183,	29.15729492,	22.99921292,	0.04716577887]
#dp_S1_mes  = [736.2,	686.6,	671.9,	241.5,	186.6,	80.4,	0.2]

# (Diciembre 2019)
#dt_C1_mes  = [1225.7,	1009,	1033.4,	326.9,	249.2,	118.5,	1.8]
#dt_CS1_mes = [448.9643331,	297.3659869,	238.1280273,	55.80691587,	33.5420724,	25.14325568,	0.1152546981]
#dt_S1_mes  = [776.8,	711.6,	795.2,	271,	215.7,	93.4,	1.7]

#dp_C1_mes  = [1164.9,	960,	896.9,	295.5,	205.8,	103.8,	1.8]
#dp_CS1_mes = [441.6766899,	289.1769928,	230.6808006,	53.79143628,	28.5329259,	24.64381865,	0.1152546981]
#dp_S1_mes  = [723.3,	670.8,	666.2,	241.7,	177.3,	79.2,	1.7]

# (Noviembre 2019)
#dt_C1_mes  = [1282.2,	948.6,	1022.4,	377.8,	236.3,	118.1,	0.1]
#dt_CS1_mes = [466.4031855,	274.7857981,	224.3905763,	56.77683894,	31.38072835,	24.86282782,	0.002962682057]
#dt_S1_mes  = [815.8,	673.9,	798,	321.1,	204.9,	93.2,	0.1]

#dp_C1_mes  = [1226.3,	899.9,	893,	345.7,	197.8,	102.8,	0.1]
#dp_CS1_mes = [459.372741,	269.1181873,	217.8163848,	54.80073,	28.29953901,	24.35917187,	0.002962682057]
#dp_S1_mes  = [767,	630.9,	675.2,	291,	169.5,	78.4,	0.1]

# (Octubre 2019)
#dt_C1_mes  = [1237.1, 940.1, 970, 386.6, 235.2, 121.8, 0]
#dt_CS1_mes = [431.2485707, 245.0009355,	199.9714891, 59.58486901, 37.47702049, 24.8698446, 0]
#dt_S1_mes  = [805.8, 695.1, 770, 327, 197.7, 97, 0]#

#dp_C1_mes  = [1182.1, 892.1, 833, 354.7, 190.9, 105.1, 0]
#dp_CS1_mes = [424.0347121, 239.6462269, 191.783507, 57.39309145, 27.46849691, 24.3649636, 0]
#dp_S1_mes  = [758, 652.5, 641.2, 297.2, 163.4, 80.8, 0]

# (Septiembre 2019)
#dt_C1_mes  = [1260.3,	924.1,	955.6,	377.6,	222.2,	120.5]#,	0]
#dt_CS1_mes = [443.10079, 244.3926864, 198.4367218, 55.41555703,	37.12860215, 23.98000722]#, 0]
#dt_S1_mes  = [817.2, 679.7, 757.2, 322.2, 185.1, 96.5]#, 0]

#dp_C1_mes  = [1203.3, 876.3, 817.2,	349.9, 186.5, 103.8]#, 0]
#dp_CS1_mes = [439.0091882, 237.5544627,	188.3389349, 53.47711596, 32.17513964, 23.43127928]#, 0]
#dp_S1_mes  = [764.3, 638.8, 628.9, 296.4, 154.4, 80.4]#, 0]



# (Agosto 2019)
#dt_C1_mes  = [1222.7, 939.8, 940, 371.6, 216.4,	125.9,	163.8]
#dt_CS1_mes = [430.8055297, 257.722791,	194.3116184, 53.00033834, 35.56211618, 25.93576243,	34.5051635]
#dt_S1_mes  = [791.9, 682.1, 745.7, 318.6, 180.9, 100, 129.3]

#dp_C1_mes  = [1168.8, 891, 802.9, 344, 180, 109, 163.8]
#dp_CS1_mes = [426.3681249, 250.2522614,	184.9727079, 51.07806179, 27.95085919, 25.39081799,	34.5051635]
#dp_S1_mes  = [742.4, 640.7,	617.9, 292.9, 152.1, 83.6,	129.3]


# Diciembre 2019

dt_C1_dic19  = [1225.7,	1009,	1033.4,	326.9,	249.2,	118.5,	1.8]
dt_CS1_dic19 = [448.9643331,	297.3659869,	238.1280273,	55.80691587,	33.5420724,	25.14325568,	0.1152546981]
dt_S1_dic19  = [776.8,	711.6,	795.2,	271,	215.7,	93.4,	1.7]

dp_C1_dic19  = [1164.9,	960,	896.9,	295.5,	205.8,	103.8,	1.8]
dp_CS1_dic19 = [441.6766899,	289.1769928,	230.6808006,	53.79143628,	28.5329259,	24.64381865,	0.1152546981]
dp_S1_dic19  = [723.3,	670.8,	666.2,	241.7,	177.3,	79.2,	1.7]


# Diciembre 2018

dt_C1_dic18  = [1224.8,	938.3,	1023.2,	397,	225.9,	142, 0]#,	343.2]
dt_CS1_dic18 = [390.09,	226.94,	199.8,	58.59,	33.62,	20.78, 0]#, 88.92]
dt_S1_dic18  = [834.7,	711.3,	823.4,	338.4,	192.2,	121.2, 0]#, 254.2]

dp_C1_dic18  = [1186.8,	885.2,	875.7,	354.3,	176.5,	120.1, 0]#, 343.2]
dp_CS1_dic18 = [387.2,	219.72,	193.6,	56.64,	20.94,	19.74, 0]#, 88.92]
dp_S1_dic18  = [799.6,	665.4,	682.1,	297.6,	155.5,	100.3, 0]#, 254.2]

# Marzo 2018

dt_C1_mar18  = [1778.88, 1306.32, 1431.17, 500.50, 301.21, 157.54, 0]#, 382.59]
dt_CS1_mar18 = [619.48, 341.70, 269.75, 75.29, 33.30, 20.41, 0]#, 129.73]
dt_S1_mar18  = [1159.40, 964.62, 1161.42, 425.21, 267.91, 137.13, 0]#, 252.86]

dp_C1_mar18  = [1737.6, 1258.9, 1289.9, 452.5, 263.1, 137.9, 0]#, 382.6]
dp_CS1_mar18 = [616.2, 329.6, 260.7, 71.7, 21.4, 19.2, 0]#, 129.]
dp_S1_mar18  = [1121.5, 929.3, 1029.3, 380.7, 241.8, 118.7, 0]#, 252.9]

# Diciembre 2017

dt_C1_dic17  = [1636.03, 1245.49, 1369.01, 488.87, 294.36, 148.75, 0]#, 329.79]
dt_CS1_dic17 = [483.73, 309.53, 281.36, 69.09, 38.02, 17.59, 0]#, 107.38]
dt_S1_dic17  = [1152.30, 935.96, 1087.63,419.78, 256.34, 131.16, 0]#, 222.42]

dp_C1_dic17  = [1609.7, 1205.8, 1271.4, 445.9, 256.4, 128.1, 0]#, 329.9]
dp_CS1_dic17 = [481, 303.4, 276.2, 68, 20.7,  17.1, 0]#,  107.4]
dp_S1_dic17  = [1128.6, 902.4, 995.1, 377.9,  235.8, 110.9, 0]#, 222.5]

# %%
import numpy as np

import pandas as pd

#help(tabula.read_pdf)

# Se deberá instalar el módulo y garantizar que esté instalado java en la computadora:
#!pip install tabula-py
import tabula

# %%

"""## Depósitos en Córdobas"""

#Cuadro de Depósitos en Córdobas
depositos_CS = tabula.read_pdf(pdf,
                     area=(area1), pages=1,
#                    output_format="dataframe",
#                     pages = "all", # en caso que sean varias páginas =>"all",    #####
                     pandas_options={'header': None})
                     #multiple_tables = False)

depositos_CS = depositos_CS[0]

depositos_CS

# %%
# %%

type(depositos_CS)

#depositos_CS = pd.DataFrame(depositos_CS)
#depositos_CS
# %%
depositos_CS.info()  #Aparecen variables como texto, esto es responsabilidades de las comas y porcentaje %

# %%
# Convirtiendo todos los valores a numéricos (float).
depositos_CS = depositos_CS.replace('', 0)
depositos_CS1 = depositos_CS[cols1].replace({'%': '', ',': ''}, regex=True).astype(float)
depositos_CS1['instituciones'] = depositos_CS[0]
depositos_CS1.info()

# %%
depositos_CS1

# %%
depositos_CS1 = depositos_CS1.loc[0:canti,:]
depositos_CS1.loc[0:,"instituciones"] = instituciones
depositos_CS1

# %%
"""## Depósitos en Dólares"""

#Cuadro de Depósitos en Córdobas
depositos_S = tabula.read_pdf(pdf,
                     area=(area2), pages=1,
                    # pages = 1, # en caso que sean varias páginas =>"all",  
                     pandas_options={'header': None})
                     #multiple_tables = True)

depositos_S = depositos_S[0]

# %%
depositos_S.info()

# %%
# Convirtiendo todos los valores a numéricos (float).
depositos_S = depositos_S.replace('', 0)
depositos_S1 = depositos_S[cols2].replace({'%': '', ',': ''}, regex=True).astype(float)
depositos_S1['instituciones'] = depositos_S[0]
depositos_S1.info()

# %%
depositos_S1

depositos_S1 = depositos_S1.loc[0:canti,:]
depositos_S1.loc[0:,"instituciones"] = instituciones
depositos_S1

# %%
"""## Depósitos Consolidados"""

#Cuadro de Depósitos en Córdobas
depositos_C = tabula.read_pdf(pdf,
                     area=(area3), pages=1,
                    # pages = 1, # en caso que sean varias páginas =>"all",  
                     pandas_options={'header': None})
                     #multiple_tables = True)

depositos_C = depositos_C[0]
# %%

depositos_C.info()

# %%
# Convirtiendo todos los valores a numéricos (float).
depositos_C = depositos_C.replace('', 0)
depositos_C1 = depositos_C[cols3].replace({'%': '', ',': ''}, regex=True).astype(float)
depositos_C1['instituciones'] = depositos_C[0]
depositos_C1.info()

# %%
depositos_C1

# %%
depositos_C1 = depositos_C1.loc[0:canti,:]
depositos_C1.loc[0:,"instituciones"] = instituciones
depositos_C1

# %%
"""# Convertir a una sola moneda"""

depositos_CS1

# %%
#depositos_CS1.loc[0:,[1,2,3,4,6,9,11]] = depositos_CS1[0:,[1,2,3,4,6,9,11]]

depositos_CS1.loc[0:,[1,2,3,4,6,9,11]] = depositos_CS1.loc[0:,[1,2,3,4,6,9,11]] / TIPO

depositos_CS1

# %%
"""## Importación a GoogleSheets"""

import pygsheets

#gc = pygsheets.authorize(service_account_file = r'C:\\Users\\Deybi.Morales\\Google Drive\\Scripts\\JUPYTERLAB\\elegant-weaver-254616-b76ad103c4e5.json')
gc = pygsheets.authorize(service_account_file = 'C:/Users/JENNY/Desktop/BORRAR HOY/Hackers-finanzas/data_07082020/elegant-weaver-254616-b76ad103c4e5.json')

sh = gc.open('DEPOSITOSDIARIOS')

# Commented out IPython magic to ensure Python compatibility.
# Ejecutando script python
# %run -i "/content/drive/My Drive/Scripts/JUPYTERLAB/depositos_diarios.py"

################################################################################################################################################
################################################################################################################################################
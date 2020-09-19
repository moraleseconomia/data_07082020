"""## Importación a GoogleSheets"""

#import gspread
#from oauth2client.service_account import ServiceAccountCredentials

#scope = ['https://spreadsheets.google.com/feeds',
#         'https://www.googleapis.com/auth/drive']

#credentials = ServiceAccountCredentials.from_json_keyfile_name('elegant-weaver-254616-b76ad103c4e5.json', scope)

#gc = gspread.authorize(credentials)

#sh = gc.open(googleSheet)


"""### Los tipos de depósitos consolidados por monedas"""

#worksheet = sh.worksheet("bd_depositos_diarios")

#import numpy as np
#dt = np.array(depositos_C1[1])
#dtcs = np.array(depositos_CS1[1])
#dts = np.array(depositos_S1[1])



#cell_list = worksheet.range('B%s' % + linea + ':I%s' % + linea)
#cell_values = np.append(dt, np.sum(dt))

#for i, val in enumerate(cell_values): 
#    cell_list[i].value = val    

#worksheet.update_cells(cell_list, 'USER_ENTERED')
#worksheet.update_acell('A%s' % + linea, FECHA)

#cell_list = worksheet.range('M%s' % + linea + ':T%s' % + linea)
#cell_values = np.append(dtcs, np.sum(dtcs))

#for i, val in enumerate(cell_values): 
#    cell_list[i].value = val    

#worksheet.update_cells(cell_list, 'USER_ENTERED')
#worksheet.update_acell('L%s' % + linea, FECHA)

#cell_list = worksheet.range('X%s' % + linea + ':AE%s' % + linea)
#cell_values = np.append(dts, np.sum(dts))

#for i, val in enumerate(cell_values): 
#    cell_list[i].value = val    

#worksheet.update_cells(cell_list, 'USER_ENTERED')
#worksheet.update_acell('W%s' % + linea, FECHA)

depositos_C1

wks = sh.worksheet_by_title("bd_depositos_diarios")

### Consolidado

wks.update_value('A%s' % + linea , FECHA)
cell_values = depositos_C1[[1]].T#, np.sum(depositos_C1))
wks.update_values('B%s' % + linea + ':H%s' % + linea, np.array(cell_values).tolist())
wks.update_value('J%s' % + linea , depositos_C1[1].sum(axis=0))

### Córdobas
depositos_CS1

wks.update_value('M%s' % + linea , FECHA)
cell_values = depositos_CS1[[1]].T#, np.sum(depositos_C1))
wks.update_values('N%s' % + linea + ':T%s' % + linea, np.array(cell_values).tolist())
wks.update_value('V%s' % + linea , depositos_CS1[1].sum(axis=0))

### Dólares

wks.update_value('Y%s' % + linea , FECHA)
cell_values = depositos_S1[[1]].T#, np.sum(depositos_C1))
wks.update_values('Z%s' % + linea + ':AF%s' % + linea, np.array(cell_values).tolist())
wks.update_value('AH%s' % + linea , depositos_S1[1].sum(axis=0))



# Insertar Variaciones Consolidadas

wks = sh.worksheet_by_title("bd_depositos_diarios")

encabezado = wks.get_values(start='B2', end='J2', returnas='matrix')
data_dt = wks.get_values(start = 'B%s' % + (linea-1), end = 'J%s' % + linea, returnas='matrix')
data_dt = pd.DataFrame(data_dt, columns=encabezado[0])

data_dt = data_dt.replace('', 0)

data_dt = data_dt.replace({'%': '', ',': '.'}, regex=True).astype(float)

data_dt_dif = data_dt.diff()

data_dt_dif

import numpy as np
wks.update_value('AK%s' % + linea , FECHA)
wks.update_values('AL%s' % + linea + ':AT%s' % + linea, np.array(data_dt_dif.loc[1:,]).tolist())



############## Insertar variación en córdobas

encabezado = wks.get_values(start='N2', end='V2', returnas='matrix')
data_dt = wks.get_values(start = 'N%s' % + (linea-1), end = 'V%s' % + linea, returnas='matrix')
data_dt = pd.DataFrame(data_dt, columns=encabezado[0])

data_dt = data_dt.replace('', 0)

data_dt = data_dt.replace({'%': '', ',': '.'}, regex=True).astype(float)

data_dt_dif = data_dt.diff()

data_dt_dif

import numpy as np
wks.update_value('AW%s' % + linea , FECHA)
wks.update_values('AX%s' % + linea + ':BF%s' % + linea, np.array(data_dt_dif.loc[1:,]).tolist())

############## Insertar Variación en dólares

encabezado = wks.get_values(start='Z2', end='AH2', returnas='matrix')
data_dt = wks.get_values(start = 'Z%s' % + (linea-1), end = 'AH%s' % + linea, returnas='matrix')
data_dt = pd.DataFrame(data_dt, columns=encabezado[0])

data_dt = data_dt.replace('', 0)

data_dt = data_dt.replace({'%': '', ',': '.'}, regex=True).astype(float)

data_dt_dif = data_dt.diff()

data_dt_dif

import numpy as np
wks.update_value('BI%s' % + linea , FECHA)
wks.update_values('BJ%s' % + linea + ':BR%s' % + linea, np.array(data_dt_dif.loc[1:,]).tolist())

"""## Depósitos Instituciones Financieras"""

depositos_C1

wks = sh.worksheet_by_title("bd_instituciones_financieras")

### Consolidado

wks.update_value('A%s' % + linea , FECHA)
cell_values = depositos_C1[[6]].T#, np.sum(depositos_C1))
wks.update_values('B%s' % + linea + ':I%s' % + linea, np.array(cell_values).tolist())
wks.update_value('J%s' % + linea , depositos_C1[6].sum(axis=0))

### Córdobas

wks.update_value('M%s' % + linea , FECHA)
cell_values = depositos_CS1[[6]].T#, np.sum(depositos_C1))
wks.update_values('N%s' % + linea + ':U%s' % + linea, np.array(cell_values).tolist())
wks.update_value('V%s' % + linea , depositos_CS1[6].sum(axis=0))

### Dólares

wks.update_value('Y%s' % + linea , FECHA)
cell_values = depositos_S1[[6]].T#, np.sum(depositos_C1))
wks.update_values('Z%s' % + linea + ':AG%s' % + linea, np.array(cell_values).tolist())
wks.update_value('AH%s' % + linea , depositos_S1[6].sum(axis=0))

### Insertar variación consolidada

encabezado = wks.get_values(start='B2', end='J2', returnas='matrix')
data_dt = wks.get_values(start = 'B%s' % + (linea-1), end = 'J%s' % + linea, returnas='matrix')
data_dt = pd.DataFrame(data_dt, columns=encabezado[0])

data_dt = data_dt.replace('', 0)

data_dt = data_dt.replace({'%': '', ',': '.'}, regex=True).astype(float)

data_dt_dif = data_dt.diff()

wks.update_value('AK%s' % + linea , FECHA)
wks.update_values('AL%s' % + linea + ':AT%s' % + linea, np.array(data_dt_dif.loc[1:,]).tolist())

############## Insertar variación en córdobas

encabezado = wks.get_values(start='N2', end='V2', returnas='matrix')
data_dt = wks.get_values(start = 'N%s' % + (linea-1), end = 'V%s' % + linea, returnas='matrix')
data_dt = pd.DataFrame(data_dt, columns=encabezado[0])

data_dt = data_dt.replace('', 0)

data_dt = data_dt.replace({'%': '', ',': '.'}, regex=True).astype(float)

data_dt_dif = data_dt.diff()

data_dt_dif

wks.update_value('AW%s' % + linea , FECHA)
wks.update_values('AX%s' % + linea + ':BF%s' % + linea, np.array(data_dt_dif.loc[1:,]).tolist())

############## Insertar Variación en dólares

encabezado = wks.get_values(start='Z2', end='AH2', returnas='matrix')
data_dt = wks.get_values(start = 'Z%s' % + (linea-1), end = 'AH%s' % + linea, returnas='matrix')
data_dt = pd.DataFrame(data_dt, columns=encabezado[0])

data_dt = data_dt.replace('', 0)

data_dt = data_dt.replace({'%': '', ',': '.'}, regex=True).astype(float)

data_dt_dif = data_dt.diff()

wks.update_value('BI%s' % + linea , FECHA)
wks.update_values('BJ%s' % + linea + ':BR%s' % + linea, np.array(data_dt_dif.loc[1:,]).tolist())

"""## Obteniendo Depósitos del Público"""

dp_C1 = depositos_C1[[1]].sub(depositos_C1[6], axis=0)

dp_CS1 = depositos_CS1[[1]].sub(depositos_CS1[6], axis=0)

dp_S1 = depositos_S1[[1]].sub(depositos_S1[6], axis=0)

wks = sh.worksheet_by_title("bd_depositos_diariosp")

### Consolidado

wks.update_value('A%s' % + linea , FECHA)
cell_values = dp_C1.T#, np.sum(depositos_C1))
wks.update_values('B%s' % + linea + ':I%s' % + linea, np.array(cell_values).tolist())
wks.update_value('J%s' % + linea , dp_C1[1].sum(axis=0))

### Córdobas

wks.update_value('M%s' % + linea , FECHA)
cell_values = dp_CS1.T#, np.sum(depositos_C1))
wks.update_values('N%s' % + linea + ':U%s' % + linea, np.array(cell_values).tolist())
wks.update_value('V%s' % + linea , dp_CS1[1].sum(axis=0))

### Dólares

wks.update_value('Y%s' % + linea , FECHA)
cell_values = dp_S1.T#, np.sum(depositos_C1))
wks.update_values('Z%s' % + linea + ':AG%s' % + linea, np.array(cell_values).tolist())
wks.update_value('AH%s' % + linea , dp_S1[1].sum(axis=0))

### Insertar variación consolidada

encabezado = wks.get_values(start='B2', end='J2', returnas='matrix')
data_dt = wks.get_values(start = 'B%s' % + (linea-1), end = 'J%s' % + linea, returnas='matrix')
data_dt = pd.DataFrame(data_dt, columns=encabezado[0])

data_dt = data_dt.replace('', 0)

data_dt = data_dt.replace({'%': '', ',': '.'}, regex=True).astype(float)

data_dt_dif = data_dt.diff()

wks.update_value('AK%s' % + linea , FECHA)
wks.update_values('AL%s' % + linea + ':AT%s' % + linea, np.array(data_dt_dif.loc[1:,]).tolist())

############## Insertar variación en córdobas

encabezado = wks.get_values(start='N2', end='V2', returnas='matrix')
data_dt = wks.get_values(start = 'N%s' % + (linea-1), end = 'V%s' % + linea, returnas='matrix')
data_dt = pd.DataFrame(data_dt, columns=encabezado[0])

data_dt = data_dt.replace('', 0)

data_dt = data_dt.replace({'%': '', ',': '.'}, regex=True).astype(float)

data_dt_dif = data_dt.diff()

wks.update_value('AW%s' % + linea , FECHA)
wks.update_values('AX%s' % + linea + ':BF%s' % + linea, np.array(data_dt_dif.loc[1:,]).tolist())

############## Insertar Variación en dólares

encabezado = wks.get_values(start='Z2', end='AH2', returnas='matrix')
data_dt = wks.get_values(start = 'Z%s' % + (linea-1), end = 'AH%s' % + linea, returnas='matrix')
data_dt = pd.DataFrame(data_dt, columns=encabezado[0])

data_dt = data_dt.replace('', 0)

data_dt = data_dt.replace({'%': '', ',': '.'}, regex=True).astype(float)

data_dt_dif = data_dt.diff()

wks.update_value('BI%s' % + linea , FECHA)
wks.update_values('BJ%s' % + linea + ':BR%s' % + linea, np.array(data_dt_dif.loc[1:,]).tolist())

"""## Varaciones ___"""

wks = sh.worksheet_by_title("Variacion_a_dic_2017")

#### Variaciones a Diciembre 2017
# Depósitos Totales

## Variaciones consolidadas
depositos_C1

wks.update_value('A%s' % + linea , FECHA)
wks.update_values('B%s' % + linea + ':I%s' % + linea, np.array(np.array(depositos_C1[[1]].T) - dt_C1_dic17).tolist())
wks.update_value('J%s' % + linea , (np.array(depositos_C1[[1]].T) - dt_C1_dic17).sum())

## Variaciones córdobas

wks.update_value('M%s' % + linea , FECHA)
wks.update_values('N%s' % + linea + ':U%s' % + linea, np.array(np.array(depositos_CS1[[1]].T) - dt_CS1_dic17).tolist())
wks.update_value('V%s' % + linea , (np.array(depositos_CS1[[1]].T) - dt_CS1_dic17).sum())

## Variaciones dólares

wks.update_value('Y%s' % + linea , FECHA)
wks.update_values('Z%s' % + linea + ':AG%s' % + linea, np.array(np.array(depositos_S1[[1]].T) - dt_S1_dic17).tolist())
wks.update_value('AH%s' % + linea ,  (np.array(depositos_S1[[1]].T) - dt_S1_dic17).sum())

#### Variaciones a Diciembre 2017
# Depósitos del Público

wks.update_value('AK%s' % + linea , FECHA)
wks.update_values('AL%s' % + linea + ':AS%s' % + linea, np.array(np.array(dp_C1[[1]].T) - dp_C1_dic17).tolist())
wks.update_value('AT%s' % + linea , (np.array(dp_C1[[1]].T) - dp_C1_dic17).sum())

wks.update_value('AW%s' % + linea , FECHA)
wks.update_values('AX%s' % + linea + ':BE%s' % + linea, np.array(np.array(dp_CS1[[1]].T) - dp_CS1_dic17).tolist())
wks.update_value('BF%s' % + linea , (np.array(dp_CS1[[1]].T) - dp_CS1_dic17).sum())

wks.update_value('BI%s' % + linea , FECHA)
wks.update_values('BJ%s' % + linea + ':BQ%s' % + linea, np.array(np.array(dp_S1[[1]].T) - dp_S1_dic17).tolist())
wks.update_value('BR%s' % + linea , (np.array(dp_S1[[1]].T) - dp_S1_dic17).sum())

#### Variaciones a Marzo 2018
# Depósitos Totales

wks = sh.worksheet_by_title("Variacion_a_mar_2018")

## Variaciones consolidadas

wks.update_value('A%s' % + linea , FECHA)
wks.update_values('B%s' % + linea + ':I%s' % + linea, np.array(np.array(depositos_C1[[1]].T) - dt_C1_mar18).tolist())
wks.update_value('J%s' % + linea , (np.array(depositos_C1[[1]].T) - dt_C1_mar18).sum())

## Variaciones en córdobas

wks.update_value('M%s' % + linea , FECHA)
wks.update_values('N%s' % + linea + ':U%s' % + linea, np.array(np.array(depositos_CS1[[1]].T) - dt_CS1_mar18).tolist())
wks.update_value('V%s' % + linea , (np.array(depositos_CS1[[1]].T) - dt_CS1_mar18).sum())

## Variaciones dólares

wks.update_value('Y%s' % + linea , FECHA)
wks.update_values('Z%s' % + linea + ':AG%s' % + linea, np.array(np.array(depositos_S1[[1]].T) - dt_S1_mar18).tolist())
wks.update_value('AH%s' % + linea ,  (np.array(depositos_S1[[1]].T) - dt_S1_mar18).sum())

#### Variaciones a Marzo 2018
# Depósitos del Público

wks.update_value('AK%s' % + linea , FECHA)
wks.update_values('AL%s' % + linea + ':AS%s' % + linea, np.array(np.array(dp_C1[[1]].T) - dp_C1_mar18).tolist())
wks.update_value('AT%s' % + linea , (np.array(dp_C1[[1]].T) - dp_C1_mar18).sum())

wks.update_value('AW%s' % + linea , FECHA)
wks.update_values('AX%s' % + linea + ':BE%s' % + linea, np.array(np.array(dp_CS1[[1]].T) - dp_CS1_mar18).tolist())
wks.update_value('BF%s' % + linea , (np.array(dp_CS1[[1]].T) - dp_CS1_mar18).sum())

wks.update_value('BI%s' % + linea , FECHA)
wks.update_values('BJ%s' % + linea + ':BQ%s' % + linea, np.array(np.array(dp_S1[[1]].T) - dp_S1_mar18).tolist())
wks.update_value('BR%s' % + linea , (np.array(dp_S1[[1]].T) - dp_S1_mar18).sum())

#### Variaciones a Diciembre 2018
# Depósitos Totales

wks = sh.worksheet_by_title("Variacion_a_dic_2018")

## Variaciones consolidadas

wks.update_value('A%s' % + linea , FECHA)
wks.update_values('B%s' % + linea + ':I%s' % + linea, np.array(np.array(depositos_C1[[1]].T) - dt_C1_dic18).tolist())
wks.update_value('J%s' % + linea , (np.array(depositos_C1[[1]].T) - dt_C1_dic18).sum())

## Variaciones en córdobas

wks.update_value('M%s' % + linea , FECHA)
wks.update_values('N%s' % + linea + ':U%s' % + linea, np.array(np.array(depositos_CS1[[1]].T) - dt_CS1_dic18).tolist())
wks.update_value('V%s' % + linea , (np.array(depositos_CS1[[1]].T) - dt_CS1_dic18).sum())

## Variaciones dólares

wks.update_value('Y%s' % + linea , FECHA)
wks.update_values('Z%s' % + linea + ':AG%s' % + linea, np.array(np.array(depositos_S1[[1]].T) - dt_S1_dic18).tolist())
wks.update_value('AH%s' % + linea ,  (np.array(depositos_S1[[1]].T) - dt_S1_dic18).sum())

#### Variaciones a Diciembre 2018
# Depósitos del Público

wks.update_value('AK%s' % + linea , FECHA)
wks.update_values('AL%s' % + linea + ':AS%s' % + linea, np.array(np.array(dp_C1[[1]].T) - dp_C1_dic18).tolist())
wks.update_value('AT%s' % + linea , (np.array(dp_C1[[1]].T) - dp_C1_dic18).sum())

wks.update_value('AW%s' % + linea , FECHA)
wks.update_values('AX%s' % + linea + ':BE%s' % + linea, np.array(np.array(dp_CS1[[1]].T) - dp_CS1_dic18).tolist())
wks.update_value('BF%s' % + linea , (np.array(dp_CS1[[1]].T) - dp_CS1_dic18).sum())

wks.update_value('BI%s' % + linea , FECHA)
wks.update_values('BJ%s' % + linea + ':BQ%s' % + linea, np.array(np.array(dp_S1[[1]].T) - dp_S1_dic18).tolist())
wks.update_value('BR%s' % + linea , (np.array(dp_S1[[1]].T) - dp_S1_dic18).sum())

#### Variaciones a Mes Anterior
# Depósitos Totales

wks = sh.worksheet_by_title("Variacion_mes_anterior")

## Variaciones consolidadas

wks.update_value('A%s' % + linea , FECHA)
wks.update_values('B%s' % + linea + ':I%s' % + linea, np.array(np.array(depositos_C1[[1]].T) - dt_C1_mes).tolist())
wks.update_value('J%s' % + linea , (np.array(depositos_C1[[1]].T) - dt_C1_mes).sum())

## Variaciones en córdobas

wks.update_value('M%s' % + linea , FECHA)
wks.update_values('N%s' % + linea + ':U%s' % + linea, np.array(np.array(depositos_CS1[[1]].T) - dt_CS1_mes).tolist())
wks.update_value('V%s' % + linea , (np.array(depositos_CS1[[1]].T) - dt_CS1_mes).sum())

## Variaciones dólares

wks.update_value('Y%s' % + linea , FECHA)
wks.update_values('Z%s' % + linea + ':AG%s' % + linea, np.array(np.array(depositos_S1[[1]].T) - dt_S1_mes).tolist())
wks.update_value('AH%s' % + linea ,  (np.array(depositos_S1[[1]].T) - dt_S1_mes).sum())

#### Variaciones a Mes Anterior
# Depósitos del Público

wks.update_value('AK%s' % + linea , FECHA)
wks.update_values('AL%s' % + linea + ':AS%s' % + linea, np.array(np.array(dp_C1[[1]].T) - dp_C1_mes).tolist())
wks.update_value('AT%s' % + linea , (np.array(dp_C1[[1]].T) - dp_C1_mes).sum())

wks.update_value('AW%s' % + linea , FECHA)
wks.update_values('AX%s' % + linea + ':BE%s' % + linea, np.array(np.array(dp_CS1[[1]].T) - dp_CS1_mes).tolist())
wks.update_value('BF%s' % + linea , (np.array(dp_CS1[[1]].T) - dp_CS1_mes).sum())

wks.update_value('BI%s' % + linea , FECHA)
wks.update_values('BJ%s' % + linea + ':BQ%s' % + linea, np.array(np.array(dp_S1[[1]].T) - dp_S1_mes).tolist())
wks.update_value('BR%s' % + linea , (np.array(dp_S1[[1]].T) - dp_S1_mes).sum())

"""## Encaje Diarios"""

depositos_C1

wks = sh.worksheet_by_title("bd_encajes_diarios")

### Consolidado

depositos_C1[[7]] = depositos_C1[[7]].replace(np.nan, 0)
depositos_C1[[7]]

wks.update_value('A%s' % + linea , FECHA)
cell_values = depositos_C1[[7]].T.div(100)#, np.sum(depositos_C1))
wks.update_values('B%s' % + linea + ':I%s' % + linea, np.array(cell_values).tolist())
#wks.update_value('I%s' % + linea , depositos_C1[7].sum(axis=0))

### Córdobas

depositos_CS1[[7]] = depositos_CS1[[7]].replace(np.nan, 0)

wks.update_value('M%s' % + linea , FECHA)
cell_values = depositos_CS1[[7]].T.div(100)#, np.sum(depositos_C1))
wks.update_values('N%s' % + linea + ':U%s' % + linea, np.array(cell_values).tolist())
#wks.update_value('T%s' % + linea , depositos_CS1[6].sum(axis=0))

### Dólares

depositos_S1[[7]] = depositos_S1[[7]].replace(np.nan, 0)

wks.update_value('Y%s' % + linea , FECHA)
cell_values = depositos_S1[[7]].T.div(100)#, np.sum(depositos_C1))
wks.update_values('Z%s' % + linea + ':AG%s' % + linea, np.array(cell_values).tolist())
#wks.update_value('AE%s' % + linea , depositos_S1[6].sum(axis=0))

"""## Encaje Semana"""

depositos_C1

wks = sh.worksheet_by_title("bd_encajes_semanal")

### Consolidado

depositos_C1[[8]] = depositos_C1[[8]].replace(np.nan, 0)

wks.update_value('A%s' % + linea , FECHA)
cell_values = depositos_C1[[8]].T.div(100)#, np.sum(depositos_C1))
wks.update_values('B%s' % + linea + ':I%s' % + linea, np.array(cell_values).tolist())
#wks.update_value('I%s' % + linea , depositos_C1[7].sum(axis=0))

### Córdobas

depositos_CS1[[8]] = depositos_CS1[[8]].replace(np.nan, 0)

wks.update_value('M%s' % + linea , FECHA)
cell_values = depositos_CS1[[8]].T.div(100)#, np.sum(depositos_C1))
wks.update_values('N%s' % + linea + ':U%s' % + linea, np.array(cell_values).tolist())
#wks.update_value('T%s' % + linea , depositos_CS1[6].sum(axis=0))

### Dólares

depositos_S1[[8]] = depositos_S1[[8]].replace(np.nan, 0)

wks.update_value('Y%s' % + linea , FECHA)
cell_values = depositos_S1[[8]].T.div(100)#, np.sum(depositos_C1))
wks.update_values('Z%s' % + linea + ':AG%s' % + linea, np.array(cell_values).tolist())
#wks.update_value('AE%s' % + linea , depositos_S1[6].sum(axis=0))

"""## Exceso Déficit"""

depositos_C1

wks = sh.worksheet_by_title("bd_depositos_exceso_deficit")

### Consolidado

depositos_C1[[9]] = depositos_C1[[9]].replace(np.nan, 0)

wks.update_value('A%s' % + linea , FECHA)
cell_values = depositos_C1[[9]].T#, np.sum(depositos_C1))
wks.update_values('B%s' % + linea + ':I%s' % + linea, np.array(cell_values).tolist())
wks.update_value('J%s' % + linea , depositos_C1[9].sum(axis=0))

### Córdobas

depositos_CS1[[9]] = depositos_CS1[[9]].replace(np.nan, 0)

wks.update_value('M%s' % + linea , FECHA)
cell_values = depositos_CS1[[9]].T#, np.sum(depositos_C1))
wks.update_values('N%s' % + linea + ':U%s' % + linea, np.array(cell_values).tolist())
wks.update_value('V%s' % + linea , depositos_CS1[9].sum(axis=0))

### Dólares

depositos_S1[[9]] = depositos_S1[[9]].replace(np.nan, 0)

wks.update_value('Y%s' % + linea , FECHA)
cell_values = depositos_S1[[9]].T #, np.sum(depositos_C1))
wks.update_values('Z%s' % + linea + ':AG%s' % + linea, np.array(cell_values).tolist())
wks.update_value('AH%s' % + linea , depositos_S1[9].sum(axis=0))

### Insertar variación consolidada

encabezado = wks.get_values(start='B2', end='J2', returnas='matrix')
data_dt = wks.get_values(start = 'B%s' % + (linea-1), end = 'J%s' % + linea, returnas='matrix')
data_dt = pd.DataFrame(data_dt, columns=encabezado[0])

data_dt = data_dt.replace('', 0)

data_dt = data_dt.replace({'%': '', ',': '.'}, regex=True).astype(float)

data_dt_dif = data_dt.diff()

wks.update_value('AK%s' % + linea , FECHA)
wks.update_values('AL%s' % + linea + ':AT%s' % + linea, np.array(data_dt_dif.loc[1:,]).tolist())

############## Insertar variación en córdobas

encabezado = wks.get_values(start='N2', end='V2', returnas='matrix')
data_dt = wks.get_values(start = 'N%s' % + (linea-1), end = 'V%s' % + linea, returnas='matrix')
data_dt = pd.DataFrame(data_dt, columns=encabezado[0])

data_dt = data_dt.replace('', 0)

data_dt = data_dt.replace({'%': '', ',': '.'}, regex=True).astype(float)

data_dt_dif = data_dt.diff()

wks.update_value('AW%s' % + linea , FECHA)
wks.update_values('AX%s' % + linea + ':BF%s' % + linea, np.array(data_dt_dif.loc[1:,]).tolist())

############## Insertar Variación en dólares

encabezado = wks.get_values(start='Z2', end='AH2', returnas='matrix')
data_dt = wks.get_values(start = 'Z%s' % + (linea-1), end = 'AH%s' % + linea, returnas='matrix')
data_dt = pd.DataFrame(data_dt, columns=encabezado[0])

data_dt = data_dt.replace('', 0)

data_dt = data_dt.replace({'%': '', ',': '.'}, regex=True).astype(float)

data_dt_dif = data_dt.diff()

wks.update_value('BI%s' % + linea , FECHA)
wks.update_values('BJ%s' % + linea + ':BR%s' % + linea, np.array(data_dt_dif.loc[1:,]).tolist())

"""## VOLATILIDAD"""

wks = sh.worksheet_by_title("VOLATILIDAD")

from datetime import datetime, timedelta
from datetime import date

diass = (datetime.strptime(FECHA, '%d/%m/%Y') - datetime.strptime('31/03/2018', '%d/%m/%Y')).days
#diass
VARIACION = (dp_C1.sub(dp_C1_mar18, axis=0)).div(diass)
VARIACION

DIAS_EXCESO = -depositos_C1[[9]].div(np.array(VARIACION))
DIAS_EXCESO

wks.update_value('A%s' % + linea , FECHA)
cell_values = VARIACION.T#, np.sum(depositos_C1))
wks.update_values('B%s' % + linea + ':I%s' % + linea, np.array(cell_values).tolist())
wks.update_value('J%s' % + linea , VARIACION[1].sum(axis=0))

wks.update_value('M%s' % + linea , FECHA)
cell_values = DIAS_EXCESO.T#, np.sum(depositos_C1))
wks.update_values('N%s' % + linea + ':U%s' % + linea, np.array(cell_values).tolist())
wks.update_value('V%s' % + linea , (-depositos_C1[[9]].sum(axis=0).div(np.array(VARIACION).sum(axis=0)))[9])


#### Variaciones a Diciembre 2019
# Depósitos Totales

wks = sh.worksheet_by_title("Variacion_a_dic_2019")

## Variaciones consolidadas

wks.update_value('A%s' % + linea , FECHA)
wks.update_values('B%s' % + linea + ':I%s' % + linea, np.array(np.array(depositos_C1[[1]].T) - dt_C1_dic19).tolist())
wks.update_value('J%s' % + linea , (np.array(depositos_C1[[1]].T) - dt_C1_dic19).sum())

## Variaciones en córdobas

wks.update_value('M%s' % + linea , FECHA)
wks.update_values('N%s' % + linea + ':U%s' % + linea, np.array(np.array(depositos_CS1[[1]].T) - dt_CS1_dic19).tolist())
wks.update_value('V%s' % + linea , (np.array(depositos_CS1[[1]].T) - dt_CS1_dic19).sum())

## Variaciones dólares

wks.update_value('Y%s' % + linea , FECHA)
wks.update_values('Z%s' % + linea + ':AG%s' % + linea, np.array(np.array(depositos_S1[[1]].T) - dt_S1_dic19).tolist())
wks.update_value('AH%s' % + linea ,  (np.array(depositos_S1[[1]].T) - dt_S1_dic19).sum())

#### Variaciones a Diciembre 2019
# Depósitos del Público

wks.update_value('AK%s' % + linea , FECHA)
wks.update_values('AL%s' % + linea + ':AS%s' % + linea, np.array(np.array(dp_C1[[1]].T) - dp_C1_dic19).tolist())
wks.update_value('AT%s' % + linea , (np.array(dp_C1[[1]].T) - dp_C1_dic19).sum())

wks.update_value('AW%s' % + linea , FECHA)
wks.update_values('AX%s' % + linea + ':BE%s' % + linea, np.array(np.array(dp_CS1[[1]].T) - dp_CS1_dic19).tolist())
wks.update_value('BF%s' % + linea , (np.array(dp_CS1[[1]].T) - dp_CS1_dic19).sum())

wks.update_value('BI%s' % + linea , FECHA)
wks.update_values('BJ%s' % + linea + ':BQ%s' % + linea, np.array(np.array(dp_S1[[1]].T) - dp_S1_dic19).tolist())
wks.update_value('BR%s' % + linea , (np.array(dp_S1[[1]].T) - dp_S1_dic19).sum())


#############################################################################################################
#############################################################################################################






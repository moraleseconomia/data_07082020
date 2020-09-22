# -*- coding: utf-8 -*-
"""IMPORTAR A EXCEL Y DUPLICACION.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JgrSfXh8Izt1xgiyuqvp2EDMX1meFGpt

# Importar a Excel datos
"""

# from google.colab import drive
# drive.mount('/content/drive')

# %%
import pandas as pd
datos = pd.read_excel('~/Google Drive/Datos/SaldosMuc20200831.xls')#, index_col=0)

datos.head()

# %%
from pandas import ExcelWriter

writer = ExcelWriter('SaldosMuc20200831.xlsx')
datos.to_excel(writer, 'SaldosMuc', index=False)
writer.save()


# %%
##############################################################################################################################################
##############################################################################################################################################


# Comprobación de Banlanzas contable


###############################################################################
###############################################################################

# %%
# Segundo archivo de Balanza Contable

import pandas as pd
datoss = pd.read_excel('/content/drive/My Drive/Datos/SaldosMuc20191231-3.xls')#, index_col=0)

datoss.head()

# %%

datos.equals(datoss)

df_diff = pd.concat([datos,datoss]).drop_duplicates(keep=False)
df_diff

################################################################################################################################################
################################################################################################################################################

# %%
## Revisando datos de Asegurados

datas = pd.read_csv('/content/drive/My Drive/Datos/ANXBCO_M_Depositos_FOGADE_diciembre2019.txt', sep="|", header=None)

datas.head()

# %%
datass = pd.read_csv('/content/drive/My Drive/Datos/ANXBCO_M_Depositos_FOGADE_diciembre2019-3.txt', sep="|", header=None)

datass.head()

datas.equals(datass)

dfa_diff = pd.concat([datas,datass]).drop_duplicates(keep=False)
dfa_diff

##########################################################################################################################################
##########################################################################################################################################
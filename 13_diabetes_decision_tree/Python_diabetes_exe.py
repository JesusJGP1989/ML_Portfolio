
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier, export_text


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

########################################
########################################
######## Definiciones ##################
########################################
########################################

def indiscernibility(attr, table):
    u_ind = {}  # un diccionario vacío para almacenar los elementos de la relación de indiscernibilidad (U/IND({conjunto de atributos}))
    attr_values = []  # una lista vacía para almacenar los valores de los atributos

    for i in table.index:
        attr_values = []
        for j in attr:
            attr_values.append(table.loc[i, j])  # encontrar el valor de la tabla en la fila correspondiente y el atributo deseado y agregarlo a la lista attr_values

        # convertir la lista en una cadena y verificar si ya es una clave en el diccionario
        key = ''.join(str(k) for k in attr_values)

        if key in u_ind:  # si la clave ya existe en el diccionario
            u_ind[key].add(i)
        else:  # si la clave aún no existe en el diccionario
            u_ind[key] = set()
            u_ind[key].add(i)

    # Ordenar la relación de indiscernibilidad por la longitud de cada conjunto
    u_ind_sorted = sorted(u_ind.values(), key=len, reverse=True)
    return u_ind_sorted

#############################################

def lower_approximation(R, X):  #We have to try to describe the knowledge in X with respect to the knowledge in R; both are LISTS OS SETS [{},{}]

  l_approx = set()  #change to [] if you want the result to be a list of sets

  #print("X : " + str(len(X)))
  #print("R : " + str(len(R)))

  for i in range(len(X)):
    for j in range(len(R)):

      if(R[j].issubset(X[i])):
        l_approx.update(R[j]) #change to .append() if you want the result to be a list of sets)
  return l_approx

###############################################


def upper_approximation(R, X):  #We have to try to describe the knowledge in X with respect to the knowledge in R; both are LISTS OS SETS [{},{}]

  u_approx = set()  #change to [] if you want the result to be a list of sets

  #print("X : " + str(len(X)))
  #print("R : " + str(len(R)))

  for i in range(len(X)):
    for j in range(len(R)):

      if(R[j].intersection(X[i])):
        u_approx.update(R[j]) #change to .append() if you want the result to be a list of sets

  return u_approx

###############################################

def GenerateDecisionTree(X, Y):
    
    # Establecer una semilla aleatoria para reproducibilidad
    np.random.seed(13)
    
    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

    # Crear el clasificador de árbol de decisión
    clf = DecisionTreeClassifier()

    # Entrenar el clasificador
    clf.fit(X_train, y_train)

    # Predecir las etiquetas para los datos de prueba
    y_pred = clf.predict(X_test)
    
    # Calcular la precisión del modelo
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Precisión del modelo: {accuracy:.2f}')

    # Mostrar el reporte de clasificación
    print(classification_report(y_test, y_pred))

    # Mostrar la matriz de confusión
    conf_matrix = confusion_matrix(y_test, y_pred)
    print('Matriz de confusión:')
    print(conf_matrix)
    
    return clf
##########################################################
## Calcular indiscernibilidad #########################

def calcular_indiscernibilidad(columnas_seleccionadas, dataset):
    
    ind = indiscernibility(columnas_seleccionadas, dataset)

    X_positivo = [set(dataset[dataset["C6_21"] == 1].index.tolist())]
    R = ind
    L = lower_approximation(R, X_positivo)
    U = upper_approximation(R, X_positivo)
    aprox = U-L

    #print(L)
    #print(U)

    #Obtener la cardinalidad de los conjuntos L y U
    cardinalidad_L = len(L)
    cardinalidad_U = len(U)

    #Dividar la cardinalidad del conjunto L entre la del conjunto U
    division = cardinalidad_L / cardinalidad_U

    print("La cardinalidad de L dividad por la cardinalidad de U es:\n ", division)

##########################################################
########### Calcular errror####################

def calcularError(Columna, dataset):
    coincidencias = (dataset["C6_21"] == Columna).sum()
    total_filas = len(dataset)
    no_coincidencias = total_filas - coincidencias
    error= (no_coincidencias/total_filas)*100
    return error

##############################################################################
############# Programa principal #############################################
##############################################################################

dataD = pd.read_csv('datos_enasem_2021_math.csv')

# Seleccionar columnas específicas
dataD1 = dataD[['AGE_21', 'SEX_21', 'C71A_21', 'C6_21', 'C12_21','C19_21','C25B_21','C26_21','C4_21','C32_21','H3_21','H9_21','C64_21','C49_8_21','C68D_21']]

# Mostrar las primeras filas del DataFrame resultante
#print(dataD1.head())

# Filtrar todas las columnas seleccionadas donde la edad (AGE_21) sea mayor o igual a 60
dataD1 = dataD1[dataD1['AGE_21'] >= 60]

# Filtrar todas las columnas seleccionadas donde las personas no les falta ninguna extremidad
#Pregunta C71A.21 ¿Le falta alguna extremidad o parte de sus piernas o brazos debido a un accidente o enfermedad?
dataD1 = dataD1[dataD1['C71A_21'] != 1]

#Pregunta C12.21 ¿Alguna vez le ha dicho un doctor o personal médico que usted tiene cáncer?
dataD1 = dataD1[dataD1['C12_21'] !=1]

#Pregunta C19.21 ¿Alguna vez le ha dicho un doctor o personal médico que usted tiene alguna enfermedad respiratoria, tal como asma o enfisema?
dataD1 = dataD1[dataD1['C19_21'] !=1]

#Pregunta C25B.21 ¿Alguna vez le ha dicho un doctor o personal médico que usted ha tenido: falla cardíaca/insuficiencia cardíaca/falla congestiva del corazón, arritmia, o angina?
dataD1 = dataD1[dataD1['C25B_21'] !=1]

#Pregunta C26.21 ¿Alguna vez le ha dicho un doctor o personal médico que usted ha tenido una embolia cerebral, derrame cerebral o isquemia cerebral transitoria?
dataD1 = dataD1[dataD1['C26_21'] !=1]

#Pregunta C4.21 ¿Alguna vez le ha dicho un doctor o personal médico que usted tiene hipertensión o presión alta?
dataD1 = dataD1[dataD1['C4_21'] !=1]

#Pregunta C32.21 ¿Alguna vez le ha dicho un doctor o personal médico que usted tiene artritis o reumatismo?
dataD1 = dataD1[dataD1['C32_21'] !=1]


##############################################################################
#Preguntas seleccionadas:
# H3_21     ->  ¿Tiene alguna dificultad en caminar una cuadra?
# H9_21     ->  ¿Tiene alguna dificultad en subir o extender los brazos más arriba de los hombros?
# C64_21    ->  ¿Comparado con hace dos años, usted ha perdido de peso ?
# C49_8_21  ->  ¿La mayor parte del tiempo se ha sentido cansado?
# C68D_2    ->  ¿Ha tenido sed intensa frecuentemente? 
##############################################################################


############### Cnjunto de datos modelo Nº 1 ################################
dataset1 = dataD1[["H3_21","C64_21", "C49_8_21", "C68D_21","C6_21"]]

 # Drop rows where the column values are not 1 or 2
dataset1 = dataset1[dataset1['H3_21'].isin([1, 2])]
dataset1 = dataset1[dataset1['C64_21'].isin([1, 2])]
dataset1 = dataset1[dataset1['C49_8_21'].isin([1, 2])]
dataset1 = dataset1[dataset1['C68D_21'].isin([1, 2])]
dataset1 = dataset1[dataset1['C6_21'].isin([1, 2])]

############### Cnjunto de datos modelo Nº 2  ################################
dataset2 = dataD1[['H9_21',"C64_21", "C49_8_21", "C68D_21","C6_21"]]

 # Drop rows where the column values are not 1 or 2
dataset2 = dataset2[dataset2['H9_21'].isin([1, 2])]
dataset2 = dataset2[dataset2['C64_21'].isin([1, 2])]
dataset2 = dataset2[dataset2['C49_8_21'].isin([1, 2])]
dataset2 = dataset2[dataset2['C68D_21'].isin([1, 2])]
dataset2 = dataset2[dataset2['C6_21'].isin([1, 2])]

############3Cnjunto de datos modelo Nº 3 ####################
dataset3 = dataD1[["C64_21", "C49_8_21", "C68D_21","C6_21"]]

 # Drop rows where the column values are not 1 or 2
dataset3 = dataset3[dataset3['C64_21'].isin([1, 2])]
dataset3 = dataset3[dataset3['C49_8_21'].isin([1, 2])]
dataset3 = dataset3[dataset3['C68D_21'].isin([1, 2])]
dataset3 = dataset3[dataset3['C6_21'].isin([1, 2])]


############Conjunto de datos modelo Nº 4 ####################
dataset4 = dataD1[["C64_21", "C49_8_21", "C6_21"]]

 # Drop rows where the column values are not 1 or 2
dataset4 = dataset4[dataset4['C64_21'].isin([1, 2])]
dataset4 = dataset4[dataset4['C49_8_21'].isin([1, 2])]
dataset4 = dataset4[dataset4['C6_21'].isin([1, 2])]

############### Cnjunto de datos modelo Nº 5 ################################
dataset5 = dataD1[["H3_21", 'H9_21', "C64_21", "C49_8_21", "C68D_21","C6_21"]]

 # Drop rows where the column values are not 1 or 2
dataset5 = dataset5[dataset5['H3_21'].isin([1, 2])]
dataset5 = dataset5[dataset5['H9_21'].isin([1, 2])]
dataset5 = dataset5[dataset5['C64_21'].isin([1, 2])]
dataset5 = dataset5[dataset5['C49_8_21'].isin([1, 2])]
dataset5 = dataset5[dataset5['C68D_21'].isin([1, 2])]
dataset5 = dataset5[dataset5['C6_21'].isin([1, 2])]

########################################################################
########################### z-score ####################################
data_set_age = dataD[['AGE_21', 'C6_21']]
data_set_age = data_set_age[data_set_age['C6_21'].isin([1])]


# Seleccionar las columnas relevantes y filtrar el Grupo 1
data_set_age = dataD[['AGE_21', 'C6_21']]
group_1 = data_set_age[data_set_age['C6_21'] == 1]

# Obtener las proporciones muestrales
p1 = len(group_1) / len(data_set_age)
p2 = 1 - p1  # Ya que estamos asumiendo que solo hay dos grupos

# Calcular la proporción combinada
p_combined = (len(group_1) + 0) / len(data_set_age)  # Aquí, 0 representa la proporción del Grupo 2

# Calcular el error estándar
SE = np.sqrt(p_combined * (1 - p_combined) * (1 / len(group_1) + 1 / (len(data_set_age) - len(group_1))))

# Calcular el z-score
z_score = (p1 - p2) / SE

# Nivel de significancia
alpha = 0.05

# Calcular el valor p bilateral
p_value = 2 * (1 - stats.norm.cdf(np.abs(z_score)))

# Obtener el valor crítico z para el nivel de significancia dado
z_critical = stats.norm.ppf(1 - alpha / 2)

# Imprimir los resultados
print("Proporción muestral del Grupo 1:", p1)
print("Proporción muestral del Grupo 2:", p2)
print("Z-score:", z_score)
print("Valor p:", p_value)

# Comparar con el valor crítico y tomar una decisión
if np.abs(z_score) > z_critical or p_value < alpha:
    print("Se rechaza la hipótesis nula: hay una diferencia significativa entre las proporciones de los dos grupos.")
else:
    print("No se puede rechazar la hipótesis nula: no hay suficiente evidencia para afirmar que hay una diferencia significativa entre las proporciones de los dos grupos.")


# Prueba de hipotesis z-score de diferencia de proporción
# datos categorios
# Mujeres y hombres 
# Tomar dos grupos y evaluar 3 diferentes sintomas 

########################################################################
########################################################################
#Preguntas seleccionadas:
# H3_21     ->  ¿Tiene alguna dificultad en caminar una cuadra?
# H9_21     ->  ¿Tiene alguna dificultad en subir o extender los brazos más arriba de los hombros?
# C64_21    ->  ¿Comparado con hace dos años, usted ha perdido de peso ?
# C49_8_21  ->  ¿La mayor parte del tiempo se ha sentido cansado?
# C68D_2    ->  ¿Ha tenido sed intensa frecuentemente? 
########################################################################
########################################################################
# Separar los datos en atributos (X) y etiquetas (Y) y generar árbol de decisiones

columnas_seleccionadas_1 = ["H3_21", "C64_21", "C49_8_21", "C68D_21"]
columnas_seleccionadas_2 = ["H9_21", "C64_21", "C49_8_21", "C68D_21"]
columnas_seleccionadas_3 = ["C64_21", "C49_8_21", "C68D_21"]
columnas_seleccionadas_4 = ["C64_21", "C49_8_21"]
columnas_seleccionadas_5 = ["H3_21", "H9_21", "C64_21", "C49_8_21", "C68D_21"]


X_model1 = dataset1[columnas_seleccionadas_1]
X_model2 = dataset2[columnas_seleccionadas_2]
X_model3 = dataset3[columnas_seleccionadas_3]
X_model4 = dataset4[columnas_seleccionadas_4]
X_model5 = dataset5[columnas_seleccionadas_5]


Y_model1 = dataset1[['C6_21']]
Y_model2 = dataset2[['C6_21']]
Y_model3 = dataset3[['C6_21']]
Y_model4 = dataset4[['C6_21']]
Y_model5 = dataset5[['C6_21']]

##### Predicción del modelo N° 1 #####
print("\nMdelo Nº 1:\n ")
calcular_indiscernibilidad(columnas_seleccionadas_1, dataset1)
DeTreeClf_model1 = GenerateDecisionTree(X_model1, Y_model1)
y_pred_model1 = DeTreeClf_model1.predict(X_model1)
dataset1['prediction_model1']= y_pred_model1
error_model1 = calcularError(dataset1['prediction_model1'], dataset1 )
print("Error modelo Nº 1: ", error_model1)

###### Predicción del modelo N° 2 #####
print("\nMdelo Nº 2: \n")
calcular_indiscernibilidad(columnas_seleccionadas_2, dataset2)
DeTreeClf_model2 = GenerateDecisionTree(X_model2, Y_model2)
y_pred_model2 = DeTreeClf_model2.predict(X_model2)
dataset2['prediction_model2']= y_pred_model2
error_model2 = calcularError(dataset2['prediction_model2'], dataset2 )
print("Error modelo Nº 2: ", error_model2)

###### Predicción del modelo N° 3 #####
print("\nMdelo Nº 3: \n")
calcular_indiscernibilidad(columnas_seleccionadas_3, dataset3)
DeTreeClf_model3 = GenerateDecisionTree(X_model3, Y_model3)
y_pred_model3 = DeTreeClf_model3.predict(X_model3)
dataset3['prediction_model3']= y_pred_model3
error_model3 = calcularError(dataset3['prediction_model3'], dataset3 )
print("Error modelo Nº 3: ", error_model3)

###### Predicción del modelo N° 4 #####
print("\nMdelo Nº 4: \n")
calcular_indiscernibilidad(columnas_seleccionadas_4, dataset4)
DeTreeClf_model4 = GenerateDecisionTree(X_model4, Y_model4)
y_pred_model4 = DeTreeClf_model4.predict(X_model4)
dataset4['prediction_model4']= y_pred_model4
error_model4 = calcularError(dataset4['prediction_model4'], dataset4 )
print("Error modelo Nº 4: ", error_model4)

###### Predicción del modelo N° 5 #####
print("\nMdelo Nº 5: \n")
calcular_indiscernibilidad(columnas_seleccionadas_5, dataset5)
DeTreeClf_model5 = GenerateDecisionTree(X_model5, Y_model5)
y_pred_model5 = DeTreeClf_model5.predict(X_model5)
dataset5['prediction_model5']= y_pred_model5
error_model5 = calcularError(dataset5['prediction_model5'], dataset5 )
print("Error modelo Nº 5: ", error_model5)



########################################################################
################ Usar dataset original para la predicción ############## 

X_dataD1_model1 = dataD1[columnas_seleccionadas_1]
y_dataD1_pred_model1 = DeTreeClf_model1.predict(X_dataD1_model1)
dataD1['prediction_model1']= y_dataD1_pred_model1
error_model1 = calcularError(dataD1['prediction_model1'], dataD1 )
dataD1['error_model1']= error_model1

X_dataD1_model2 = dataD1[columnas_seleccionadas_2]
y_dataD1_pred_model2 = DeTreeClf_model2.predict(X_dataD1_model2)
dataD1['prediction_model2']= y_dataD1_pred_model2
error_model2 = calcularError(dataD1['prediction_model2'], dataD1 )
dataD1['error_model2']= error_model2

X_dataD1_model3 = dataD1[columnas_seleccionadas_3]
y_dataD1_pred_model3 = DeTreeClf_model3.predict(X_dataD1_model3)
dataD1['prediction_model3']= y_dataD1_pred_model3
error_model3 = calcularError(dataD1['prediction_model3'], dataD1 )
dataD1['error_model3']= error_model3

X_dataD1_model4 = dataD1[columnas_seleccionadas_4]
y_dataD1_pred_model4 = DeTreeClf_model4.predict(X_dataD1_model4)
dataD1['prediction_model4']= y_dataD1_pred_model4
error_model4 = calcularError(dataD1['prediction_model4'], dataD1 )
dataD1['error_model4']= error_model4

X_dataD1_model5 = dataD1[columnas_seleccionadas_5]
y_dataD1_pred_model5 = DeTreeClf_model5.predict(X_dataD1_model5)
dataD1['prediction_model5']= y_dataD1_pred_model5
error_model5 = calcularError(dataD1['prediction_model5'], dataD1 )
dataD1['error_model5']= error_model5

decision_tree_rules1 = export_text(DeTreeClf_model1, feature_names=columnas_seleccionadas_1)
print("Reglas de decisión Modelo 1:")
print(decision_tree_rules1)

decision_tree_rules2 = export_text(DeTreeClf_model2, feature_names=columnas_seleccionadas_2)
print("Reglas de decisión Modelo 2:")
print(decision_tree_rules2)

decision_tree_rules3 = export_text(DeTreeClf_model3, feature_names=columnas_seleccionadas_3)
print("Reglas de decisión Modelo 3:")
print(decision_tree_rules3)

decision_tree_rules4 = export_text(DeTreeClf_model4, feature_names=columnas_seleccionadas_4)
print("Reglas de decisión Modelo 4:")
print(decision_tree_rules4)

decision_tree_rules5 = export_text(DeTreeClf_model5, feature_names=columnas_seleccionadas_5)
print("Reglas de decisión Modelo 5:")
print(decision_tree_rules5)

##################################################################
#################################################################
############## Gererar archivo .csv #############################

#csv_filename = 'dataset_results.csv'
#dataD1.to_csv(csv_filename, index=True)  # Set index=False to not write row indices to the CSV file
#print(f"CSV file '{csv_filename}' has been generated successfully.")

datasets_dir = r"c:/users/tinti/appdata/roaming/python/python310/site-packages" #Esto es el directorio en el que se instalo el modulo de datasets, lo tienes que cambiar puesto que sera diferente en tu PC, avisame para hacerlo
import sys #Importamos el modulo sys, usado para proveer acceso a algunas variables usadas o mantenidas por el intérprete y a funciones que interactúan fuertemente con el intérprete
sys.path.append(datasets_dir) #Agregamos el directorio donde se instalo el modulo 'datasets' a nuestro PATH. Esto es el lugar donde Python encuentra todas sus librerias, funciones y componentes necesarios para funcionar
import numpy as np #Importamos el modulo de Numpy, y lo abreviamos como 'np'
from datasets import load_dataset #Desde el modulo de 'datasets' solo importamos el metodo 'load_dataset' que es usado para cargar los sets de datos

dataset = load_dataset("mstz/heart_failure") #Declaramos una variable 'dataset' la cual guardara la informacion del conjunto de datos "mstz/heart_failure"

data = dataset["train"] #En la variable 'data' guardamos solo la parte de la data que nos importa 

array = np.array(data["age"]) #Creamos una variable 'array' donde guardaremos todos los datos correspondientes a la edad ('age') del conjunto de datos, y a su vez, lo convertimos en un arreglo de Numpy

print(np.average(array)) #Imprimimos por pantalla el promedio calculado mediante la funcion 'np.average()'

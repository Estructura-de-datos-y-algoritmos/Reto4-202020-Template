"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """

import config as cf
import os
from App import model
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________
def init():
    analyzer = model.newAnalyzer()
    return analyzer

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________


def loadFile(analyzer):
    
    for filename in os.listdir(cf.data_dir):
        if filename.endswith('.csv'):
            print('Cargando archivo: ' + filename)
            loadData(analyzer, filename)
    return analyzer




def loadData(analyzer, tripFile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    tripFile = cf.data_dir + tripFile
    input_file = csv.DictReader(open(tripFile, encoding="utf-8"),
                                delimiter=",")
    for trip in input_file:
        model.addTrip(analyzer, trip)
        model.addAge(analyzer, trip)
    return analyzer


def totalConnections(analyzer):
    return model.totalConnections(analyzer)


def totalStops(analyzer):

    return model.totalStops(analyzer)

def connectedComponents(analyzer):

    return model.connectedComponents(analyzer)


def inician(analyzer, edad):

    return model.inician(analyzer, edad)


def rutaCircular(analyzer, time, identificador):

    return model.rutaCircular(analyzer, time, identificador)


def estacionCritica(analyzer):

    return model.estacionCritica(analyzer)

def estacionCriticaSalida(analyzer):

    return model.estacionCriticaSalida(analyzer)

def estacionCriticaSinuso(analyzer):

    return model.estacionCriticaSinuso(analyzer)


def coordenadas(analyzer, first_ll, last_ll):
    return model.coordenadas(analyzer, first_ll, last_ll)



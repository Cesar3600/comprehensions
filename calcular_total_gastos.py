'''
Para resolver este desafío, debes utilizar el archivo data.csv que contiene los datos de los gastos de una empresa. El archivo tiene dos columnas: el nombre del área y el total de gastos del año.

Tu reto es implementar la función read_csv que lee el archivo CSV y calcula el total de gastos de la empresa. Para leer el archivo CSV, puedes utilizar la función open y el módulo csv de Python. Una vez que hayas leído los datos, puedes calcular el total de gastos implementando la lógica que consideres necesaria.
'''

import csv

def read_csv(file_path):
    total=0
    with open(file_path,'r') as fileCsv:
        FileReader = csv.reader(fileCsv,delimiter=',')
        for area in FileReader:
            total += int(area[1])
    return total


path='./data.csv'
if(__name__ == "__main__"):
    read_csv(path)
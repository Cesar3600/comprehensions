
import csv

def read_csv(file_path):
    csv_file = open(file_path,'r')
    reader = csv.reader(csv_file,delimiter=',')
    print(list(reader))


path = './data.csv'
read_csv(path)



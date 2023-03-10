'''
import csv

def reader_csv(csv_path):
    with open(csv_path,'r') as CSV_file:
        CSV_reader = csv.reader(CSV_file,delimiter=',')
        for row in CSV_reader:
            print('*'*33)
            print(row)


if __name__ =="__name__":
    reader_csv('./app/data.csv')
'''


import csv

def reader_csv(csv_path):
    with open(csv_path,'r') as CSV_file:
        CSV_reader = csv.reader(CSV_file,delimiter=',')
        header = next(CSV_reader)
        data =[]
        for row in CSV_reader:
            iterable = zip(header,row)
            country_dict = {key:value for key,value in iterable}
            data.append(country_dict)
        return data


if __name__ =="__main__":
    data = reader_csv('./app/data.csv')
    print(data[0])

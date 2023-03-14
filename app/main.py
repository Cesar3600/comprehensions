
import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('./app/data.csv')
  country = input('Tipea tu pais => ')

  country_info = utils.population_by_country(data,country)
  print('DATA!!!!!!!!!!!')


  if len(country_info) > 0:
    country = country_info[0]
    labels,values = utils.get_population(country)
    #mr = list(labels)
    #print(mr)
    #print(values)
    #labels = ['2022','2023']
    #values = [100000,200000]
    return charts.generate_bar_chart(labels, values)


if __name__ == '__main__':
  run()

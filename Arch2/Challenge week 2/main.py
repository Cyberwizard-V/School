import matplotlib.pyplot as plt
from functions import *
import statistics

#Make nodes with API https://api.basecampserver.tech/nodes
#KEY: bKkUQatjtDu7fIwiOpl8uA
#ID:  444
#Make post request to create node

weather = get_sensor_data()
weather = sorted(weather, key=lambda e: (e['timestamp']))

lengthJSON = len(get_sensor_data()) - 1
print(lengthJSON)
def show_all_data():
  count = 10
  print(f'''            Show all data             ''')
  print(f'''######################################''')
  print(f'''[Time]  [Temp]  [Humidity]  [pressure]''')
  while True:
    count += 1
    xTime = weather[count]['timestamp']
    xTemp = weather[count]['temperature']
    xHumi = weather[count]['humidity']
    xPres = weather[count]['pressure']
    print(f'''{xTime}   {xTemp}°C     {xHumi}% Ph20      {xPres}Milibars ''')
    if count == lengthJSON:
      break

def show_recent_data():
  print(f'''            Show Recent data             ''')
  print(f'''######################################''')
  print(f'''[Time]  [Temp]  [Humidity]  [pressure]''')
  xTime = weather[lengthJSON]['timestamp']
  xTemp = weather[lengthJSON]['temperature']
  xHumi = weather[lengthJSON]['humidity']
  xPres = weather[lengthJSON]['pressure']
  print(f'''{xTime}   {xTemp}°C     {xHumi}% Ph20      {xPres}Milibars ''')


def average_data():
  averageTemp = []
  averageHumi = []
  averagePres = []
  count = 14
  print(f'''            Standard deviation        ''')
  print(f'''######################################''')
  print(f'''[Temp]  [Humidity]  [pressure]''')
  while True:
    count += 1
    #Average Temperature
    averageTemp.append(weather[count]['temperature'])
    #Calculate average
    t = round(sum(averageTemp) / len(averageTemp), 2)

    #Average Humidity
    averageHumi.append(weather[count]['humidity'])
    #Calculate average
    h = round(sum(averageHumi) / len(averageHumi), 2)

    #Average Humidity
    averagePres.append(weather[count]['pressure'])
    #Calculate average
    p = round(sum(averagePres) / len(averagePres), 2)

    if count == lengthJSON:
      break

  print(f'''{t}°C     {h}% Ph20      {p}Milibars ''')


def deviation_data():
  averageTemp = []
  averageHumi = []
  averagePres = []
  count = 14
  print(f'''            Average  data             ''')
  print(f'''######################################''')
  print(f'''[Temp]  [Humidity]  [pressure]''')
  while True:
    count += 1
    averageTemp.append(weather[count]['temperature'])
    averageHumi.append(weather[count]['humidity'])
    averagePres.append(weather[count]['pressure'])


    if count == lengthJSON:
      break

  t = statistics.stdev(averageTemp)
  h = statistics.stdev(averageHumi)
  p = statistics.stdev(averagePres)
  print(f'''{round(t,3)}°C     {round(h,3)}% Ph20      {round(p,3)}Milibars ''')

def graph_data():
  averageTemp = []
  averageHumi = []
  averagePres = []
  time_list = []
  count = 14
  while True:
    count += 1
    #Average Temperature
    averageTemp.append(weather[count]['temperature'])

    #Average Humidity
    averageHumi.append(weather[count]['humidity'])

    #Average Humidity
    averagePres.append(weather[count]['pressure'])

    time_list.append(weather[count]['timestamp'])
    if count == lengthJSON:
      break
  plt.figure(figsize=(15,10))
  plt.subplot(131)
  plt.plot(time_list,averageTemp)
  plt.ylabel("°C")
  plt.xlabel("time")
  plt.title('Temperature')
  plt.subplot(132)
  plt.plot(time_list,averageHumi)
  plt.ylabel(f"% Ph20 h20 molecules")
  plt.xlabel("time")
  plt.title('Humidity')

  plt.subplot(133)
  plt.plot(time_list,averagePres)
  plt.ylabel("Milibars")
  plt.xlabel("time")
  plt.title('Pressure')
  plt.show()


def min_val():
  weather1 = get_sensor_data()
  weather1 = sorted(weather, key=lambda e: (e['temperature']))
  mintemp = weather1[0]["temperature"]
  weather1 = sorted(weather, key=lambda e: (e['humidity']))
  minhum = weather1[0]["humidity"]
  weather1 = sorted(weather, key=lambda e: (e['pressure']))
  minpres = weather1[0]["pressure"]

  print(f'''         Show Minuimum data           ''')
  print(f'''######################################''')
  print(f'''  [Temp]  [Humidity]  [pressure]''')
  print(f'''  {mintemp}°C    {minhum}% Ph20       {minpres}Milibars''')


def max_val():
  weather1 = get_sensor_data()
  weather1 = sorted(weather, key=lambda e: (-e['temperature']))
  mintemp = weather1[0]["temperature"]
  weather1 = sorted(weather, key=lambda e: (-e['humidity']))
  minhum = weather1[0]["humidity"]
  weather1 = sorted(weather, key=lambda e: (-e['pressure']))
  minpres = weather1[0]["pressure"]

  print(f'''         Show Maximum data           ''')
  print(f'''######################################''')
  print(f'''  [Temp]  [Humidity]  [pressure]''')
  print(f'''  {mintemp}°C    {minhum}% Ph20       {minpres}Milibars''')

def main():
  print('''
  Select a input
  [1] : Show all data
  [2] : Show average weather data
  [3] : Show most recent weather data
  [4] : Show graph of all data

  > Max - Min
  [5] : Show minimum values
  [6] : Show maximum values
  [7] : Show standard deviation

  X : Exit


  ''')
  userInput = input("").upper()
  if userInput == "1":
    show_all_data()
  elif userInput == "2":
    average_data()
  elif userInput == "3":
    show_recent_data()
  elif userInput == "4":
    graph_data()
  elif userInput == "5":
    min_val()
  elif userInput == "6":
    max_val()
  elif userInput == "7":
    deviation_data()
  elif userInput == "X":
    quit()


if __name__ == "__main__":

  while True:
    main()
    input("Press enter to continue...")
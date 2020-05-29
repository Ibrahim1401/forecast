import json
import requests,datetime

def Date_Check(data_set):
    Dates = []
    diff = []
    for data in data_set['list']:
	Dates.append(int(i['dt_txt'].split(" ")[0].split("-")[2]))
    Dates = sorted(list(set(Dates)))
    for res in range(len(Dates)-1):
	diff.append(Dates[res+1] - Dates[res])
    return 1 if (max(diff) == 1 and len(Dates) == 4) else 0

def Hour_Check(data_set):
    d_time = {}
    for time in data_set['list']:
	date = time['dt_txt'].split(" ")[0]
	if time not in d_time.keys():
	   d_time[date] = []
	   d_time[date].append(time['dt_txt'])
	else:
	   d_time[date].append(time['dt_txt'])
    time_diff = []
    for values in d_time.values:
	for tm in range(len(values)-1):
	    diff = datetime.datetime.strptime(d_time[tm+1],'%Y-%m-%d %H:%M:%S') - datetime.datetime.strptime(d_time[tm],'%Y-%m-%d %H:%M:%S')
	    time_diff = int(diff.seconds // (60*60))
    return 1 if (max(time_diff) == 1) else 0

def Temp_Check(data_set):
    for data in data_set['list']:
	if data['main']['temp'] < data['main']['temp_min'] or data['main']['temp'] > data['main']['temp_max']:
	   return 0 
	else:
	   continue
    return 1

def Description(data_set):
    for data in data_set:
	for weath in data['weather']:
	    if weath['id'] == 800:
		print ("Light Rain")
	    else:
		print ("Clear Sky")
        
if__name__=="__main__":
    data = requests.get("https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22")
    data_set = data.content
    data_set = json.loads(data_set)
    Date_Check_Result = Date_Check(data_set)
    if Date_Check_Result == 1:
       print ("The Data_Set contains consecutive 4 days of data")
    Hour_check_result = Hour_Check(data_set)
    if Hour_check_result == 1:
	print ("The Forecast is in hourly manner")
    Temp_Check_res = Temp_Check(data_set)
    if Temp_Check_res == 1:
	print ("The temperature is accurate that is not less than min temp and not greater than max temp")
    Description(data_set)
    

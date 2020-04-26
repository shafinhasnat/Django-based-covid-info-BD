import numpy as np
import pickle 
import csv
#loading the dumped files
def forcast():
    loaded_cases=pickle.load(open('covidPr_app/static/ess/model_cases.pkl','rb'))
    loaded_deaths=pickle.load(open('covidPr_app/static/ess/model_deaths.pkl','rb'))
    case_pred = abs(int((loaded_cases[0]-loaded_cases[1])[0]))
    death_pred = abs(int((loaded_deaths[0]-loaded_deaths[1])[0]))
    return case_pred, death_pred

def predictionGraph():
    loaded_cases_plus_pred=pickle.load(open('covidPr_app/static/ess/model_cases_plus_pred.pkl','rb'))
    loaded_deaths_plus_pred=pickle.load(open('covidPr_app/static/ess/model_deaths_plus_pred.pkl','rb'))
    pred_death = []
    pred_case = [] 
    for i in loaded_deaths_plus_pred:
        pred_death.append(int(i[0]))
    pred_death[:0] = [0,0,0,0,0,0,0,0,0,0]
    for i in loaded_cases_plus_pred:
        pred_case.append(int(i[0]))
    return pred_death, pred_case

def division():
    num = []
    with open('covidPr_app/static/ess/division.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i in csv_reader:
            num.append(int(i[1]))
    return num

def district():
    name = []
    case = []
    lat = []
    lon = []
    with open('covidPr_app/static/ess/district.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i in csv_reader:
            name.append(str(i[0]))
            case.append(int(i[1]))
            lat.append(float(i[2]))
            lon.append(float(i[3]))
    return name, case, lat, lon
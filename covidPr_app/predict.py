import numpy as np
import pickle 

#loading the dumped files
def forcast():
	loaded_cases=pickle.load(open('covidPr_app/static/ess/model_cases.pkl','rb'))
	loaded_deaths=pickle.load(open('covidPr_app/static/ess/model_deaths.pkl','rb'))
	case_pred = loaded_cases[0][0]
	death_pred = loaded_deaths[0][0]
	return int(case_pred), int(death_pred)

def predictionGraph():
    loaded_cases_plus_pred=pickle.load(open('covidPr_app/static/ess/model_cases_exp.pkl','rb'))
    loaded_deaths_plus_pred=pickle.load(open('covidPr_app/static/ess/model_deaths_exp.pkl','rb'))
    pred_death = []
    pred_case = [] 
    for i in loaded_deaths_plus_pred:
        pred_death.append(int(i[0]))
    pred_death[:0] = [0,0,0,0,0,0,0,0,0,0]
    for i in loaded_cases_plus_pred:
        pred_case.append(int(i[0]))
    return pred_death, pred_case
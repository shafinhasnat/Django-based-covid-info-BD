import numpy as np
import pickle 

#loading the dumped files
def forcast():
	loaded_cases=pickle.load(open('covidPr_app/static/ess/model_cases.pkl','rb'))
	loaded_deaths=pickle.load(open('covidPr_app/static/ess/model_deaths.pkl','rb'))
	case_pred = loaded_cases[0][0]
	death_pred = loaded_deaths[0][0]
	return int(case_pred), int(death_pred)
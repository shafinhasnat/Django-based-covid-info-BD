from django.shortcuts import render
from .models import CovidData
from .predict import forcast, predictionGraph
# Create your views here.

def home(request):
	title='Home'
	data = CovidData.objects.all()
	latest_data = CovidData.objects.order_by('-pk')[0]
	latest_death = abs(int(CovidData.objects.order_by('-pk')[1].death)-int(CovidData.objects.order_by('-pk')[0].death))
	latest_case = abs(int(CovidData.objects.order_by('-pk')[1].case)-int(CovidData.objects.order_by('-pk')[0].case))
	latest_recover = abs(int(CovidData.objects.order_by('-pk')[1].recover)-int(CovidData.objects.order_by('-pk')[0].recover))
	case_pred, death_pred = forcast()
	# case_pred = abs(int(case_pred_total)-int(latest_data.case))
	# death_pred = abs(int(death_pred_total)-int(latest_data.death))

	pred_death, pred_case = predictionGraph()
	# print(case_pred, death_pred)
	return render(request, 'home.html', {'data': data, 'title': title,
	 'latest_data': latest_data, 'latest_case': latest_case,
	  'latest_death': latest_death, 'latest_recover': latest_recover, 
	  'case_pred': case_pred, 'death_pred': death_pred, 'pred_death': pred_death, 'pred_case': pred_case})
	

def details(request):
	title = 'Detailed data in Bandladesh'
	data = CovidData.objects.all()
	return render(request, 'details.html', {'title': title, 'data': data})

def about(request):
	title = 'About'
	return render(request, 'about.html', {'title': title})
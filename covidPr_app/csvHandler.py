import csv
from django.shortcuts import render
from django.db import connection
def csvH():
	date = []
	case = []
	death = []
	recover = []
	with open('static/ess/COVID-19_in_bangladesh.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			date.append(row[0])
			case.append(row[1])
			death.append(row[2])
			recover.append(row[3])
	date.remove('Date')
	case.remove('cases')
	death.remove('deaths')
	recover.remove('Recovered')
	case = list(map(int, case))
	death = list(map(int, death))
	recover = list(map(int, recover))
	return date, case, death, recover

	# print('Date:', date)
	# print('Case:', case)
	# print('Death:', death)
	# print('Recover:', recover)

dates, cases, deaths, recovers = csvH()

for i, j, k, l in zip(dates, cases, deaths, recovers):
	print(i,j,k,l)
	pass

import psycopg2
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "19971904",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "covidpred")

    cursor = connection.cursor()
    for i, j, k, l in zip(dates, cases, deaths, recovers):
    	command = '''INSERT INTO "covidPr_app_coviddata" (date, "case", death, recover) VALUES ('{}', {}, {}, {});'''.format(i,j,k,l)
    	cursor.execute(command)
    	connection.commit()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
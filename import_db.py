import csv
import random
from PS2.models import *
with open("data.csv") as f:
	reader=csv.reader(f)
	for row in reader:
		created=UserIdPassword.objects.get_or_create(
			user_id=row[1],
			pwd=random.randint(0,999999),
			token=0,
			)
		created=Mentor.objects.get_or_create(
			mentor_name=row[4],
			mentor_id=row[5],
			mentor_contact=row[6],
			mentor_email=row[7],
			)
		created=Station.objects.get_or_create(
			mentor=Mentor.objects.get(mentor_id=row[5]),
			station_name=row[2],
			station_address=row[3],
			)
		created = Student.objects.get_or_create(
			station=Station.objects.get(station_name=row[2]),
			student_id=row[0],
			student_name=row[1],
			# student_contact=row[],
			# student_email=row[],
			)

import csv
from chaf.threads.models import BirthRegistration, MarriageRegistration

def load_data():
	data_file = '/Users/tim/mycode/chaf-django/chaf/chaf/threads/data/threads.csv'
	with open(data_file, 'rb') as csv_file:
		reader = csv.DictReader(csv_file)
		for row in reader:
			if row['Event'] == 'B':
				event = BirthRegistration(
						reg_year = row['Registration year'],
						index_child_firstname = row['Given name(s)'],
						index_child_surname = row['Surname'],
						index_father_firstname = row['Father / Spouse surname'],
						index_mother_firstname = row['Mother / Spouse given name(s)'],
						index_year = row['Index year'],
						index_registration_place = row['Place of registration']
					)
			elif row['Event'] == 'M':
				event = MarriageRegistration(
						reg_year = row['Registration year'],
						index_spouse1_firstname = row['Given name(s)'],
						index_spouse1_surname = row['Surname'],
						index_spouse2_surname = row['Father / Spouse surname'],
						index_spouse2_firstname = row['Mother / Spouse given name(s)'],
						index_year = row['Index year'],
						index_registration_place = row['Place of registration']
					)
			if not row['Registration number'] and row['Volume reference']:
				event.reg_number = row['Volume reference']
			elif row['Registration number']:
				event.reg_number = row['Registration number']
			event.save()
import json
import os

import frappe
from erpnext.setup.setup_wizard.utils import complete
from frappe.desk.page.setup_wizard.setup_wizard import make_records

records = json.loads(open(os.path.expanduser('~/projects/frappe/records.json')).read())

print('Setup Wizard')
complete()

for record in records:
	try:
		exists = frappe.db.exists(record)
		if not exists:
			print('Creating ' + record['doctype'])
			make_records([record])
			frappe.db.commit()
		else:
			print('Skipping ' + record['doctype'])
	except Exception as e:
		print('Failed ' + record['doctype'])
		print(str(e))
	# print('Failed ' + str(e))


from pypika import Query, Table, Field
from frappe.query_builder.functions import Count
from frappe.utils import get_datetime, now_datetime


hsu = 'Healthcare Service Unit'
filters = {'company': 'For Testing', 'parent_healthcare_service_unit': None}
filterss = {'company': 'For Testing', 'parent_healthcare_service_unit': ''}


# settings
hr_settings = frappe.get_doc("HR Settings")
hr_settings.standard_working_hours = 2
hr_settings.save()


holiday_list = frappe.get_doc('Holiday List', 'weekends')
company = frappe.get_doc('Company', 'AvilPage')
company.default_holiday_list = holiday_list.name
# company.default_currency = "INR"
# company.save()


frappe.db.commit()

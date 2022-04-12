import json
import sys

import frappe
import requests
from frappe.utils.install import complete_setup_wizard
from frappe.desk.page.setup_wizard.setup_wizard import make_records


print('Setup Wizard')
complete_setup_wizard()


def fetch_records():
    try:
        json_file = sys.argv[1]
    except:
        json_file = '/tmp/records.json'
        json_url = 'https://raw.githubusercontent.com/ChillarAnand/frappe_init/main/records.json'
        response = requests.get(json_url)
        with open(json_file, 'w') as fh:
            fh.write(response.text)

    records = json.loads(open(json_file).read())
    return records


def create_records(records):
    for record in records:
        frappe.db.commit()
        try:
            if record.get('name'):
                exists = frappe.db.exists(record['doctype'], record['name'])
            else:
                exists = frappe.db.exists(record)
            if not exists:
                print('Creating ' + record['doctype'])
                make_records([record])
                frappe.db.commit()
            else:
                print('Skipping ' + record['doctype'])
        except Exception as e:
            frappe.db.rollback()
            print('Failed ' + record['doctype'])
            print(str(e))


records = fetch_records()
create_records(records)


# settings
hr_settings = frappe.get_doc("HR Settings")
hr_settings.standard_working_hours = 2
hr_settings.save()


holiday_list = frappe.get_doc('Holiday List', 'weekends')

# company = frappe.get_doc('Company', 'AvilPage')
# company.default_holiday_list = holiday_list.name
# company.default_currency = "INR"
# company.save()


frappe.db.commit()

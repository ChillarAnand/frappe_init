### Why Frappe Init?

I create multiple benches/sites for dev/testing purposes everyday. A lot of time is wasted on setup wizard, setting up initial data, tweaking various settings.

This repo helps to automate most of the things.


#### Usage:
This repo has 3 files.

1. records.json - Hand written records for the most used doctypes.

2. ipython.py - This script is used to complete setup, load bootstrap data and tweak settings from bench console.

3. init.py - This script is used to load bootstrap data on a remote site.


#### Quick start

Paste this in a bench console

```py
import requests

script_url = 'https://raw.githubusercontent.com/ChillarAnand/frappe_init/main/ipython.py'
response = requests.get(script_url)
with open('/tmp/ipython.py', 'w') as fh:
	fh.write(response.text)
%run /tmp/ipython.py
```

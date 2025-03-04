#!/usr/bin/env python3
import requests
import passwords
response = requests.get('http://localhost:80/basic-auth/Liam/test',auth=(passwords.USERNAME, passwords.PASSWORD))
print(response.status_code)

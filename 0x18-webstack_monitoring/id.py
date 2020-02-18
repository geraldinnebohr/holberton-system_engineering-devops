from datadog import initialize, api

options = {
    'api_key': '3fc5505397e9e9516cf9eb4cf1fa0235',
    'app_key': 'f904ce0d11b00f160cf8e89ca76084ef89477dbe'
}

initialize(**options)

print(api.Dashboard.get_all())

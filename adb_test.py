from ppadb.client import Client as AdbClient
import json

# Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
device = client.device('e325f4f10dafe932')  #TODO : need to remove hard coded device name here

with open('app_versions.json') as file:
    app_versions = json.load(file)

# for app, version in app_versions.items():
#     print(f"{app} version is {version}")

def list_of_devices():
    """Used to find list of devices. App stops when no 
    devices found.
    """
    pass


def version_check(list_of_apps=app_versions):
    for app, version in list_of_apps.items():
        if device.is_installed("com.omnitracs.diagnostics"):
            diagnostics_version = device.shell("dumpsys package com.omnitracs.diagnostics | grep versionName")
            diagnostics_version = diagnostics_version.split("=")
            print(f"{list_of_apps[app]} app is version {diagnostics_version[1]}", end="")
        else: 
            print("App is not installed.")

def update_check():
    pass



if __name__ == "__main__": 
    version_check()

from adb_exceptions import ZeroDeviceFound, TooManyDevices  # pylint: disable=import-error
import subprocess


def check_available_devices():

    try: 
        p1 = subprocess.run(["adb", "devices"], capture_output=True, text=True)
        captured_devices = [line for line in p1.stdout.split("\n") if line != ""]
        captured_devices.remove(captured_devices[0])
    except FileNotFoundError:
        print("ADB may not be installed in your system. \nPlease install ADB or check if properly configured in system variables")

    # pulling in only device name
    device_list = [device.split("\t")[0] for device in captured_devices]
    device_list = [tuple((index, device)) for index, device in enumerate(device_list, 1)]
    print(device_list)

    # checking to see how many devices
    selected_device = 0
    if len(device_list) == 0:
        raise ZeroDeviceFound("There are no android devices found.")
    elif len(device_list) > 1:
        # TODO: Implement multiple devices feature
        raise TooManyDevices("""\n
    >>> I have currently not implemented this script to accomodate multiple devices.
    >>> Please plug only one device and restart the script.""")
    else: 
        # if only one device just get device in device list
        selected_device = device_list[0]
    return selected_device

    
    


if __name__ == "__main__":
    print(check_available_devices())
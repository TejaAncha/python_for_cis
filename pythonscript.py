from netmiko import ConnectHandler as ch 
from getpass import getpass
userName = input("UserName: ")
password = getpass("password: ")
get_ip = input("provide ip address: ")
device_details = {"device_type":"cisco_ios","ip":get_ip, "username":userName, "password":password}
connect = ch(**device_details)
out = connect.send_command("sh ip int br")
try:
    with open("Device1", "w") as file:
        file.write(out)
except:
    print("No such file found")
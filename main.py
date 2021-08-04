from modl.ip_in import ip_api as ip
from modl.port_info import scan_port
from modl.admin_q import process_find 
web = input("input ur web ( www.example.com ): ")
print("----- ip -----")
val = ip(web)
if val[0] != "result":
    print(val[1])
else:
    print(val[0],":",val[1])
    exit()
print("----- port -----")
print(scan_port(val[0]))
print("---- admin scan ----")
for i in process_find(web):
    print(i)

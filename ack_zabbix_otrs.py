from zabbix_api import ZabbixAPI
import sys, re
 
server = "http://localhost/zabbix"
username = "Admin"              
password = "zabbix"     
 
zapi = ZabbixAPI(server = server)
zapi.login(username, password)

zapi.event.acknowledge({"eventids": sys.argv[1], "message": "Ticket " + str(sys.argv[2]) + " criado no OTRS."})



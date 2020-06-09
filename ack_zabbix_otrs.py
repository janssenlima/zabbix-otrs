#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################
# Autor: Janssen dos Reis Lima - janssenreislima@gmail.com    #
# Objetivo: Fazer o ack no evento automaticamente             #
# Versao: 1.0                                                 #
###############################################################
from zabbix_api import ZabbixAPI
import sys, re

# Parametros de acesso da interface web do Zabbix 
server = "http://localhost/zabbix"
username = "Admin"              
password = "zabbix"     
 
zapi = ZabbixAPI(server = server)
zapi.login(username, password)


zapi.event.acknowledge({"eventids": sys.argv[1], "message": "Ticket " + str(sys.argv[2]) + " criado no OTRS.", "action": 4})
zapi.event.acknowledge({"eventids": sys.argv[1], "action": 2})



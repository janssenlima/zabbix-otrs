# -*- coding: utf-8 -*-
# @author: Janssen Lima - janssenreislima@gmail.com
# ATEN??O: C?digo n?o est? funcional. Em desenvolvimento

from otrs.client import GenericTicketConnector
from otrs.objects import Ticket, Article, DynamicField

server_uri = 'http://localhost/'
webservice_name = 'IntegraZabbix'
client = GenericTicketConnector(server_uri, webservice_name)
user_login = 'user'
password = 'pass'

client.user_session_register(user_login, password)

pega_ticket = client.ticket_search(State=1)

print len(pega_ticket)

pega_ticket = client.ticket_search(Body='<inserir_texto_procura>')

for tickets in pega_ticket:
    print "Ticket: ",tickets


pega_fechados = client.ticket_search(State='new')

df_searchId = DynamicField(Name='ZabbixIdTrigger', Value="13563", Operator='Like')
df_searchState = DynamicField(Name='ZabbixStateTrigger', Value="PROBLEM", Operator='Like')

busca_df=client.ticket_search(Queues='Zabbix', dynamic_fields=[df_searchId, df_searchState])
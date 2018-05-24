#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################
# Autor: Janssen dos Reis Lima - janssenreislima@gmail.com    #
# Objetivo: Abrir e fechar registros no no OTRS via API       #
#           a partir de um problema identificado pelo Zabbix  #
# Versao: 1.0                                                 #
###############################################################

from otrs.ticket.template import GenericTicketConnectorSOAP
from otrs.client import GenericInterfaceClient
from otrs.ticket.objects import Ticket, Article, DynamicField, Attachment
import sys, os


server_uri = 'http://127.0.0.1'
webservice_name = 'IntegraZabbix'
client = GenericInterfaceClient(server_uri, tc=GenericTicketConnectorSOAP(webservice_name))

client.tc.SessionCreate(user_login='alerta', password='123456')

fechar_ticket = Ticket(State='fechado automaticamente')

assunto_artigo_fechado = "Ticket fechado automaticamente atraves do evento " + sys.argv[4]
estado_trigger = sys.argv[6]
artigo_fechar = Article(Subject=assunto_artigo_fechado, Body=assunto_artigo_fechado, Charset='UTF8', MimeType='text/plain')

def abrirTicket():
    corpo = sys.argv[3] + " " + sys.argv[4]
    evento = sys.argv[4]

    t = Ticket(State='new', Priority='3 normal', Queue='Zabbix', Title=sys.argv[1], CustomerUser='root@localhost', Type='Unclassified')

    a = Article(Subject=sys.argv[2], Body=corpo, Charset='UTF8', MimeType='text/plain')

    df1 = DynamicField(Name='ZabbixIdTrigger', Value=sys.argv[5])
    df2 = DynamicField(Name='ZabbixStateTrigger', Value=sys.argv[6])
    df3 = DynamicField(Name='ZabbixEvento', Value=sys.argv[4])

    ticket_id, numero_ticket = client.tc.TicketCreate(t, a, [df1, df2, df3])

    comando = "python /usr/lib/zabbix/externalscripts/ack_zabbix.py " + str(evento) + " " + str(numero_ticket)
    os.system(comando)

def fecharTicket():
    df_searchId = DynamicField(Name='ZabbixIdTrigger', Value=sys.argv[5], Operator='Like')
    df_searchState = DynamicField(Name='ZabbixStateTrigger', Value=sys.argv[6], Operator='Like')
    busca_df=client.tc.TicketSearch(OwnerIDs=2,Queues='Zabbix', dynamic_fields=[df_searchId])
    client.tc.TicketUpdate(ticket_id=busca_df[0], ticket=fechar_ticket, article=artigo_fechar)

if estado_trigger == "OK":
    fecharTicket()
else:
    abrirTicket()

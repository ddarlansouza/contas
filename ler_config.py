# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:12:17 2019

@author: darlan.paulo.d.souza
"""

from configparser import ConfigParser

class Inicial:

    try:
        from configparser import ConfigParser
    except ImportError:
        from ConfigParser import ConfigParser  # ver. < 3.0
            
    def __init__(Self):        
        caminho = r'C:\WorkSpace\Projetos\aula_python'
        arq_ini = r'\config.ini'

       # print('Objeto Criado')
        
        # instantiate
        config = ConfigParser()

        #parse existing file
        config.read(caminho+arq_ini)

        # read values from a section
        versao_db  = config.get('secao', 'versao_db')
        versao_sis = config.get('secao','versao_sis')
        data_sis   = config.get('secao','data_sis')
        db_caminho = config.get('secao','db_caminho')
        db_banco   = config.get('secao','db_banco')

        print(versao_db)
        print(versao_sis)
        print(data_sis)
        print(db_caminho)
        print('Nome do banco :',db_banco)

        if versao_db == '1.00':
            print('Versão Correta!')
        else:
            print('Versao Incorreta!')


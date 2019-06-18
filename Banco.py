# -*- coding: utf-8 -*-

#importando módulo do SQlite
from ler_config import Inicial
import sqlite3

class Banco():
    
    #definição do caminho + banco de dados 
    db_caminho = None  # r'C:\DBDados\SQlite3'
    db_banco   = None  # r'\teste.db'
	
    def __init__(self):
        db_caminho = r'C:\DBDados\SQlite3\teste.db'
        print('Banco de dados - Aqui : ', db_caminho)
        self.ler_configuracao()
        self.conexao = sqlite3.connect(db_caminho)
        self.createTable()
  
    def createTable(self):
        c = self.conexao.cursor()
                 
        c.execute("""create table if not exists usuarios (
                     idusuario integer primary key autoincrement ,
                     nome text,
                     telefone text,
                     email text,
                     usuario text,
                     senha text)""")
        self.conexao.commit()
        c.close()
		
    def ler_configuracao(self):
        print('Aneste de criar o objeto local')
        local = Inicial()
        print('Estou aqui, depois de criar o objeto')
        db_caminho = local.db_caminho
        db_banco   = local.getDbBanco()
        
    

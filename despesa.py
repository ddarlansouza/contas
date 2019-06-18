# -*- coding: utf-8 -*-

class Despesa:

	def __init__(Self, des_sequencia=0, des_codigo="", des_nome=""):
		self.info          = {}
		self.des_sequencia = des_sequencia
		self.des_codigo    = des_codigo
		self.des_nome      = des_nome
		print('Despesa criada!')
 	
	def insertDespesa(self):

		banco = Banco()
		try:
  
			c = banco.conexao.cursor()
  
			c.execute("insert into TB_DESPESA (des_sequencia, des_codigo, des_nome ) values ('" + self.des_sequencia + "', '" + self.des_codigo + "', '" + self.des_nome + "')")
  
			banco.conexao.commit()
			c.close()
  
			return "Despesas cadastrado com sucesso!"
		except:
			return "Ocorreu um erro na inserção da despesa"
			
	def updateDespesa(self):
  
		banco = Banco()
		try:
  
			c = banco.conexao.cursor()
  
			c.execute("update TB_DESPESA set des_sequencia = '" + self.des_sequencia + "',des_codigo = '" + self.des_codigo + "', des_nome = '" + self.des_nome + "' + "' where des_sequencia = " + self.des_codigo + " ")
  
			banco.conexao.commit()
			c.close()
  
			return "Despesa atualizado com sucesso!"
		except:
			return "Ocorreu um erro na alteração da despesa"
  
	def deleteDepesa(self):
  
		banco = Banco()
		try:
  
			c = banco.conexao.cursor()
  
			c.execute("delete from TB_DESPESA where des_codigo = " + self.des_codigo + " ")
  
			banco.conexao.commit()
			c.close()
  
			return "Despesa excluído com sucesso!"
		except:
			return "Ocorreu um erro na exclusão da despesa"
  
	def selectDespesa(self, des_codigo):
		banco = Banco()
		try:
  
			c = banco.conexao.cursor()
  
			c.execute("select * from TB_DESPESA where des_codigo = " + des_codigo + "  ")
  
			for linha in c:
				self.des_sequencia = linha[0]
				self.des_codigo    = linha[1]
				self.des_nome      = linha[2]
  
				c.close()
  
			return "Busca feita com sucesso!"
		except:
			return "Ocorreu um erro na busca da despesa"


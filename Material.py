class Material:
	materiais = {}

	def __init__(self, nome, conteudo):
		self.nome = nome
		self.conteudo = conteudo
		self.bolsista_responsavel = bolsista

	def alterar_nome(self, nome):
		self.nome = nome
	
	def alterar_conteudo(self, conteudo):
		self.conteudo = conteudo


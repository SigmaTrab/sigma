class Aluno:
	alunos = {}

	def __init__(self, nome, endereco, matricula):
		self.nome = nome
		self.endereco = endereco
		self.matricula = matricula

	def alterar_endereco(self, novo_endereco):
		self.endereco = novo_endereco
		
	def alterar_nome(self, novo_nome):
		self.nome = novo_nome
	
	def alterar_matricula(self, novo_matricula):
		self.matricula = novo_matricula

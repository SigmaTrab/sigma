class Aluno:
	alunos = {}

	def __init__(self, nome, endereco, matricula):
		self.nome = nome
		self.endereco = endereco
		self.matricula = matricula


	def alterar_endereco(self, novo_endereco):
		self.endereco = novo_endereco

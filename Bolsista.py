from Aluno import Aluno
from Curso import Curso

class Bolsista(Aluno):
	def __init__(self, Aluno):
		self.nome = Aluno.nome
		self.endereco = Aluno.endereco
		self.matricula = Aluno.matricula
		
	def postar_material(self, nome, conteudo, disciplina):
		um_material = Material(nome, conteudo, self.nome)
		disciplina.incluir_material(um_material)
		return disciplina

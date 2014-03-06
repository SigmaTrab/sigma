class Curso:
	cursos = {}

	def __init__(self, nome, turno):
		self.nome = nome
		self.turno = turno
		self.codigo = Curso.cadastrar(self)
		self.disciplinas = {}

	def incluir_disciplina(self, disciplina):
		self.disciplinas[disciplina.codigo] = disciplina

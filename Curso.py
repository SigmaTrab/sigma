class Curso:
	cursos = {}

	def __init__(self, nome, turno):
		self.nome = nome
		self.turno = turno
		self.codigo = Curso.cadastrar(self)
		self.disciplinas = {}
		self.alunos = {}

	def incluir_disciplina(self, disciplina):
		self.disciplinas[disciplina.codigo] = disciplina
		
	def matricular(self, aluno):
    self.alunos = aluno

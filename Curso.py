class Curso:
	cursos = {}

	def __init__(self, nome, turno, codigo):
		self.nome = nome
		self.turno = turno
		self.codigo = codigo
		self.disciplinas = {}
		self.alunos = {}
		
	def definir_nome(self, nome):
		self.nome = nome
		
	def definir_turno(self, turno):
		self.turno = turno
	
	def definir_codigo(self, codigo):
		self.codigo = codigo
		
	def incluir_disciplina(self, disciplina):
		self.disciplinas.append(disciplina)
		
	def matricular(self, aluno):
		self.alunos.append(aluno)
	

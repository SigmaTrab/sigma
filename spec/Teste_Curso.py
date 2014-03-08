import unittest
from should_dsl import should
from Curso import Curso
from Aluno import Aluno

class Teste_Curso(unittest.TestCase):
	def setUp(self):
		Curso.cursos = {}

	def test_criar_curso(self):
		um_curso = Curso('Soldador','N', 222)
		um_curso.nome |should| equal_to('Soldador')
		um_curso.turno |should| equal_to('N')
		um_curso.codigo |should| equal_to(222)	
	
	def teste_definir_nome(self, nome):
		um_curso = Curso('Soldador','N', 222)
		um_curso.definir_nome('Tecnico em Informatica')
		um_curso.nome |should| equal_to('Tecnico em Informatica')
		
	def teste_definir_turno(self, turno):
		um_curso = Curso('Soldador','N', 222)
		um_curso.definir_turno('M')
		um_curso.turno |should| equal_to('M')
	
	def teste_definir_codigo(self, codigo):
		um_curso = Curso('Soldador','N', 222)
		um_curso.definir_codigo(333)
		um_curso.codigo |should| equal_to(333)
'''
	def teste_incluir_disciplina(self, disciplina):
		self.disciplinas.append(disciplina)
		
	def teste_matricular(self, aluno):
		self.alunos.append(aluno)
'''
if __name__ == "__main__":
	unittest.main()

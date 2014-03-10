import unittest
from should_dsl import should
from Curso import Curso
from Aluno import Aluno
from Disciplina import Disciplina

class Teste_Curso(unittest.TestCase):
	def setUp(self):
		Curso.cursos = {}

	def test_criar_curso(self):
		um_curso = Curso('Soldador','N', 222)
		um_curso.nome |should| equal_to('Soldador')
		um_curso.turno |should| equal_to('N')
		um_curso.codigo |should| equal_to(222)	
	
	def teste_definir_nome(self):
		um_curso = Curso('Soldador','N', 222)
		um_curso.definir_nome('Tecnico em Informatica')
		um_curso.nome |should| equal_to('Tecnico em Informatica')
		
	def teste_definir_turno(self):
		um_curso = Curso('Soldador','N', 222)
		um_curso.definir_turno('M')
		um_curso.turno |should| equal_to('M')
	
	def teste_definir_codigo(self):
		um_curso = Curso('Soldador','N', 222)
		um_curso.definir_codigo(333)
		um_curso.codigo |should| equal_to(333)

	def teste_incluir_disciplina(self):
		um_curso = Curso('Soldador','N', 222)
		uma_disciplina = Disciplina("Biologia")
		um_curso.incluir_disciplina(uma_disciplina)
		um_curso.disciplinas[0] |should| equal_to(uma_disciplina)
		
	
	def teste_matricular(self):
		um_curso = Curso('Soldador','N', 222)
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		um_curso.matricular(um_aluno)
		um_curso.alunos[0] |should| equal_to(um_aluno)

if __name__ == "__main__":
	unittest.main()

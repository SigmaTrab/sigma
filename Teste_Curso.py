import unittest
from should_dsl import should
from Curso import Curso

# fake
class Aluno:
	def __init__(self, nome, endereco):
		self.matricula = 1
# /fake

class Teste_Curso(unittest.TestCase):
	def setUp(self):
		Curso.cursos = {}

	def test_criar_curso(self):
		um_curso = Curso('Soldador','N')
		um_curso.nome |should| equal_to('Soldador')
		um_curso.turno |should| equal_to('N')

import unittest
from should_dsl import should
from Disciplina import Disciplina
from Material import Material

class Teste_Disciplina(unittest.TestCase):
	def setUp(self):
		Disciplina.disciplinas = []

	def test_criar_disciplina(self):
		uma_disciplina = Disciplina("Biologia")
		uma_disciplina.nome |should| equal_to("Biologia")
	
	def teste_alterar_nome_disciplina(self):
		uma_disciplina = Disciplina("Biologia")
		uma_disciplina.alterar_nome("Quimica")
		uma_disciplina.nome |should| equal_to("Quimica")
	
	def teste_incluir_material_e_retornar_material_disciplina(self):
		uma_disciplina = Disciplina("Biologia")
		um_material = Material("Livro", "Lorem ipsum", "Ricardo")
		uma_disciplina.incluir_material(um_material)
		uma_disciplina.retornar_material(0) |should| equal_to(um_material)
<<<<<<< HEAD

=======
	'''
	def teste_alterar_matricula_aluno(self):
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		um_aluno.alterar_matricula(2)
		um_aluno.matricula |should| equal_to(2)
	'''
>>>>>>> 5da33106efb7b6b014c27d8b2d39b8c15e838dbc

if __name__ == "__main__":
	unittest.main()

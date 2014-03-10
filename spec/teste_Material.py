import unittest
from should_dsl import should
from Material import Material
from Aluno import Aluno

class Teste_Aluno(unittest.TestCase):
	def setUp(self):
		Material.mateirais = {}

	def test_criar_material(self):
		um_material = Material("livro", "Biologia")
		um_material.nome |should| equal_to("livro")
		um_material.disciplina |should| equal_to("Biologia")
	
	def teste_alterar_nome_material(self):
		um_material = Material("livro", "Biologia")
		um_material.alterar_nome("book")
		um_material.nome |should| equal_to("book")
	
	def teste_alterar_conteudo_material(self):
		um_material = Material("livro", "conteudo")
		um_material.alterar_conteudo("content")
		um_material.conteudo |should| equal_to("content")
	
	'''
	def teste_alocar_bolsista_material(self):
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		um_material = Material("livro", "Biologia")
		um_material.alocar_bolsista(um_aluno)
		um_material.bolsista |should| equal_to(um_aluno)
	'''

if __name__ == "__main__":
	unittest.main()

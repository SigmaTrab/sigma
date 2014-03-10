import unittest
from should_dsl import should
from Material import Material
from Aluno import Aluno
from Bolsista import Bolsista
from Disciplina import Disciplina

class Teste_Aluno(unittest.TestCase):
	def setUp(self):
		Material.mateirais = []

	def test_criar_material(self):
	#Eu sei que posso criar o material direto mas eu prefiro passar por tudo isso pra testar de verdade se todo o sistema funciona....
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		uma_disciplina = Disciplina("Biologia")
		um_bolsista = Bolsista(um_aluno)
		uma_disciplina = um_bolsista.postar_material("Livro", "Lorem ipson", uma_disciplina)
		um_material = uma_disciplina.retornar_material(0)
		um_material.nome |should| equal_to("Livro")
		um_material.conteudo |should| equal_to("Lorem ipson")
	
	def teste_alterar_nome_material(self):
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		uma_disciplina = Disciplina("Biologia")
		um_bolsista = Bolsista(um_aluno)
		uma_disciplina = um_bolsista.postar_material("Livro", "Lorem ipson", uma_disciplina)
		um_material = uma_disciplina.retornar_material(0)
		um_material.alterar_nome("book")
		um_material.nome |should| equal_to("book")
	
	def teste_alterar_conteudo_material(self):
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		uma_disciplina = Disciplina("Biologia")
		um_bolsista = Bolsista(um_aluno)
		uma_disciplina = um_bolsista.postar_material("Livro", "Lorem ipson", uma_disciplina)
		um_material = uma_disciplina.retornar_material(0)
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

import unittest
from should_dsl import should
from Bolsista import Bolsista
from Aluno import Aluno

class Teste_Aluno(unittest.TestCase):
	def setUp(self):
		Bolsista.Bolsistas = []

	def test_criar_bolsista(self):
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		um_Bolsista = Bolsista(um_aluno)
		um_Bolsista.nome |should| equal_to("Joao")
		um_Bolsista.endereco |should| equal_to("Rua das Coves")
		um_Bolsista.matricula |should| equal_to(1)
	
	def teste_alterar_nome_Bolsista(self):
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		um_Bolsista = Bolsista(um_aluno)
		um_Bolsista.alterar_nome("Marcos")
		um_Bolsista.nome |should| equal_to("Marcos")
	
	def teste_alterar_endereco_Bolsista(self):
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		um_Bolsista = Bolsista(um_aluno)
		um_Bolsista.alterar_endereco("Rua 2")
		um_Bolsista.endereco |should| equal_to("Rua 2")
	
	def teste_alterar_matricula_Bolsista(self):
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		um_Bolsista = Bolsista(um_aluno)
		um_Bolsista.alterar_matricula(2)
		um_Bolsista.matricula |should| equal_to(2)
	

if __name__ == "__main__":
	unittest.main()

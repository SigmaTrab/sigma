import unittest
from should_dsl import should
from Aluno import Aluno

class Teste_Aluno(unittest.TestCase):
	def setUp(self):
		Aluno.alunos = {}

	def test_criar_aluno(self):
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		um_aluno.nome |should| equal_to("Joao")
		um_aluno.endereco |should| equal_to("Rua das Coves")
		um_aluno.matricula |should| equal_to(1)
	
	def teste_alterar_nome_aluno(self):
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		um_aluno.alterar_nome("Marcos")
		um_aluno.nome |should| equal_to("Marcos")
	
	def teste_alterar_endereco_aluno(self):
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		um_aluno.alterar_endereco("Rua 2")
		um_aluno.endereco |should| equal_to("Rua 2")
	
	def teste_alterar_matricula_aluno(self):
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		um_aluno.alterar_matricula(2)
		um_aluno.matricula |should| equal_to(2)
	

if __name__ == "__main__":
	unittest.main()

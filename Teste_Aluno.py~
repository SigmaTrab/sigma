import unittest
from should_dsl import should
from Aluno import Aluno

#Fake
class Curso:
  def __init__(self, nome, turno):
    self.nome = nome
    self.turno = turno
    self.alunos = {}

  def matricular(self, aluno):
    self.alunos = aluno #de aluno para curso
#/Fake

class Teste_Aluno(unittest.TestCase):
  def setUp(self):
    Aluno.alunos = {}

  def test_criar_aluno(self):
    um_aluno = Aluno("Joao", "Rua das Coves", 1)
    um_aluno.nome |should| equal_to("Joao")
    um_aluno.endereco |should| equal_to("Rua das Coves")
    um_aluno.matricula |should| equal_to(1)

  def test_matricular_aluno(self):
    curso = Curso("Informatica", "N")
    aluno = Aluno("Andre", "Rua dos Bobos", 1)
    aluno.matricular(aluno)
		
  def test_alterar_endereco_de_aluno(self):
    aluno = Aluno("Jose", "Alberto Torres", 01)
    aluno.alterar_endereco("7 de setembro")
    aluno.endereco |should| equal_to("7 de setembro")
    
if __name__ == "__main__":
  unittest.main()

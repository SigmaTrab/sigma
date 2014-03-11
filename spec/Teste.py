#!/usr/bin/env python
#coding: utf-8

import unittest
from should_dsl import should
from Aluno import Aluno
from Bolsista import Bolsista
from Curso import Curso
from Disciplina import Disciplina
from Material import Material

class AlunoSpec(unittest.TestCase):
	def setUp(self):
		Aluno.alunos = []

	def it_creates_a_object_aluno(self):
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		um_aluno.nome |should| equal_to("Joao")
		um_aluno.endereco |should| equal_to("Rua das Coves")
		um_aluno.matricula |should| equal_to(1)
		del um_aluno
	
	def it_alterate_nome_aluno(self):
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		um_aluno.alterar_nome("Marcos")
		um_aluno.nome |should| equal_to("Marcos")
		del um_aluno
	
	def it_alterate_endereco_aluno(self):
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		um_aluno.alterar_endereco("Rua 2")
		um_aluno.endereco |should| equal_to("Rua 2")
		del um_aluno
	
	def it_alterate_matricula_aluno(self):
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		um_aluno.alterar_matricula(2)
		um_aluno.matricula |should| equal_to(2)
		del um_aluno
		
class BolsistaSpec(unittest.TestCase):
	def setUp(self):
		Bolsista.Bolsistas = []

	def test_criar_bolsista(self):
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		um_Bolsista = Bolsista(um_aluno)
		um_Bolsista.nome |should| equal_to("Joao")
		um_Bolsista.endereco |should| equal_to("Rua das Coves")
		um_Bolsista.matricula |should| equal_to(1)
	
	def test_alterar_nome_Bolsista(self):
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		um_Bolsista = Bolsista(um_aluno)
		um_Bolsista.alterar_nome("Marcos")
		um_Bolsista.nome |should| equal_to("Marcos")
	
	def test_alterar_endereco_Bolsista(self):
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		um_Bolsista = Bolsista(um_aluno)
		um_Bolsista.alterar_endereco("Rua 2")
		um_Bolsista.endereco |should| equal_to("Rua 2")
	
	def test_alterar_matricula_Bolsista(self):
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		um_Bolsista = Bolsista(um_aluno)
		um_Bolsista.alterar_matricula(2)
		um_Bolsista.matricula |should| equal_to(2)

class CursoSpec(unittest.TestCase):
	def setUp(self):
		Curso.cursos = []

	def test_criar_curso(self):
		um_curso = Curso('Soldador','N', 222)
		um_curso.nome |should| equal_to('Soldador')
		um_curso.turno |should| equal_to('N')
		um_curso.codigo |should| equal_to(222)	
	
	def test_definir_nome_curso(self):
		um_curso = Curso('Soldador','N', 222)
		um_curso.definir_nome('Tecnico em Informatica')
		um_curso.nome |should| equal_to('Tecnico em Informatica')
		
	def test_definir_turno_curso(self):
		um_curso = Curso('Soldador','N', 222)
		um_curso.definir_turno('M')
		um_curso.turno |should| equal_to('M')
	
	def test_definir_codigo_curso(self):
		um_curso = Curso('Soldador','N', 222)
		um_curso.definir_codigo(333)
		um_curso.codigo |should| equal_to(333)

	def test_incluir_disciplina_curso(self):
		um_curso = Curso('Soldador','N', 222)
		uma_disciplina = Disciplina("Biologia")
		um_curso.incluir_disciplina(uma_disciplina)
		um_curso.disciplinas[0] |should| equal_to(uma_disciplina)
		
	
	def test_matricular_curso(self):
		um_curso = Curso('Soldador','N', 222)
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		um_curso.matricular(um_aluno)
		um_curso.alunos[0] |should| equal_to(um_aluno)

class DisciplinaSpec(unittest.TestCase):
	def setUp(self):
		Disciplina.disciplinas = []

	def test_criar_disciplina(self):
		uma_disciplina = Disciplina("Biologia")
		uma_disciplina.nome |should| equal_to("Biologia")
	
	def test_alterar_nome_disciplina(self):
		uma_disciplina = Disciplina("Biologia")
		uma_disciplina.alterar_nome("Quimica")
		uma_disciplina.nome |should| equal_to("Quimica")
	
	def test_incluir_material_e_retornar_material_disciplina(self):
		uma_disciplina = Disciplina("Biologia")
		um_material = Material("Livro", "Lorem ipsum", "Ricardo")
		uma_disciplina.incluir_material(um_material)
		uma_disciplina.retornar_material(0) |should| equal_to(um_material)

class MaterialSpec(unittest.TestCase):
	def setUp(self):
		Material.mateirais = []

	def it_criar_material(self):
	#Eu sei que posso criar o material direto mas eu prefiro passar por tudo isso pra testar de verdade se todo o sistema funciona....
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		uma_disciplina = Disciplina("Biologia")
		um_bolsista = Bolsista(um_aluno)
		uma_disciplina = um_bolsista.postar_material("Livro", "Lorem ipson", uma_disciplina)
		um_material = uma_disciplina.retornar_material(0)
		um_material.nome |should| equal_to("Livro")
		um_material.conteudo |should| equal_to("Lorem ipson")
	
	def it_alterar_nome_material(self):
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		uma_disciplina = Disciplina("Biologia")
		um_bolsista = Bolsista(um_aluno)
		uma_disciplina = um_bolsista.postar_material("Livro", "Lorem ipson", uma_disciplina)
		um_material = uma_disciplina.retornar_material(0)
		um_material.alterar_nome("book")
		um_material.nome |should| equal_to("book")
	
	def it_alterar_conteudo_material(self):
		um_aluno = Aluno("Joao", "Rua das Coves", 1)
		uma_disciplina = Disciplina("Biologia")
		um_bolsista = Bolsista(um_aluno)
		uma_disciplina = um_bolsista.postar_material("Livro", "Lorem ipson", uma_disciplina)
		um_material = uma_disciplina.retornar_material(0)
		um_material.alterar_conteudo("content")
		um_material.conteudo |should| equal_to("content")


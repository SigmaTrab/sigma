from Material import Material
import sys

class Disciplina:
	disciplinas = []
	
	def __init__(self, nome):
		self.nome = nome
		self.materiais = []
		
	def alterar_nome(self, nome):
		self.nome = nome
	
	def incluir_material(self, material):
		self.materiais.append(material)
		
	def listar_materiais(self):
		for n in self.materiais:
			print n.nome
		
	def retornar_material(self, n):
		return self.materiais[n]
	
'''	
uma_disciplina = Disciplina("Biologia")
um_material = Material("Livro", "Lorem ipsum", "Ricardo")
uma_disciplina.incluir_material(um_material)
t = sys.stdout
uma_disciplina.listar_materiais()	
print(t)
'''

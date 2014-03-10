

class Disciplina:
	
	def __init__(self, nome):
		self.nome = nome
		materiais = {}
		
	def modificar_nome(self, nome):
		self.nome = nome
	
	def incluir_material(self, material):
		self.materiais.append(material)
		
	def listar_materiais(self):
		for n in materiais:
			print n
		
	def retornar_material(self, n):
		return materiais(n)
		
	
		
	

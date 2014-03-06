class Material:
  materials = {}

	def __init__(self, nome, disciplina):
    self.nome = nome
    self.disciplina = disciplina

  def Formatar_material(self, material, disciplina, bolsista):
    self.material = material
    self.disciplina = disciplina
    self.bolsista = bolsista


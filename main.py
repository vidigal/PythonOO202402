from especialidade import especialidade
from medico import medico

m1 = medico("Victor", "45645", False)
m2 = medico("Bruno", "545645", True)
m3 = medico("Ana Maria", "545755", True)

e1 = especialidade("Pediatria")
e2 = especialidade("Cardiologia")
e3 = especialidade("Dermatologia")

m1.especialidades.append(e1)
m1.especialidades.append(e2)

m2.especialidades.append(e3)

print(f'Especialidades do {m1.nome}: ')
m1.listar_especialidades()

print(f'Especialidades do {m2.nome}: ')
m2.listar_especialidades()


from especialidade import especialidade


class medico:

    def __init__(self, nome="", crm="", ativo=True):
        self.nome = nome
        self.crm = crm
        self.ativo = ativo
        self.especialidades: [especialidade] = []

    def listar_especialidades(self):
        for especialidade in self.especialidades:
            print(especialidade.descricao)

class Funcionario:

    def __init__(self, nome):
        self.nome = nome

    def registrar_horas(self, horas):
        print('Horas registradas...')

    def monstrar_tarefa(self):
        print('Fez muita coisa...')


class Turmaa(Funcionario):
    def monstrar_tarefa(self):
        print('Fez muita coisa, Turma-A')

    def buscar_cursos_do_mes(self, mes=None):
        print(f'Monstrando Cursos - {mes}' if mes else 'Mostrando curso desse mês')

class Turmab(Funcionario):
    def monstrar_tarefa(self):
        print('Fez muita coisa, Turma-B!')

    def buscar_perguntas_sem_respostas(self):
        print('Mostrando perguntas não respondidas do Fórum')

class Turmac:
    def __str__(self):
        return f'Turma-C, {self.nome}'

class Junior(Turmab):
    pass

class Pleno(Turmab, Turmab):
    pass

class Senior(Turmab, Turmab, Turmac):
    pass

jose = Junior('Jose')
jose.buscar_perguntas_sem_respostas()
jose.monstrar_tarefa()
print('*'*50)

luan = Pleno('Luan')
luan.buscar_perguntas_sem_respostas()
luan.buscar_cursos_do_mes()
luan.monstrar_tarefa()
print('*'*50)

sergio = Senior('Sergio')
print(sergio)
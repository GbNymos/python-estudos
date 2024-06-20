import os
from time import sleep
#Este código define uma estrutura básica de gerenciamento de alunos e alunos PCD (Pessoas com Deficiência) em uma instituição de ensino. 
#Ele inclui funcionalidades como cadastro de alunos, gerenciamento de notas, cálculo de média, e alteração de status de matrícula e mensalidade.

alunos=[]

class aluno:
    status_matricula=False  #True caso estiver ativo a matricula 
    media=0
    notas=[]
    status_mensalidade=False
    def __init__(self,n,idade,curso,mensalidade) :
        self.nome=str(n)
        self.idade=int(idade)
        self.curso=str(curso)
        self.mensalidade=float(mensalidade)
    def cadastrar_notas(self):
        print("Para parar de digitar as notas, digite -0")
        while True:
            notas=float(input("Digite a nota do aluno:"))
            if notas==-0:
                break
            self.notas.append(notas)
        print(self.notas)
    def calc_media(self):
        soma=sum(self.notas)
        self.media=soma/len(self.notas)
        if self.media>6:
            print("Aprovado")
        else :
            print("Reprovado")
    
    def mudar_status_matricula(self):
        if self.status_matricula==False:
            self.status_matricula=True
            print("Matricula ativa")
        else:
            self.status_matricula=False
            print("Matricula inativa")

    def mensalidade_mudar_status(self):
        if self.status_mensalidade==False:
            self.status_mensalidade=True
            print("Mensalidade Paga")  
        else:
            self.status_mensalidade=False
            print("Mensalidade pendente")

    def informacao_aluno(self):
        print(f""" 
        Nome........:{self.nome}
        idade.......:{self.idade}
        Curso.......:{self.curso}
        Matricula...:{"Ativa" if self.status_matricula else "Inativa"}
        Notas.......:{self.notas}
        Media.......:{self.media}
        Mensalidade :{"Paga" if self.status_mensalidade else "Pendente"}
        Valor da Mensalidade R${self.mensalidade}.
        """)

class alunos_pcd(aluno):
    def __init__(self,n,idade,curso,mensalidade,deficiencia,nome_acompanhante):
        super().__init__(n, idade,curso,mensalidade)
        self.deficiencia=deficiencia
        self.nome_acompanhante=nome_acompanhante
    def cadastrar_notas(self):
        return super().cadastrar_notas()
    def calc_media(self):
        return super().calc_media()
    def mudar_status_matricula(self):
        return super().mudar_status_matricula()
    def mensalidade_mudar_status(self):
        return super().mensalidade_mudar_status()
    def informacao_aluno(self):
        print(f"""
        Aluno PCD
        Deficiencia...........:{self.deficiencia}
        Nome acompanhante.....:{self.nome_acompanhante}""")
        return super().informacao_aluno()


def menu():
    sleep(2)
    print(""" \033[32m Escolha uma das opcoes abaixo:
          1-Para cadastrar aluno
          2-para mudar situacao de matricula(Ativa ou inativa) do aluno
          3-Para adicionar notas do aluno
          4-Para mudar status da mensalidade(Paga ou Pendente) do aluno
          5-Para ver informacoes do aluno
        \033[m""")
    print(f"\033[31m Alunos cadastrados: {len(alunos)}  \033[m \n")

def cadastrar_aluno():
    os.system("cls") or None
    global alunos
    pcd=str(input("O aluno e pcd? [s|n]: ")).lower()
    try:
        nome=str(input("Nome completo:"))
        idade=int(input("idade: "))
        curso=str(input("Nome do curso: "))
        mensalidade=float(input("valor da mensalidade: "))
        if pcd == "s":
            defic=str(input("Qual a deficiencia:"))
            responsavel=str(input("Digite o nome do responsavel:"))
            a=alunos_pcd(nome,idade,curso,mensalidade,defic,responsavel)
            alunos.append(a)
        else:
            a=aluno(nome,idade,curso,mensalidade)
            alunos.append(a)
    except ValueError:
        print("Valor incorreto")

def identificador():
    nome_aluno=str(input("Nome completo: "))
    for i in range(len(alunos)):
        if alunos[i].nome==nome_aluno:
            return i
        else:
            print("Aluno nao encontrado,verifique se escreveu o nome completo e corretamente.") ##vai passar por cada um e me trazer o nome

def mudar_situacao_matricula(): 
    os.system("cls") or None
    alunos[identificador()].mudar_status_matricula()

def mudar_status_mensalidade():
    os.system("cls") or None
    alunos[identificador()].mensalidade_mudar_status()

def cadastrar_notas():
    os.system("cls") or None
    alunos[identificador()].cadastrar_notas()

def calcular_media():
    os.system("cls") or None
    alunos[identificador()].calc_media()

def  informacao_alunos():
    os.system("cls") or None
    alunos[identificador()].informacao_aluno()

while True:
    menu()
    try:
        opc=int(input("Digite uma opcao:"))
        if opc==0:
            break
        elif opc==1:
            cadastrar_aluno()
        elif opc==2:
            mudar_situacao_matricula()
        elif opc==3:
            cadastrar_notas()
        elif opc==4:
            mudar_status_mensalidade()
        elif opc==5:
            informacao_alunos()
        else:
            print("Ops! essa opcao nao e valida.")

    except ValueError:
        print("Valor incorreto")

print("PROGRAMA FINALIZADO.")
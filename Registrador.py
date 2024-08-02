import re

#O modulo serve basicamente para regitrar o usuário pedindo seu nome completo, data de nascimento, idade, cpf, rg, número de telefone e email
#depois ele armazena tudo isso em um arquivo txt, se o usuário tiver 65 anos ou mais ele é classificado como grupo de risco, abaixo disso o usuário é classificado no grupo padrão.

#Função para verificar se o nome é valido, excluido caracteres especiais com exceção do espaçamento e acentuação nas letras.
def obter_nome_valido():
    while True:
        nome = input("Digite o nome: ")
        # Expressão regular para permitir apenas letras (com acentos) e espaços
        if re.fullmatch(r'[A-Za-zÀ-ÖØ-Ýà-öø-ÿ\s]+', nome):
            return nome
        else:
            print("O nome possui caracteres inválidos. Por favor, insira um nome válido.")



def validar_email(email):
    # Regex para validar o formato do e-mail
    padrao = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return padrao.match(email)

def obter_email_valido():
    while True:
        email = input("Digite o e-mail do usuário: ")
        if validar_email(email):
            return email
        else:
            print("E-mail inválido, por favor insira um e-mail válido.")


# Obtendo e salvando o e-mail do usuário
email_usuario = obter_email_valido()

print("E-mail registrado com sucesso!")

def validar_cpf(cpf):
    """
    Valida se o CPF contém exatamente 11 dígitos numéricos.

    """
    padrao = re.compile(r'^\d{11}$')
    return padrao.match(cpf)

def obter_cpf_valido():
    while True:
        cpf = input("Digite o CPF do usuário (somente números): ")
        if validar_cpf(cpf):
            return cpf
        else:
            print("CPF inválido, por favor insira um CPF com exatamente 11 dígitos.")


if __name__ == "__main__":
    cpf_usuario = obter_cpf_valido()

def validar_rg(rg):
    """
    Valida se o RG contém exatamente 10 dígitos numéricos.

    """
    padrao = re.compile(r'^\d{5,10}$')
    return padrao.match(rg)

def obter_rg_valido():
    """
    Solicita ao usuário um RG válido e garante que contenha exatamente 10 dígitos.
    """
    while True:
        rg = input("Digite o RG do usuário (somente números): ")
        if validar_rg(rg):
            return rg
        else:
            print("RG inválido, por favor insira um RG válido")

if __name__ == "__main__":
    rg_usuario = obter_rg_valido()


import re
from datetime import datetime

def validar_data_nascimento(data):
    """
    Valida se a data de nascimento está no formato DD/MM/AAAA e é uma data válida.

    """
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def obter_data_nascimento_valida():
    """
    Solicita ao usuário uma data de nascimento válida no formato DD/MM/AAAA.

    """
    while True:
        data = input("Digite a data de nascimento do usuário (DD/MM/AAAA): ")
        if validar_data_nascimento(data):
            return data
        else:
            print("Data inválida, por favor insira uma data no formato DD/MM/AAAA.")

def calcular_idade(data_nascimento):
    """
    Calcula a idade do usuário com base na data de nascimento fornecida.


    """
    data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
    hoje = datetime.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

def classificar_usuario(idade):
    """
    Classifica o usuário em grupo de risco ou grupo padrão com base na idade.

    """
    if idade >= 65:
        return "grupo de risco"
    else:
        return "grupo padrão"


# Exemplo de uso
if __name__ == "__main__":
    data_nascimento_usuario = obter_data_nascimento_valida()
    idade_usuario = calcular_idade(data_nascimento_usuario)

def salvar_dados_em_arquivo(nome, email, cpf, rg, data_nascimento, idade, classificacao, telefone, telefone_2, arquivo='dados_usuario.txt'):
    """
    Salva todos os dados do usuário em um arquivo de forma organizada.
    """
    try:
        with open(arquivo, 'a', encoding='utf-8') as f:  # Abre o arquivo em modo de anexação
            f.write(f"Nome: {nome}\n")
            f.write(f"E-mail: {email}\n")
            f.write(f"CPF: {cpf}\n")
            f.write(f"RG: {rg}\n")
            f.write(f"Data de Nascimento: {data_nascimento}\n")
            f.write(f"Idade: {idade} anos\n")
            f.write(f"Classificação: {classificacao}\n")
            f.write(f"Telefone 1: {telefone}\n")
            f.write(f"Telefone 2: {telefone_2}\n")
            f.write("-" * 40 + "\n")  # Linha separadora entre registros
    except IOError as e:
        print(f"Erro ao abrir o arquivo: {e}")

def obter_telefones():
    """
    Solicita ao usuário dois números de telefone.
    """
    telefone = input("Insira um telefone para contato: ")
    telefone_2 = input("Insira outro telefone para contato caso o primeiro não atenda: ")
    return telefone, telefone_2

def main():
    """
    Função principal para registro de usuários.
    """
    while True:
        nome_usuario = obter_nome_valido()
        email_usuario = obter_email_valido()
        cpf_usuario = obter_cpf_valido()
        rg_usuario = obter_rg_valido()
        data_nascimento_usuario = obter_data_nascimento_valida()
        idade_usuario = calcular_idade(data_nascimento_usuario)
        classificacao_usuario = classificar_usuario(idade_usuario)
        telefone, telefone_2 = obter_telefones()
        
        salvar_dados_em_arquivo(nome_usuario, email_usuario, cpf_usuario, rg_usuario, data_nascimento_usuario, idade_usuario, classificacao_usuario, telefone, telefone_2)
        
        print(f"Dados salvos com sucesso! A idade do usuário é {idade_usuario} anos, o RG é {rg_usuario}, e a classificação é {classificacao_usuario}.")
        print(f"Telefones de contato: {telefone} e {telefone_2}")
        
        continuar = input("Deseja registrar outro usuário? (sim/não): ").strip().lower()
        if continuar == 'não':
            print("Obrigado pela preferência!")
            break

if __name__ == "__main__":
    main()
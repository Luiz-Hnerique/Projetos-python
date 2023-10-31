#                                         Revisão Geral

#                                       tipos de variáveis

# int = Variavel de tipo inteira. geralemte números positivos ou negativos.
print(123, 1, 2, 3 ) #Virgulas separam as informões em qualquer print.


# str = String -> variável de tipo simbolo. sempre ente aspas simples ou duplas; qualquer coisa escrito nela 
# será lido como texto.
print('AbC', "AbC") #Sempre usar a virgular pra separar fora das aspas. se usar dentro será lido como parte 
#do texto e não como separador de termos.


# float = São variaveis do tipo flutuante -> São número que possuem casas decimais separados por Poonto
# e não por virgulas como feito na matemática comum.
print(2.5, 5.8)


# Bool = São Variaveis do tipo booleanos -> Usado para questinar se um valor é igual a outro respondendo False (falso) para NÃO ou True para SIM (verdadeiro) São comumente
# usados para mudar o fluxo do programa combinado com "if" e "else"
print(10 == 10)
print(50 == 20)


#                                          Comandos

# print() -> Comando usado para imprimir alguma coisa na tela. Sempre ecrito com letra minúscula e acompanhado de parenteses.
print("Olá Mundo")


# sep='-' #-> O comando sep é usado para definir todos separadores que serão exibidos no print de uma só vez.
print(1, 2, 3, sep='-')
# Também pode ser usado o \n para quebra de linha como separador.
print(1, 2, 3, sep='\n') 
# OU tambem posso mistura o separador com a quebra de linha.
print(1, 2, 3, sep='-', end='\n')
 

# type() -> O comando type serve para que tipo de variavel é aquela que foi colocado entre os parenteses.
print(   type("oi")   )
print(   type(8)      )
print(   type(1.3)    )
print(   type(50 == 50))


# conversão ou coreção de tipos -> para mudar um tipo para qualquer outro se caso for nescessário pois em alguns caso não podemos misturar tipos 
# diferentes em algumas operações.
print(int('1') + 1)  # O Primeiro 1 era uma str pois estava entre "aspas" e foi convertido em int (inteiro) para realizar a operção sem erro.
print(str(2) + 'B')  # Nesse caso o int 2 foi convertido em str para que pudesse concaternar (juntar) sem erro.


#                                                    Variaveis

# As variaveis são criados pelo programador para alocar ou guardar uma inforção na memória que pode ser acessada sempre que for 
# for solicitado. Exemplo:
meu_nome = 'Akashi Seijure'
print(meu_nome)
# sempre que eu usar a variavel 'meu_nome' na verdade eu estou me referindo ao valor nela atribuido anteriormente.  
# obs: sempre utilize o sinha de = (igual) para atribuir o valor, pode se utilizar o underline e sempre seja bem específico quando escolher os nomes para 
# facilitar o reconhecimento durante o projeto.



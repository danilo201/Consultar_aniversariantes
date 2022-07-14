#importação para fazer o DateFrame (formato que apresenta o conteúdo)
#caso der erro instalar pelo cmd (pip install pandas)
import pandas as pd

#importando o tabulate para estilizar o formato de apresentação do dataframe
#caso não rodar instalar no terminal com (pip instal tabulate) ou /
#(pip3 install tabulate)
from tabulate import tabulate

#Apresentação do programa
print('Esse programa aceita apenas numeros como resposta,caso contrario tem que reiniciar o prgrama')
print('No caso de duvidas estou a disposição\n ass.Danilo')
print('\n\n*** Sistema de consulda de aniversariantes da igreja Reviver *** \n\n')

#Conteúdo apresentado do mes de junho
dicionario = {
    'Nome':['Fernando Luiz de souza','danilo'],
    'Nascimento':['26/06/1984','20/06/2000'],
    'Local':['Santa Cecília SC','Monte castelo SC'],
    'RG':[4868289,390957471],
    'CPF':['05085843748','43713216210'],
    }

#Transforma o dicionario em um DataFrame com ajuda do import pandas
junho = pd.DataFrame(dicionario)

print('*** Digite apenas numeros que representa o mês que deseja consultar ***\n')
opcao= int(input('''
    [1]  - Janeiro
    [2]  - Fevereiro
    [3]  - Março
    [4]  - Abril
    [5]  - Maio
    [6]  - Junho ** Apensa esse mês está cadastrado !**
    [7]  - julho
    [8]  - Agosto
    [9]  - Setembro
    [10] - Outubro
    [11] - Novembro
    [12] - Dezembro \n '''))

#Essa é as opções que seja verificada de acordo com a pergunta anterior
if (opcao ==1):
    #como eu não fiz dados de todos os meses ainda esta incompleto, mas a base é essa!
    print(tabulate(Janeiro, headers = 'keys', tablefmt = 'fancy_grid'))
    
elif (opcao ==2):
    #como eu não fiz dados de todos os meses ainda esta incompleto, mas a base é essa!
    print(tabulate(Fevereiro, headers = 'keys', tablefmt = 'fancy_grid'))
    
elif (opcao ==3):
    #como eu não fiz dados de todos os meses ainda esta incompleto, mas a base é essa!
    print(tabulate(Março, headers = 'keys', tablefmt = 'fancy_grid'))
    
elif (opcao ==4):
    #como eu não fiz dados de todos os meses ainda esta incompleto, mas a base é essa!
    print(tabulate(Abril, headers = 'keys', tablefmt = 'fancy_grid'))
    
elif (opcao ==5):
    #como eu não fiz dados de todos os meses ainda esta incompleto, mas a base é essa!
    print(tabulate(Maio, headers = 'keys', tablefmt = 'fancy_grid'))
    
elif (opcao ==6):
    #estilo de apresentação do dataframe
    print(tabulate(junho, headers = 'keys', tablefmt = 'fancy_grid'))
    
elif (opcao ==7):
    #como eu não fiz dados de todos os meses ainda esta incompleto, mas a base é essa!
    print(tabulate(julho, headers = 'keys', tablefmt = 'fancy_grid'))
    
elif (opcao ==8):
    #como eu não fiz dados de todos os meses ainda esta incompleto, mas a base é essa!
    print(tabulate(Agosto, headers = 'keys', tablefmt = 'fancy_grid'))
    
elif (opcao ==9):
    #como eu não fiz dados de todos os meses ainda esta incompleto, mas a base é essa!
    print(tabulate(Setembro, headers = 'keys', tablefmt = 'fancy_grid'))
    
elif (opcao ==10):
    #como eu não fiz dados de todos os meses ainda esta incompleto, mas a base é essa!
    print(tabulate(Outubro, headers = 'keys', tablefmt = 'fancy_grid'))
    
elif (opcao ==11):
    #como eu não fiz dados de todos os meses ainda esta incompleto, mas a base é essa!
    print(tabulate(Novembro, headers = 'keys', tablefmt = 'fancy_grid'))
    
elif (opcao ==12):
    #como eu não fiz dados de todos os meses ainda esta incompleto, mas a base é essa!
    print(tabulate(Dezembro, headers = 'keys', tablefmt = 'fancy_grid'))
    
else:
    print('Resposta invalida, abrir novamente com um numero valido !')
    
#Para que o programa não fechar ao chegar no final, ele recebe um /
    #para aguardar uma resposta
input('\n Aperte o "ENTER" para fechar o programa')

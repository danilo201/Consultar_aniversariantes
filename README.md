Consulta de aniversariantes

*** Informo que não tem todos os meses e os dados é fake, é apenas um demostrativo para ajudar a solucionar caso ter um problema parecido ou até mesmo igual. ***



Os pastores da greja estava com dificuldade para parabenizar os aniversariantes, foi feito um pedido para construir um sistema simples para ajudar com esse problema.

Pensando nisso foi foi criado um dicionario com dentro do codigo para que não tenha atraso ao abrir, por conta do computador ter pouca memoria e travar na importação.
para uma facil visualização, usei o pandas para organizar e apresentar de uma forma mais limpa.

caso der erro pode ser por conta de não ter instalado o "pandas", nesse caso aconselho instalar no terminal com o comando (pip install pandas) ou no linux (sudo apt-get install pandas) com a senha de administrador.

como eu ainda não tinha gostado do formato de apresentação, decidir mudar para um mais agradavel usando a biblioteca "tabulate'. 
caso der erro nessa parte é por conta de não ter essa biblioteca instalada, a instalação é possivel fazer com o comando (pip install tabulate) ou (pip3 install tabulate) ou até mesmo no linux (sudo apt-get install tabulate)

Para estilizar eu usei esse padrão da propria biblioteca:
print(tabulate(Janeiro, headers = 'keys', tablefmt = 'fancy_grid'))

Está com uma estrutura de if/elif por eu ter mais facilidade, mas acredito que ao terminar vou trocar essa estrutura por uma mais simples de fazer manutenção:

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


A criação do dicionario foi feito com o nome da variavel "dicionario",como o formato da data estava dando erro optei para deixar como string para evitar erro. Os dados abaixo é fake para não ter risco de vasamento:

dicionario = {
    'Nome':['Fernando','danilo'],
    'Nascimento':['26/06/2001','10/06/2000'],
    'Local':['Santa Cecília SC','Monte castelo SC'],
    'RG':[4868553,390381312],
    'CPF':['0508179480','37122347341'],
    }
    
    para transformar esses dados em um dataframe com pandas, foi feito criado uma nova variavel recebendo a palavra "pd." como a variavel que foi criado o dicionario como mostra abaixo:
    
    junho = pd.DataFrame(dicionario)
    
como é do mês de junho fez mais sentido separar assim.

Em seguida foi feito a criação de uma variavel recebendo um input com as opções (numero e mês referente ao mês), caso a entrada for algo diferente de 1 a 12 que é os meses que temos ele retornar uma mensagem informando que so aceita esse padrão e fecha o programa.

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

Para não fechar ao retornar a entrada no ultimo input (informando que qual mês gostaria de inserar), decidir deixar mais um input vazio para quando terminar apertar "ENTER' e por não ter nehuma saida nesse input ele fecha o programa finalisando o processo:

input('\n Aperte o "ENTER" para fechar o programa')

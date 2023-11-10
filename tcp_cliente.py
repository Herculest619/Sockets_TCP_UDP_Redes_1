import socket, sys, os

HOST = '127.0.0.1'  # endereço IP Localhost
#HOST = '192.168.2.27'  # endereço IP
PORT_TCP = 20000        # Porta utilizada pelo servidor
BUFFER_SIZE = 1024  # tamanho do buffer para recepção dos dados


def main(argv): 
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #with fecha o socket ao final, AF_INET: indica o protocolo IPv4. SOCK_STREAM: tipo de socket para TCP
            s.connect((HOST, PORT_TCP)) #conecta ao servidor
            print("\nConectado ao server!")
            # s.send("cliente".encode()) #texto.encode - converte a string para bytes
            # data = s.recv(BUFFER_SIZE) #recebe os dados do servidor
            # texto_recebido = repr(data) #converte de bytes para um formato "printável"
            # print('\nRecebido do servidor', texto_recebido) #imprime o texto recebido

            '''
            s.send("listar".encode()) #texto.encode - converte a string para bytes
            data = s.recv(BUFFER_SIZE) #recebe os dados do servidor
            texto_recebido = repr(data) #converte de bytes para um formato "printável"
            print('\nRecebido do servidor', texto_recebido) #imprime o texto recebido
'''
            while(True):       
                #limpa a tela do cmd no windows
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nBem vindo ao sistema de gerenciamento de dispositivos!")
                print("\nSeleciona uma das opções abaixo:")

                print("\n1 - Cadastrar novo dispositivo")
                print("2 - Listar dispositivos")
                print("3 - Sair")

                opcao = input("\nDigite a opção desejada: ")

                if(opcao == "1"):
                    print("\nCADASTRAR NOVO DISPOSITIVO!")
                    s.send("cadastrar".encode())
                elif(opcao == "2"):
                    print("\nListando os dispositivos conectados...")
                    s.send("listar".encode())
                    data = s.recv(BUFFER_SIZE)
                    texto_recebido = repr(data)
                    print('\nRecebido do servidor', texto_recebido)
                elif(opcao == "3"):
                    print("\nSaindo do sistema...")
                    s.send("sair".encode())
                    s.close()
                    break
                else:
                    print("\nOpção inválida!")
                    input("\nPressione qualquer tecla para continuar...")

                '''data = s.recv(BUFFER_SIZE) #recebe os dados do servidor
                texto_recebido = repr(data) #converte de bytes para um formato "printável"
                print('\nRecebido do servidor', texto_recebido) #imprime o texto recebido
                texto_string = data.decode('utf-8') #converte os bytes em string
                if (texto_string == 'bye'):
                    print('\nvai encerrar o socket cliente!')
                    s.close()
                    break'''
    except Exception as error:
        print("\nExceção - Programa será encerrado!")
        print(error)
        return


if __name__ == "__main__":   
    main(sys.argv[1:])
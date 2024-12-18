import os

def exibir_nome_do_programa():
 print ('𝑺𝒂𝒃𝒐𝒓 𝑬𝒙𝒑𝒓𝒆𝒔𝒔\n')

def exibir_opcoes():
    print ('1. Cadastrar restaurante')
    print ('2. Listar restaurante')
    print ('3. Ativar restaurante')
    print ('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Finalizando o app!')

def opcao_invalida():
    print('Opção Inválida!\n')
    input('Digite uma tecla para voltar ao menu principal!')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            print ('Cadastrar restaurante')
        elif opcao_escolhida == 2:
            print ('Listar restaurante')
        elif opcao_escolhida == 3:
            print ('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__': 
    main()
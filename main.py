import os
from Pedido import Pedido
from cliente import Cliente
from Produto import Produto
from ItemPedido import ItemPedido

listaClientes = []
listaProdutos = []

def menuCliente():
    
    while True:
        os.system("cls")
        print("----  Clientes 👤 ----\n"+
            "1 - 📄 Cadastrar\n"+
            "2 - 🔎 Listar\n"+
            "3 - 📝 Alterar\n"+
            "4 - ❌ Excluir\n"+
            "0 - ⬅️ Sair\n")
        opcao = input("Digite a opção escolhida:")

        if opcao=="0":
            break
        elif opcao=="1":
            os.system("cls")
            print("---  Cadastrar Cliente ---\n")


            nome=input("Nome do Cliente:")
            cpf=input("CPF:")
            telefone=input("Telefone:")
            endereco=input("Endereco:")
            mail=input("E-mail:")

            novo = Cliente(nome=nome, cpf=cpf, email=mail, endereco=endereco, tel=telefone)
            listaClientes.append(novo)
            input("\n\nSalvo com sucesso!\n Digite algo para voltar.")
        elif opcao=="2":
            for cliente in listaClientes:
                cliente.imprimeficha()
                input("\n\nDigite algo para voltar. ")
                

def menuProduto():
    while True:
        os.system("cls")
        print("----  Produtos 📦 ----\n"+
            "1 - 📄 Cadastrar\n"+
            "2 - 🔎 Listar\n"+
            "3 - 📝 Alterar\n"+
            "4 - ❌ Excluir\n"+
            "0 - ⬅️ Sair\n")
        opcao = input("Digite a opção escolhida:")

        if opcao=="0":
            break
        
        elif opcao=="1":
                    os.system("cls")
                    print("---  CADASTRAR PRODUTO ---\n")
        
        
                    cod=input("Nome do Produto:")
                    desc=input("Descricao:")
                    categoria=input("Categoria:")
                    preco=input("Preco:")
                
        
                    novo = Produto(cod, desc, categoria, preco)
                    listaProdutos.append(novo)
                    input("\n\nSalvo com sucesso!\n Digite algo para voltar.")
        elif opcao=="2":
            for produto in listaProdutos:
                produto.imprimeProduto()
                input("\n\nDigite algo para voltar. ")
                


            

##main
if __name__ == "__main__":

    

    while True:
        os.system("cls")
        print("---- Sistema Lanchonete 🥪 ----\n"
            "1 - 👤 Clientes\n"+
            "2 - 📦 Produtos\n"+
            "3 - 🛒 Novo Pedido\n"+
            "0 - ⬅️ Sair\n")
        opcao = input("Digite a opção escolhida:")

        if opcao=="0":
            break
        elif opcao=="1":
            menuCliente()
        elif opcao=="2":
            menuProduto()
    print("\n bye!\n ( ﾟдﾟ)✌️   ")

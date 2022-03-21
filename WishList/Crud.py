import mysql.connector
#conexao com banco de dados local
conexao = mysql.connector.connect(

    host='localhost',
    user='root',
    password='*******',
    database='dbwishlist',
)

cursor=conexao.cursor()
MSG = "Olá\n Bem vindo a sua lista de desejos!!\n ! Informe a opção desejada:\n 1- Listar \n 2- Cadastrar \n 3- Atualizar\n 4-Excluir \n 5-Sair"
escolha=0
#Criação da estrutura de repetição setando o numero 5 (int) como o encerramento.
while (escolha!='5'):

    print(MSG)
    escolha=input("Digite a opção:  ")
    if(escolha == '1'):
#Opção que lê o banco de dados
#READ
        comando = f'SELECT * FROM dbwishlist.desejos'
        cursor.execute(comando)
        resultado = cursor.fetchall()# Ler banco de dados
        print(resultado)
#Opção que adiciona um novo item a wishlist
#CREATE
    elif(escolha=='2'):
        cursor = conexao.cursor()
        Categoria=input(("Digite a Categoria do produto: "))
        Nome=input("Digite o nome do produto: ")
        Preco=input("Digite o valor do produto: ")
        Link=input("Digite o link do produto: ")
        comando = f'INSERT INTO desejos (Categoria, Nome,Preco,Link) VALUES ("{Categoria}","{Nome}",{Preco},"{Link}")'
        cursor.execute(comando)
        conexao.commit()
#Opção que atualiza valor de um item baseado em seu nome.
#UPDATE
    elif(escolha=='3'):
        attnm=input("Digite o nome do produto que mudou de preço")
        Nome=attnm
        attpc=input("Informe o novo valor")
        Preco=attpc
        comando=f'UPDATE desejos SET Preco = {Preco} WHERE Nome = "{Nome}"'
        cursor.execute(comando)
        conexao.commit()
#Opção para deletar algo da lista baseado no nome.
#DELETE
    elif(escolha=='4'):
        Nome=input("Digite o nome do produto a ser excluido da lista: ")
        comando=f'DELETE FROM desejos WHERE Nome = "{Nome}"'
        cursor.execute(comando)
        conexao.commit()
#Encerramento da conecção com banco

cursor.close()
conexao.close()










import string, random, smtplib
from email.message import EmailMessage

def enviarEmail (email, charPW, size):
    EMAIL_ADRESS    = ''                                                            #Definir aqui o remetente do email
    EMAIL_PASSWORD  = ''                                                            #Definir aqui a senha atual do email do remetente

    msg             = EmailMessage()
    msg['Subject']  = 'Senha aleatória'                                             #Assunto do email
    msg['From']     = EMAIL_ADRESS                                                  #Remetente
    msg['To']       = email                                                         #Destinatário

    stringMSG = f"""A senha aleatória gerada pelo algoritmo de tamanho {str(size)} foi:
                \n     {charPW}
                \n \n Código disponível no GitHub: https://github.com/JIvanAV"""    #conteído da mensagem a ser enviada

    msg.set_content(stringMSG)                                                      #Conteúdo do email

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:                            #Padrão de emails pelo gmail
        smtp.login(EMAIL_ADRESS,EMAIL_PASSWORD)                                     #fazer o login
        smtp.send_message(msg)                                                      #enviar o email

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=##=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

try: size = int ( input("Informe o tamanho em caracteres da senha: ")) + 1          #definir tamanho da senha

except Exception as error:                                                          #caso o usuário coloque uma senha inválida, size = 10
    size = 10
    print(f"Número digitado inválido. Utilizaremos o tamanho padrão {str(size)}")

characters = ""                                                                     #variável que irá receber os caracteres aleatórios

while size < 5:                                                                     #barrar senhas pequenas (menores que 5)
    size = int (input("""É recomendado que a senha tenha mais de 5 caracteres \n
                         Por favor, considere digitar um número maior:""")) + 1

for i in range (1, size, 1):
    characters += str ( random.choice( string.ascii_letters + string.digits))       #usar a biblioteca random para gerar caractere aleatório e adicionar a variável

email = input (f"\nDigite um email válido para enviar a senha '{characters}': ")    #receber o email do usuário e mostrar a senha

while ".com" not in email or "@" not in email:                                      #barrar caso o email não seja válido
    email = input ("O email selecionado não é válido. Digite novamente: ")

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=##=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

enviarEmail(email,characters,size)                                                  #Enviar o email de fato, encerrando o código

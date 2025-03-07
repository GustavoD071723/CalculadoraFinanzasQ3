from finance import create_account, add_transaction, get_account_balance, get_total_balance
#Crear el menu
def main():

    #Creamos un diccionario para almacenar las cuentas
    account = []

    while True:
        print("bienvenidos a la calculadora")
        print("1. Crear cuenta")
        print("2. Agregar transaccion")
        print("3. Consultar saldo cuenta")
        print("4. Consultar el saldo total")
        print("5. Salir")

    #capturar la opcion de entrada
        option = int(input("Ingrese la opcion deseada: "))

        # Creamos una cuenta
        if option == 1:
            name = input("Ingrese el nombre de la cuenta: ")
            account_type = input("Ingrese el tipo de cuenta: ")
            account_id = create_account(account, name, account_type)
            print(f"Cuenta '{name}' creada con el id {account_id}")


        #Agregamos transaccion
        elif option == 2:
            account_id = int(input("Ingrese el id de la cuenta:"))
            description = input ("Ingrese la descripcion de la transaccion: ")
            amount = float(input("Ingrese el monto de la transaccion: "))
            add_transaction(account_id, amount)
            print(f"Transaccion de {amount} realizada en la cuenta {account_id}")

        #consultar saldo de la cuenta
        elif option == 3:
            account_id = int(input("Ingrese el id de la cuenta"))
            balance = get_account_balance(account, account_id)
            print(f"El saldo de la cuenta {account_id} es {balance}")


        #consultar saldo total
        elif option == 4:
            total_balance = get_total_balance(account)
            print(f"El saldo total de las cuentas es {total_balance}")

        elif option ==5:
            print("Gracias por usar la calculadora")
            #salimos del ciclo
            break

        #opcion invalida
        else:
            print("opcion invalida, por favor intente de nuevo")


if __name__ == "__main__":
    main()
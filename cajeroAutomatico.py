'''
CAJERO AUTOMÁTICO
- AUTENTICAR
- RETIRAR
- DEPOSITAR
- CONSULTAR_SALDO
'''
class CajeroAutomatico:
    def __init__(self, saldo_inicial=0):
        self.saldo= saldo_inicial
        self.pin= "1234"
        
    def auntenticar(self):
        pin_usuario= input("Introduce tu PIN: ")
        if pin_usuario != self.pin:
            print("PIN INCORRECTO")
            return False
        return True
    
    def consultar_saldo(self):
        print(f"Tu saldo es: ${self.saldo}")
        
    def depositar(self, cantidad):
        if cantidad>0:
            self.saldo+=cantidad
            print(f"Has depositado ${cantidad}. Tu nuevo saldo es ${self.saldo}")
        
        else:
            print("Cantidad Inválida")
    
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo-=cantidad
            print(f"Has retirado ${cantidad}. Tu nuevo saldo es ${self.saldo}")
        else:
            print("Saldo insuficiente")
            

cajero= CajeroAutomatico(500)
if cajero.auntenticar():
    while True:
        print("\n1. CONSULTAR SALDO\n2. DEPOSITAR\n3. RETIRAR\n4. SALIR")
        opcion= input("Elige una opción:  ")
        if opcion=="1":
            cajero.consultar_saldo()
        
        elif opcion=="2":
            cantidad = int(input("Introduce la cantidad: "))
            cajero.depositar(cantidad)
        
        elif opcion=="3":
            cantidad = int(input("Introduce la cantidad: "))
            cajero.retirar(cantidad)  
        
        elif opcion=="4":
            break
        
        else:
            print("OPCIÓN INVÁLIDA")
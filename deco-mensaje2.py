import re

class Codificador:
    @staticmethod
    def codificar(texto):
        if not texto:
            return ""
        return ''.join(format(ord(caracter), '08b') for caracter in texto)

    @staticmethod
    def decodificar(binario):
        """Decodifica un texto binario a texto plano y limpia el resultado."""
        try:
            texto = ''.join(chr(int(binario[i:i+8], 2)) for i in range(0, len(binario), 8))
            # Permitir caracteres imprimibles y acentos en español
            texto_limpio = re.sub(r'[^\x20-\x7E\xA1-\xFF]', r'', texto)
            return texto_limpio
        except ValueError:
            print("El código binario ingresado no es válido. Asegúrate de que el código esté en formato binario de 8 bits.")
            return ""

class Menu:
    def mostrar_menu(self):
        print("\n-----------------------------------")
        print("--- DE-CO-dificador de Mensajes ---")
        print("-----------------------------------")
        print("1. CO-dificar un mensaje")
        print("2. DE-codificar un mensaje")
        print("3. Salir")
        print("-----------------------------------")

    def manejar_opcion(self, opcion):
        if opcion == "1":
            mensaje = input("\nIngresa el mensaje a CO-dificar: ")
            codificado = Codificador.codificar(mensaje)
            print("\nMensaje CO-dificado:\n")
            print("-" * len(codificado))
            print(codificado)
            print("-" * len(codificado))
        elif opcion == "2":
            mensaje = input("\nIngresa el código que deseas DE-codificar: ")
            decodificado = Codificador.decodificar(mensaje)
            print("\nMensaje DE-codificado:\n")
            print("-" * len(decodificado))
            print(decodificado)
            print("-" * len(decodificado))
        elif opcion == "3":
            print("\n¡Gracias por utilizar el DE-CO-dificador de Mensajes!\n")
            return False
        else:
            print("\nOpción inválida. Por favor, selecciona 1, 2 o 3.")
            return True

        return self.volver_al_menu()

    def volver_al_menu(self):
        while True:
            print("\n¿Deseas volver al menú inicial?\n1. Sí // 2. No")
            opcion = input("\nElige una opción: ")
            if opcion == "1":
                return True
            elif opcion == "2":
                print("\n¡Gracias por utilizar el DE-CO-dificador de Mensajes!\n")
                return False
            else:
                print("\nOpción inválida. Por favor, elige 1 o 2.")

    def menu(self):
        while True:
            self.mostrar_menu()
            opcion = input("\nElige una opción: ")
            if not self.manejar_opcion(opcion):
                break

if __name__ == "__main__":
    app = Menu()
    app.menu()
import re

def codificar(texto):
    """Codifica un texto a binario."""
    if not texto:
        return ""
    return ''.join(format(ord(caracter), '08b') for caracter in texto)

def decodificar(binario):
    """Decodifica un texto binario a texto plano y limpia el resultado."""
    try:
        texto = ''.join(chr(int(binario[i:i+8], 2)) for i in range(0, len(binario), 8))
        # Permitir caracteres imprimibles y acentos en español
        texto_limpio = re.sub(r'[^\x20-\x7E\xA1-\xFF]', r'', texto)
        return texto_limpio
    except ValueError:
        return "El código binario ingresado no es válido. Asegúrate de que el código esté en formato binario de 8 bits."

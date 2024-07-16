import re

def validarDNI(dni):
    dni_pattern = r"\d{8}[A-Z]$"
    dni_match = re.match(dni_pattern,dni) 
    return bool(dni_match)


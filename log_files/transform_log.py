from datetime import datetime
import os

def transform_file(filename):
    with open(filename, 'r') as file:
        line2 = []
        texto = file.readlines()
        for f in range(1, len(texto) - 4):
            line2.append(texto[f][11:-3].strip())

        line2.insert(0, 'ip,icmp_seq,ttl,tempo')
        texto = '\n'.join(line2)
        texto = texto.replace('ttl=', '')
        texto = texto.replace('icmp_seq=', '')
        texto = texto.replace('tempo=', '')
        texto = texto.replace(':', '')
        texto = texto.replace(' ', ',')

    with open('teste.csv', 'w') as log:
        log.write(texto)



transform_file('ping_14-04-2022_00:08.txt')

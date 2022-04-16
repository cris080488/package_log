def transform_file(filename:str) -> None:
    '''

    :param filename:
    :return: None
    '''
    with open(filename, 'r') as file:
        line2 = []
        texto = file.readlines()
        for f in range(1, len(texto) - 4):
            line2.append(texto[f][11:-3].strip())

        line2.insert(0, 'ip,icmp_seq,ttl,tempo')
        texto = '\n'.join(line2)

        characters = ['ttl=', 'icmp_seq=', 'tempo=', ' ', ':']

        for c in characters:
            texto = texto.replace(c, '')

    with open('{}.csv'.format(filename), 'w') as log:
        log.write(texto)

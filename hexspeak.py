letters = {
    'A': 'A',
    'B': 'B',
    'C': 'C',
    'D': 'D',
    'E': 'E',
    'F': 'F',
    'G': '6',
    'I': '1',
    'O': '0',
    'S': '5',
    'T': '7',
    'Z': '2',
}


def findHexWords(file='', lenght=0):
    if file == '' or lenght == 0:
        return
    try:
        f = open(file, 'r', encoding='latin1')
        lines = f.readlines()

        for line in lines:
            line = line.replace('\n', '')
            if len(line) == lenght:
                goodword = True
                word = '0x'
                for c in line:
                    if c.upper() not in letters.keys():
                        goodword = False
                    else:
                        word += letters[c.upper()]
                if goodword:
                    print(f'Orignal word: {line} - Translated: {word}')

        f.close()
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    findHexWords('./rockyou.txt', 6)

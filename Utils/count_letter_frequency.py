ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def clean_text(text):
    text = text.strip().upper()

    original = 'ÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÇÑ'
    new = 'AAAAAEEEEIIIIOOOOOUUUUCN'
    translate_map = str.maketrans(original, new)

    clean_text = text.translate(translate_map)

    return clean_text

def count_frequency(text):
    freq = {letter: 0 for letter in ALPHABET}
    for c in text:
        if c in freq:
            freq[c] += 1
    return freq

def sort_freq(freq):
    sorted_items = list(freq.items())
    for i in range(1, len(sorted_items)):
        key = sorted_items[i]
        j = i - 1

        while j >=0 and key[1] > sorted_items[j][1]:
            sorted_items[j + 1] = sorted_items[j]
            j -= 1
        sorted_items[j + 1] = key
    return sorted_items

def main():
    while True:
        text = input('Insira o texto ou digite SAIR para encerrar: ')
        if text.lower() == 'sair':
            break

        print('\n' + '-'*50)

        freq_list = sort_freq(count_frequency(clean_text(text)))

        for letter, frequency in freq_list:
            print(f'{letter}: {frequency}')
        print('-'*50 + '\n')

if __name__ == "__main__":
    main()

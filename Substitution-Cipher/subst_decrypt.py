import random

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
BR_ALPHABET_FREQ = "AEOSRINDMUTCLPVGHQBFZJXKWY"
BR_BIGRAMS = {
    'DE': 2.50, 'AS': 1.85, 'EN': 1.55, 'AR': 1.45, 'OS': 1.40,
    'DA': 1.35, 'ER': 1.25, 'DO': 1.15, 'RE': 1.10, 'ES': 1.05,
    'TE': 0.95, 'SE': 0.85, 'CO': 0.85, 'AN': 0.80, 'OR': 0.80,
    'AL': 0.75, 'ME': 0.75, 'AM': 0.70, 'ON': 0.65, 'EM': 0.65,
    'RA': 0.65, 'IN': 0.60, 'PR': 0.60, 'CA': 0.55, 'QU': 0.55,
    'TA': 0.50, 'SA': 0.50, 'DI': 0.45, 'MA': 0.45, 'PA': 0.45,
    'NT': 0.45, 'OU': 0.40, 'ND': 0.40, 'AO': 0.40, 'TI': 0.40,
    'ST': 0.40, 'CI': 0.35, 'CE': 0.35, 'UM': 0.35, 'NA': 0.35,
    'RO': 0.35, 'RI': 0.35, 'NO': 0.35, 'EL': 0.30, 'LA': 0.30,
    'TO': 0.30, 'UR': 0.30, 'TR': 0.30, 'SI': 0.30, 'PO': 0.30,
    'EI': 0.40, 'AI': 0.40, 'IA': 0.40, 'IO': 0.40, 'UA': 0.30, 'UE': 0.30,
    'SS': 0.30, 'RR': 0.30, 'CH': 0.30, 'LH': 0.30, 'NH': 0.30,
    'BR': 0.30, 'CR': 0.30, 'DR': 0.30, 'FR': 0.30, 'GR': 0.30, 
    'BL': 0.20, 'CL': 0.20, 'FL': 0.20, 'GL': 0.20, 'PL': 0.20,
    'QA': -20.0, 'QE': -20.0, 'QI': -20.0, 'QO': -20.0, 'QK': -20.0, 'QZ': -20.0,
    'QB': -20.0, 'QC': -20.0, 'QD': -20.0, 'QF': -20.0, 'QG': -20.0, 'QH': -20.0,
    'QJ': -20.0, 'QL': -20.0, 'QM': -20.0, 'QN': -20.0, 'QP': -20.0, 'QS': -20.0, 
    'QT': -20.0, 'QV': -20.0, 'QW': -20.0, 'QX': -20.0, 'QY': -20.0, 'QQ': -20.0,
    'BH': -15.0, 'DH': -15.0, 'FH': -15.0, 'GH': -15.0, 'JH': -15.0, 'KH': -15.0,
    'MH': -15.0, 'PH': -15.0, 'RH': -15.0, 'SH': -15.0, 'TH': -15.0, 'VH': -15.0,
    'WH': -15.0, 'ZH': -15.0, 'XH': -15.0,
    'MC': -15.0, 'MD': -15.0, 'MF': -15.0, 'MG': -15.0, 'MJ': -15.0, 'MK': -15.0,
    'ML': -15.0, 'MN': -15.0, 'MQ': -15.0, 'MR': -15.0, 'MT': -15.0, 'MV': -15.0,
    'MW': -15.0, 'MX': -15.0, 'MZ': -15.0,
    'BB': -15.0, 'DD': -15.0, 'FF': -15.0, 'GG': -15.0, 'HH': -15.0, 'JJ': -15.0,
    'KK': -15.0, 'LL': -15.0, 'MM': -15.0, 'NN': -15.0, 'PP': -15.0, 'TT': -15.0,
    'VV': -15.0, 'WW': -15.0, 'XX': -15.0, 'YY': -15.0, 'ZZ': -15.0,
    'ZX': -15.0, 'XZ': -15.0, 'WX': -15.0, 'XW': -15.0, 'VW': -15.0, 'WV': -15.0,
    'JX': -15.0, 'XJ': -15.0, 'VZ': -15.0, 'ZV': -15.0, 'KX': -15.0, 'XK': -15.0,
    'CJ': -15.0, 'JC': -15.0, 'FX': -15.0, 'XF': -15.0, 'DX': -15.0, 'XD': -15.0,
    'BX': -15.0, 'XB': -15.0, 'GX': -15.0, 'XG': -15.0, 'ZK': -15.0, 'KZ': -15.0,
    'YJ': -15.0, 'JY': -15.0, 'WJ': -15.0, 'JW': -15.0, 'VK': -15.0, 'KV': -15.0,
    'CV': -15.0, 'VC': -15.0, 'BP': -15.0, 'PB': -15.0, 'KG': -15.0, 'GK': -15.0,
    'ZR': -15.0, 'RZ': -15.0, 'XR': -15.0, 'RX': -15.0,
    'AA': -10.0, 'II': -10.0, 'UU': -10.0
}

BR_TRIGRAMS = {
    'QUE': 1.50, 'ENT': 1.20, 'EST': 1.10, 'NTE': 1.00, 'MEN': 1.00, 'NTO': 1.00,
    'IDA': 0.80, 'DAD': 0.80, 'ADE': 0.80, 'CAO': 0.80, 'OES': 0.80, 'SAO': 0.80,
    'DOR': 0.70, 'URA': 0.70, 'ADO': 0.70, 'IDO': 0.70, 
    'COM': 0.65, 'CON': 0.65, 'PRO': 0.65, 'DES': 0.65, 'TER': 0.65, 'PAR': 0.65,
    'PRE': 0.60, 'TRA': 0.60, 'VER': 0.60, 'PER': 0.60,
    'NHA': 0.60, 'INH': 0.60, 'LHA': 0.60, 'MUI': 0.60, 'QUH': 0.60, 'ARA': 0.50,
    'RES': 0.50, 'ADA': 0.50, 'STO': 0.50, 'TAD': 0.50, 'OSD': 0.40, 'ERA': 0.40,
    'TIC': 0.40, 'IST': 0.40, 'ICA': 0.40, 'AME': 0.40, 'ANC': 0.40, 'RAO': 0.40,
    'AAA': -20.0, 'EEE': -20.0, 'III': -20.0, 'OOO': -20.0, 'UUU': -20.0,
    'QQQ': -20.0, 'WWW': -20.0, 'XXX': -20.0, 'ZZZ': -20.0, 'KKK': -20.0,
    'YYY': -20.0, 'JJJ': -20.0, 'HHH': -20.0, 'BBB': -20.0, 'CCC': -20.0,
    'DDD': -20.0, 'FFF': -20.0, 'GGG': -20.0, 'LLL': -20.0, 'MMM': -20.0,
    'NNN': -20.0, 'PPP': -20.0, 'TTT': -20.0, 'VVV': -20.0, 'RRR': -20.0, 'SSS': -20.0,
    'ZXC': -20.0, 'XCV': -20.0, 'QWE': -20.0, 'ASD': -20.0, 'FGH': -20.0,
    'JKL': -20.0, 'VBN': -20.0, 'NMQ': -20.0, 'WQX': -20.0, 'ZXY': -20.0,
    'BVD': -15.0, 'CFG': -15.0, 'DJM': -15.0, 'FKT': -15.0, 'GZN': -15.0,
    'KWY': -15.0, 'PTK': -15.0, 'VKJ': -15.0, 'XZB': -15.0, 'MNH': -15.0
}

EN_ALPHABET_FREQ = "ETAOINSHRDLUCMFYWGPBVKXQJZ"



WORD_LIST = set()

def open_word_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            clean_word = line.strip().upper()
            WORD_LIST.add(clean_word)
    print(f"-> Loaded {len(WORD_LIST)} words.")

    return WORD_LIST


def count_letter_freq(ciphertext):
    freq = {letter: 0 for letter in ALPHABET}
    for char in ciphertext:
        if char in freq:
            freq[char] += 1
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

def compare_freq(sorted_freq, reference_freq):
    mapping = {}
    for i in range(len(sorted_freq)):
        if sorted_freq[i][1] == 0: break
        mapping[sorted_freq[i][0]] = reference_freq[i]
    return mapping

def shuffle_mapping(mapping):
    values = list(mapping.values())
    random.shuffle(values)

    shuffled_mapping = {key: values[i] for i, key in enumerate(mapping.keys())}

    return shuffled_mapping

def decipher(ciphertext, mapping):
    plaintext = ""
    for char in ciphertext:
        if char in mapping:
            plaintext += mapping[char]
        else:
            plaintext += char
    return plaintext

def get_score(plaintext, ref_score):
    score = 0
    bigram = ""
    trigram = ""
    for i in range(0, len(plaintext) - 1):
        bigram = plaintext[i] + plaintext[i + 1]
        if bigram in ref_score[0]: 
            score += ref_score[0][bigram]

    for i in range(0, len(plaintext) - 2):
        trigram = plaintext[i:i+3]
        if trigram in ref_score[1]:
            score += ref_score[1][trigram]
        
    clean_text = plaintext.replace('.', '').replace(',', '').replace('-', ' ')
    text_length = len(clean_text)

    for i in range(text_length):
        for j in range(i + 3, min(i + 13, text_length + 1)):
            slice = clean_text[i:j]
            
            if slice in ref_score[2]:
                score += 50

                if len(slice) > 4:
                    score += 150
                if len(slice) > 7:
                    score += 300

    return score
    
def mutate(ciphertext, mapping, score, ref_score):
    keys = list(mapping.keys())
    rand1, rand2 = random.sample(keys, k=2)
    
    new_mapping = mapping.copy()

    temp = new_mapping[rand1]
    new_mapping[rand1] = new_mapping[rand2]
    new_mapping[rand2] = temp

    new_score = get_score(decipher(ciphertext, new_mapping), ref_score)
    if new_score > score:
        return new_mapping, new_score
    else:
        return mapping, score



def start_decryption(ciphertext, mapping, score, ref_score):
    attempts = {}
    for i in range(10000):
        i += 1
        mapping, score = mutate(ciphertext, mapping, score, ref_score)

        if i >= 9800:
            attempts[decipher(ciphertext, mapping)] = score
        
    return attempts

def print_attempts(attempts):
    i = 1
    sorted_attempts = sorted(attempts.items(), key=lambda item: item[1], reverse=False)

    for attempt, score in sorted_attempts:
        print(f"Score: {score}\nAttempt[{i}]: {attempt}\n")
        i += 1
        
def main():
    
    user_input = input("Insert text to decrypt or type EXIT to quit: ")
    if user_input.lower() == "exit":
        pass
    else:
        print('\n' + '-'*50)

        ref_score = [0, 0, 0]
        ref_score[0] = BR_BIGRAMS
        ref_score[1] = BR_TRIGRAMS
        ref_score[2] = open_word_file("../Utils/Dictionaries/br-utf8-wordlist.txt")

        while True:        
            
            top_attempts = {}
            CIPHERTEXT = user_input

            print("DECRYPTING...\n[" + " "*50 + "]", end="", flush=True)

            frequency = count_letter_freq(CIPHERTEXT)
            sorted_freq = sort_freq(frequency)
            mapping = compare_freq(sorted_freq, BR_ALPHABET_FREQ)   
        

            for i in range(1, 51):
                score = get_score(decipher(CIPHERTEXT, mapping), ref_score)
                attempt = start_decryption(CIPHERTEXT, mapping, score, ref_score)

                top_attempts.update(attempt)

                mapping = shuffle_mapping(mapping)
                print(f'\r[' + '='*i + " "*(50-i) + "]", end="", flush=True)

            print("\n")
            print_attempts(top_attempts)

            user_input = input("Insert text to decrypt or type EXIT to quit: ")
            if user_input.lower() == "exit":
                break
            else:
                print('\n' + '-'*50)


if __name__ == "__main__":
    main()
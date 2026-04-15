
MAX_KEY_LENGTH=20
ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PT_FREQ = {
    'A': 0.1463, 'B': 0.0104, 'C': 0.0388, 'D': 0.0499, 'E': 0.1257,
    'F': 0.0102, 'G': 0.0130, 'H': 0.0128, 'I': 0.0618, 'J': 0.0040,
    'K': 0.0002, 'L': 0.0278, 'M': 0.0474, 'N': 0.0505, 'O': 0.1073,
    'P': 0.0252, 'Q': 0.0120, 'R': 0.0653, 'S': 0.0781, 'T': 0.0434,
    'U': 0.0463, 'V': 0.0167, 'W': 0.0001, 'X': 0.0021, 'Y': 0.0001,
    'Z': 0.0047
}
CIPHERTEXT="luugdgigxqlxzyyfphqymopvczeescbaflysfagvnutwbfkjywduasfhkcivvlnywzmzypxgfzgqucumxnzswtahtzhexvsdtbpnlnclxoqtzwxjbfgvakqjyyaszwzobpxsfugqgczddvibaeycpxdpigvxgwqqqkoeiggnslfnchvvgavdhyfugnkgtgcyyxxluqysmamobpuwnjbkjdsaoaobkbkmrlpbmvcnutlwdkuypgwrcwcnqcqcmomsmjoghzaelujdelqzegmwvmivsjzwtrdljmbifhzhvshaw"

def clean_text(text):
    text = text.strip().upper()

    original = 'ÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÇÑ'
    new = 'AAAAAEEEEIIIIOOOOOUUUUCN'
    translate_map = str.maketrans(original, new)

    clean_text = text.translate(translate_map)

    return clean_text

def get_ic(text):
    n = len(text)
    if n <= 1:
        return 0.0
    
    freq = {char: text.count(char) for char in ALPHABET}

    sigma = sum(f * (f - 1) for f in freq.values())
    ic = sigma / (n * (n - 1))

    return ic

def get_key_length(ciphertext, max_key_length):
    guess_size = 1
    best_ic = 0.0
    
    for  key_len in range(1, max_key_length + 1):
        sum_ic = 0.0

        for i in range(key_len):
            column = ciphertext[i::key_len]
            sum_ic += get_ic(column)

        av_ic = sum_ic / key_len

        if av_ic > best_ic:
            best_ic = av_ic
            guess_size = key_len
    
    return guess_size

def get_column_score(column, shift):
    decrypted_col = ""
    for char in column:
        letter_index = (ALPHABET.index(char) - shift) % 26
        decrypted_col += ALPHABET[letter_index]
    
    score = 0
    for c in ALPHABET:
        score += decrypted_col.count(c) * PT_FREQ[c]
    return score

def decipher(ciphertext, key_length):
    key = ""
    for i in range(key_length):
        column = ciphertext[i::key_length]

        best_shift = 0
        best_score = 0

        for shift in range(26):
            score = get_column_score(column, shift)
            if score > best_score: 
                best_score = score
                best_shift = shift
        
        key_char = ALPHABET[best_shift]
        key += key_char

    print(f"Found Key: '{key}'...")

    plaintext = ""
    for i, char in enumerate(ciphertext):
        shift = ALPHABET.index(key[i % key_length])
        letter_index = (ALPHABET.index(char) - shift) % 26

        plaintext += ALPHABET[letter_index]
    
    return plaintext

if __name__ == "__main__":
    ciphertext = clean_text(input("Enter encrypted text: ").strip())
    print(decipher(ciphertext, get_key_length(ciphertext, MAX_KEY_LENGTH)))
    print("\n\n" + decipher(ciphertext, 4))
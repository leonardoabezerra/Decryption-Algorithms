ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
BR_ALPHABET_FREQ = "AEOSRINDMUTCLPVGHQBFZJXKWY"
EN_ALPHABET_FREQ = "ETAOINSHRDLUCMFYWGPBVKXQJZ"
CIPHERTEXT = "D FULSWRJUDILD H HVVHQFLDO SDUD D VHJXUDQFD QD LQWHUQHW. EOD JDUDQWH TXH DV PHQVDJHQV TXH HQYLDPRV SEJDP OLIDV DSHQDV SRU TXHP GHYH UHFHEH-ODV. VHP D FULSWRJUDILD, QRVVRV GDGRV HVWDULDP HADRVWRV D TXDOTXHU XP."

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

def decipher(ciphertext, mapping):
    plaintext = ""
    for char in ciphertext:
        if char in mapping:
            plaintext += mapping[char]
        else:
            plaintext += char
    return plaintext



    
print("-".join(["-"] * 25))
print(compare_freq(sort_freq(count_letter_freq(CIPHERTEXT)), BR_ALPHABET_FREQ))
print(decipher(CIPHERTEXT, compare_freq(sort_freq(count_letter_freq(CIPHERTEXT)), BR_ALPHABET_FREQ)))

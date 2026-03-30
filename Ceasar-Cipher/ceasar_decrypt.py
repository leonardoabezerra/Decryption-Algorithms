texto = "JBCRCLQRWCRVNBJENBWRWN"
output = ""

for deslocamento in range(1, 26):
    for char in texto:
        if char == " ": 
            continue
        output += chr((ord(char) - ord('A') + deslocamento) % 26 + ord('A'))
    print(output)
    output = ""
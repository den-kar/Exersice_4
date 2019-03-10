#! /usr/bin/python3.6


# Aufgabe 4.1 - 1
def uniqueSort(numberList):
    return sorted(set(numberList))

print (uniqueSort([1, 2, 4, 3]))
print (uniqueSort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]))
print (uniqueSort([6, 7, 3, 2, 1]))


# Aufgabe 4.1 - 2
morseCode = {'A': '.-',     'B': '-...',   'C': '-.-.',
             'D': '-..',    'E': '.',      'F': '..-.',
             'G': '--.',    'H': '....',   'I': '..',
             'J': '.---',   'K': '-.-',    'L': '.-..',
             'M': '--',     'N': '-.',     'O': '---',
             'P': '.--.',   'Q': '--.-',   'R': '.-.',
             'S': '...',    'T': '-',      'U': '..-',
             'V': '...-',   'W': '.--',    'X': '-..-',
             'Y': '-.--',   'Z': '--..',   ' ': '/',
                          
             '0': '-----',  '1': '.----',  '2': '..---',
             '3': '...--',  '4': '....-',  '5': '.....',
             '6': '-....',  '7': '--...',  '8': '---..',
             '9': '----.',
             
             'À': '·−−·−',  'Ä':	'·−·−',   'È':	'·−··−',
             'É': '··−··',  'Ö': '−−−·',   'Ü':	'··−−',
             'ß': '···−−··', 'Ñ':	'−−·−−', '.': '·−·−·−',
             ',': '−−··−−', ':': '−−−···', ';': '−·−·−·',
             '?':	'··−−··', '-': '−····−', '_': '··−−·−',
             '(':	'−·−−·',  ')': '−·−−·−', '"': '·−−−−·',
             '=':	'−···−',  '+': '·−·−·',  '/': '−··−·',
             '@': '·−−·−·', '!': '-.-.--'
             }

reverseMorseCode = {values:keys for keys,values in morseCode.items()}

def encodeMorse(stringToEncode):
    return ' '.join(morseCode.get(char.upper()) for char in stringToEncode)

def decodeMorse(stringToDecode):
    return ''.join(reverseMorseCode.get(charBlock) for charBlock in stringToDecode.split())

print (encodeMorse("HELP ME !"))
print (decodeMorse(".... . .-.. .--. / -- . / -.-.--"))


# Aufgabe 4.1 - 3
def decomposeURL(stringURL):
    print (stringURL)
    urlInformation = {}
# check if URL beginns with protocol type
    try:
        workingURL = stringURL.split("://")[1]
        urlInformation["Protocol Type"] = stringURL.split("://")[0]
    except:
        urlInformation["Protocol Type"] = None
        workingURL = stringURL
# check if URL contains username
    urlInformation["User Name"] = workingURL.split("@")[0].split(":")[0] if "@" in workingURL else None
# check if URL contains password
    try:        
        urlInformation["Password"] = workingURL.split("@")[0].split(":")[1]
        workingURL = workingURL.split("@")[1]
    except:
        urlInformation["Password"] = None
        if "@" in workingURL:
            workingURL = workingURL.split("@")[1]
# check if URL contains IP address
    try:
        ipAddress = workingURL.split(":")[0].split("/")[0]
        for i in range(4):
            if int(ipAddress.split(".")[i]) in range(256):
                continue
            else:
                print ("invalid IP address") 
                raise ValueError
        urlInformation["IP Address"] = ipAddress
    except ValueError:
        urlInformation["IP Address"] = None
# get sub domain
    if urlInformation["IP Address"] is None and len(workingURL.split("/")[0].split(".")) > 2:
        urlInformation["Sub Domain"] = workingURL.split("/")[0].split(".")[0]
    else:
        urlInformation["Sub Domain"] = None
# get domain name
    if urlInformation["IP Address"] is None and len(workingURL.split("/")[0].split(".")) > 2:
        urlInformation["Domain Name"] = workingURL.split("/")[0].split(".", 1)[1].split(":")[0]
    elif urlInformation["IP Address"] is None and len(workingURL.split("/")[0].split(".")) < 3:
        urlInformation["Domain Name"] = workingURL.split("/")[0].split(":")[0]
    else:
        urlInformation["Domain Name"] = None
# check if URL contains portNumber
    try:
        urlInformation["Port"] = workingURL.split(":")[1].split("/")[0]
    except:
        urlInformation["Port"] = None
# check if URL contains folder tree
    try:        
        urlInformation["Folder Tree"] = "/".join(workingURL.split("/")[1:-1])
    except:
        urlInformation["Folder Tree"] = None
# check if URL contains target file
    try:        
        urlInformation["Target File"] = "".join(workingURL.split("/")[-1:]).split("?")[0]
    except:
        urlInformation["Target File"] = None
# check if URL contains argument file
    urlInformation["Argument File"] = ", ".join(workingURL.split("?")[1].split("#")[0].split("&")) if "?" in workingURL else None
# check if URL cobeispiel.asp?vname=hans&nname=meier&ort=neuburgntains textmarker
    try:
        urlInformation["Textmarker"] = "".join(workingURL.split("#")[1])
    except:
        urlInformation["Textmarker"] = None
        
    return urlInformation

print (decomposeURL("https://www.ballalaika.de/testdirectory1/testdirectory2/testfile.html?search=ok#textmarke"), "\n")
print (decomposeURL("https://223.187.123.255@111.11.123.2:888/seiten/aktuell/scripte/beispiel.asp?vname=django#genau_hier"), "\n")
print (decomposeURL("https://TestURL-Num3:www.ballalaika.de@000.00.000.0:7777"), "\n")
print (decomposeURL("www.google.com/test/image?search=ok&vname=hans&nname=meier&ort=neuburg#textmarke"), "\n")
print (decomposeURL("http://www.domain.de:81/seiten/aktuell/scripte/beispiel.asp"), "\n")
print (decomposeURL("google.com/test/image?search=ok&vname=hans&nname=meier&ort=neuburg#textmarke"), "\n")


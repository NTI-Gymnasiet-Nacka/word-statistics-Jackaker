# Ordstatistik
# Din uppgift är att läsa in text från filen som är angiven.
# Därefter ska ditt program räkna ut följande:
# - Antal ord
# - Mest frekventa ord
# - Genomsnittlig ordlängd
# Gör en funktion för varje.

# Bonus, gör en i taget, skapa en funktion för varje: 
# - Längsta och kortaste ordet - om det finns flera, bestäm själv om du skriver ut ett eller flera
# - Räkna antalet unika ord (alltså ord som bara förekommer en gång)


def read_from_file(path: str):

    with open(path, "r" ,encoding="utf-8") as f:
        return f.readlines()
    
def count_word(text: list):
    string=""

    for ord in text:
        string+=ord
    total=string.split()
    total.remove('-')
    return print(len(total))

def most_frequent(text: list):
    string=""
    dict={}

    for ord in text:
        string+=ord.lower()
    total=string.split()
    total.remove('-')

    for word in total:
        if word  in dict:
            dict[word]+=1
        else:
            dict[word]=1
    mest = max(dict, key=dict.get)
    return print(mest)

def genomsnittlig_ordlängd(text: list):
    string=""
    tom_lista=[]

    for ord in text:
        string+=ord.lower()
    total=string.split()
    total.remove('-')

    for word in total:
        if "." in word:
            word=word.replace('.','')
        if "," in word:
            word=word.replace(',','')
        tom_lista.append(len(word))
    genomsnitt=sum(tom_lista)/len(total)
    return print(genomsnitt)

def längsta_kortaste(text: list):
    total2=[]
    string=""

    for ord in text:
        string+=ord.lower()
    total=string.split()

    for word in total:
        if "." in word:
            word=word.replace('.','')
        if "," in word:
            word=word.replace(',','')
        total2.append(word)
    total2=sorted(total2, key=len)
    print(f'Kortaste: {total2[0]}\nLängsta: {total2[-1]}')
    return

def unika_ord(text: list):
    string=""
    string2=""
    total2=[]
    dict={}

    for ord in text:
        string+=ord.lower()
    total=string.split()
    total.remove('-')

    for word in total:
        if "." in word:
            word=word.replace('.','')
        if "," in word:
            word=word.replace(',','')
        total2.append(word)

    for word in total2:
        if word  in dict:
            dict[word]+=1
        else:
            dict[word]=1
    unika=[key for key, value in dict.items() if value == 1]

    for ord in unika:
        string2+=ord
        string2+=", "
    return print(string2)


def main():
    sentences = read_from_file("en_resa_genom_svenska_skogen.txt")
    count_word(sentences)
    most_frequent(sentences)
    genomsnittlig_ordlängd(sentences)
    längsta_kortaste(sentences)
    unika_ord(sentences)
    

if __name__ == "__main__":
    main()
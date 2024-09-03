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
    """Reads a file with the given parameter path and returns the file as a list of strings, split on newline (\n).

    Args:
        path (str): the path of the readable file

    Returns:
        list(str): list of strings
    """
    with open(path, "r" ,encoding="utf-8") as f:
        def count_word():
            string=""
            for ord in f.readlines():
                string+=ord
                total=string.split()
            total.remove('-')
            return print(len(total))
        
        def most_frequent():
            string=""
            dict={}
            for ord in f.readlines():
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

        def genomsnittlig_ordlängd():
            string=""
            tom_lista=[]
            for ord in f.readlines():
                string+=ord.lower()
                total=string.split()
            # total.remove('-')
            print(total)
            for word in total:
                tom_lista.append(len(word))
            genomsnitt=sum(tom_lista)/len(total)
            return print(genomsnitt)
        genomsnittlig_ordlängd()
        
        def längsta_kortaste():
            string=""
            dict={}
            for ord in f.readlines():
                string+=ord.lower()
                total=string.split()
            total.remove('-')
            for word in total:
                if word  in dict:
                    dict[len(word)]+=1
                else:
                    dict[len(word)]=1
            mest = max(dict, key=dict.get)
            return print(mest)
        längsta_kortaste()



def main():
    
    sentences = read_from_file("en_resa_genom_svenska_skogen.txt") # Här har du nu en lista av strängar från den inlästa filen.

if __name__ == "__main__":
    main()
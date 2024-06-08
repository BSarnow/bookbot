
book_path = "./books/frankenstein.txt"

def main():
    words = text_words()
    print(f"frankenstein has {words} words in it")
    print(f"frankenstein has the following numbers of letters in it:")
    print(count_tubles())

def count_tubles():
    # Zählt die Buchstaben in count_letters und hält sie in einem dict fest.
    tubles = {}
    for a in make_letters():
         tubles[a] = 0
    for a in count_letters():
         if a in tubles:
              tubles[a] += 1
    
    sorted_tubles = dict(sorted(tubles.items()))
    #sotiert dict nach Alphabet
              
    return sorted_tubles

def count_letters():
     # filtert alle Satzzeichen aus path_text(book_path)
     # und macht aus den einzelnen Buchstaben ein String
     all_letters = []
     only_text = filter(str.isalpha, path_text(book_path))
     for a in only_text:
          all_letters.append(a)
     return all_letters         
          

def make_letters():
    # filtert alle Satzzeichen aus path_text und 
    # bildet aus den übrigen Buchstaben ein set
    set_letters =set()
    only_text = filter(str.isalpha, path_text(book_path))
    
    for a in only_text:
            set_letters.add(a)
    return set_letters


def path_text(book_path):
    # Macht aus dem Inhalt einer Datei ein String und
    # ändert alle Großbuchstaben in Kleinbuchstaben
    with open(book_path) as file:
        text = file.read()
        lower_text = text.lower()
    return lower_text

def text_words():
    # zählt die Wörter aus path_text
    words = path_text(book_path).split()
    return len(words)



main()
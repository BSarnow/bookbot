
book_path = "./books/frankenstein.txt"

def main():
    words = text_words()
    print(f"frankenstein has {words} words in it")
    print(f"frankenstein has the following numbers of letters in it:")
    print(count_tubles())

def count_tubles():
    tubles = {}
    for a in make_letters():
         tubles[a] = 0
    for a in count_letters():
         if a in tubles:
              tubles[a] += 1
    
    sorted_tubles = dict(sorted(tubles.items()))

              
    return sorted_tubles

def count_letters():
     all_letters = []
     only_text = filter(str.isalpha, path_text(book_path))
     for a in only_text:
          all_letters.append(a)
     return all_letters         
          

def make_letters():
    set_letters =set()
    only_text = filter(str.isalpha, path_text(book_path))
    
    for a in only_text:
            set_letters.add(a)
    return set_letters


def path_text(book_path):
    with open(book_path) as file:
        text = file.read()
        lower_text = text.lower()
    return lower_text

def text_words():
    words = path_text(book_path).split()
    return len(words)



main()
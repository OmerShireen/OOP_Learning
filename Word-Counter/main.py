from WordCounter import WordCounter

def main():
    text = input("Enter words seperated by space:")
    counter = WordCounter(text)
    counter.count_words()
    counter.display_counts()




if __name__=="__main__":
    main()    
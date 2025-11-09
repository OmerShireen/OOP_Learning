class WordCounter:
    def __init__(self, text):
        self.words = text.split()
        self.counts = {}

    def count_words(self):
        for word in self.words:
            if word in self.counts:
                self.counts[word] +=1
            else:
                self.counts[words]

    def display_counts(self):
        for word, count in self.counts.items():
            print(f"'{word}' appears {count} time(s)")
                                
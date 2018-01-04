from dictionary import *

class processor:

    def wordSplit(self, words):
        self.wordList = words.split()

    def wordComprehension(self, var):

        #detecting pronouns in sentence
        for i in var:
            if str(i) in personalPronouns:
                print("Personal pronoun: ",i)
            if str(i) in subjectivePronouns:
                print("Personal pronoun: ",i)

    def sentenceComprehension(self, var):

        indexLocations = []
        x = 0
        n = 1

        for i in range(0, len(var)):
            if var[x] in transitiveActiveVerbs:
                print("Transitive active verb '%s' is word %d within the sentence." % (str(var[x]), n))
                indexLocations.append(int(x))
            x+=1
            n+=1


    def main(self):
        sentence = str(input("Enter a sentence: "))
        self.wordSplit(sentence)
        #self.wordComprehension(self.wordList)
        self.sentenceComprehension(self.wordList)

if __name__ == "__main__":
    nl = processor()
    nl.main()
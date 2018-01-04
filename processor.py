from dictionary import *

class processor:

    def wordSplit(self, words):
        self.wordList = words.split()

    def sentenceComprehension(self, var):
        """
        Key:

        TAPrTV - Transitive Active Present Tense Verbs
        TAPaTV - Transitive Active Past Tense Verbs

        """

        indexLocations = []
        keyWords = []
        x = 0
        n = 1

        for i in range(0, len(var)):
            if var[x] in transitiveActivePresentTenseVerbs:
                print("Transitive active present tense verb '%s' is word %d within the sentence." % (str(var[x]), n))
                indexLocations.append(int(x))
                keyWords.append(TAPrTV+var[x])
            if var[x] in transitiveActivePastTenseVerbs:
                print("Transitive active past tense verb '%s' is word %d within the sentence." % (str(var[x]), n))
                indexLocations.append(int(x))
                keyWords.append(TAPaTV+var[x])
            x+=1
            n+=1

        print(keyWords)


    def main(self):
        sentence = str(input("Enter a sentence: "))
        self.wordSplit(sentence)
        self.sentenceComprehension(self.wordList)

if __name__ == "__main__":
    nl = processor()
    nl.main()
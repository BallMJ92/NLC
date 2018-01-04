from dictionary import *
import re

class processor:

    def tokenize(self, words):
        self.wordList = re.findall(r'[.?]|\w+', words)
        print(self.wordList)

    def sentenceComprehension(self, var):
        """
        Key:
        TAPrTV - Transitive Active Present Tense Verbs
        TAPaTV - Transitive Active Past Tense Verbs
        PPr - Personal Pronouns
        SPr - Subjective Pronouns
        """

        indexLocations = []
        keyWords = []
        n = 1

        # Analysing each individual word in sentence
        for i in range(0, len(var)):
            # Checking each word according to its index in the sentence
            if var[i] in transitiveActivePresentTenseVerbs:
                # Adding the index location of TAPrTV to list
                indexLocations.append(int(i))
                # Getting index of word within the TAPrTV list
                index = int(transitiveActivePresentTenseVerbs.index(var[i]))
                # Using index of word within the TAPrTV list to get index of opposite word in TAPaTV list
                print("Opposite of %s is %s" % (var[i], transitiveActivePastTenseVerbs[index]))
                keyWords.append(TAPrTV+var[i])
            if var[i] in transitiveActivePastTenseVerbs:
                indexLocations.append(int(i))
                index = int(transitiveActivePastTenseVerbs.index(var[i]))
                print("Opposite of %s is %s" % (var[i], transitiveActivePresentTenseVerbs[index]))
                keyWords.append(TAPaTV+var[i])
            if var[i] in personalPronouns:
                indexLocations.append(int(i))
                index = int(personalPronouns.index(var[i]))
                keyWords.append(PPr+var[i])
            if var[i] in subjectivePronouns:
                indexLocations.append(int(i))
                index = int(subjectivePronouns.index(var[i]))
                keyWords.append(SPr+var[i])
            n+=1

        print(keyWords)
        print(indexLocations)

    def main(self):
        sentence = str(input("Enter a sentence: "))
        self.tokenize(sentence)
        self.sentenceComprehension(self.wordList)


if __name__ == "__main__":
    nl = processor()
    nl.main()


from dictionary import *

class processor:

    def wordSplit(self, words):
        self.wordList = words.split()

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

        for i in range(0, len(var)):
            if var[i] in transitiveActivePresentTenseVerbs:
                print("Transitive active present tense verb '%s' is word %d within the sentence." % (str(var[i]), n))
                indexLocations.append(int(i))
                index = int(transitiveActivePresentTenseVerbs.index(var[i]))
                print("Opposite of %s is %s" % (var[i], transitiveActivePastTenseVerbs[index]))
                keyWords.append(TAPrTV+var[i])
            if var[i] in transitiveActivePastTenseVerbs:
                print("Transitive active past tense verb '%s' is word %d within the sentence." % (str(var[i]), n))
                indexLocations.append(int(i))
                index = int(transitiveActivePastTenseVerbs.index(var[i]))
                print("Opposite of %s is %s" % (var[i], transitiveActivePresentTenseVerbs[index]))
                keyWords.append(TAPaTV+var[i])
            if var[i] in personalPronouns:
                print("Personal pronoun '%s' is word %d within the sentence." % (str(var[i]), n))
                indexLocations.append(int(i))
                index = int(personalPronouns.index(var[i]))
                keyWords.append(PPr+var[i])
            if var[i] in subjectivePronouns:
                print("Subjective pronoun '%s' is word %d within the sentence." % (str(var[i]), n))
                indexLocations.append(int(i))
                index = int(subjectivePronouns.index(var[i]))
                keyWords.append(SPr+var[i])
            n+=1

        print(keyWords)

    def main(self):
        sentence = str(input("Enter a sentence: "))
        self.wordSplit(sentence)
        self.sentenceComprehension(self.wordList)


if __name__ == "__main__":
    nl = processor()
    nl.main()



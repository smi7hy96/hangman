from random_word import RandomWords


class RandomWordGenerator:

    def __init__(self):
        self.__word = self.__generate_word()

    def get_word(self):
        return self.__word

    def __generate_word(self):
        r = RandomWords()
        return r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minCorpusCount=1, maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=10, minLength=5)

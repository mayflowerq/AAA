class CountVectorizer:
    def __init__(self):
        pass

    def get_feature_names(self):
        unique_names = []
        for i in corpus:
            sentence = (i.split())
            for word in sentence:
                if word.lower() not in unique_names:
                    unique_names.append(word.lower())
        return unique_names

    def fit_transform(self, corpus):
        unique_names = self.get_feature_names()
        final_1 = []
        final_2 = []
        first_corpus = corpus[0]
        second_corpus = corpus[1]
        first_corpus = first_corpus.split()
        second_corpus = second_corpus.split()
        for unique_name in unique_names:
            counter = 0
            for name in first_corpus:
                if unique_name == name.lower():
                    counter += 1
            final_1.append(counter)
        for unique_name in unique_names:
            counter = 0
            for name in second_corpus:
                if unique_name == name.lower():
                    counter += 1
            final_2.append(counter)
        return [final_1, final_2]


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    assert count_matrix == [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]], \
        f'Неправильный вывод'
    assert vectorizer.get_feature_names() == ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
                                              'fresh', 'ingredients', 'parmesan', 'to', 'taste'],\
        f'Неправильный вывод'
    print(vectorizer.get_feature_names())
    print(count_matrix)

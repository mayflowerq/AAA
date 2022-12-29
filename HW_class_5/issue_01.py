class CountVectorizer:
    def __init__(self):
        pass

    def get_feature_names(self):
        unique_names = []
        for i in corpus:
            sentence = i.split()
            for word in sentence:
                if word.lower() not in unique_names:
                    unique_names.append(word.lower())
        return unique_names

    def fit_transform(self, corpus):
        unique_names = self.get_feature_names()
        transformed_matrix = []
        one_part = []
        counter = 0
        for i in corpus:
            sentence = i.split()
            for unique_name in unique_names:
                for name in sentence:
                    if unique_name == name.lower():
                        counter += 1
                one_part.append(counter)
                counter = 0
            transformed_matrix.append(one_part)
            one_part = []
        return transformed_matrix


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

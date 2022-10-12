class CountVectorizer:
    def __init__(self):
        pass

    def get_feature_names(self):
        array_1 = []
        for i in corpus:
            a = (i.split())
            for z in a:
                if z.lower() not in array_1:
                    array_1.append(z.lower())
        return array_1

    def fit_transform(self, corpus):
        array_1 = []
        array_2 = []
        array_3 = []
        array_4 = []
        array_5 = []
        self.corpus = corpus
        a = (corpus[0].split())
        for q in a:
            array_2.append(q.lower())
        a = (corpus[1].split())
        for q in a:
            array_3.append(q.lower())
        for i in corpus:
            a = (i.split())
            for z in a:
                if z.lower() not in array_1:
                    array_1.append(z.lower())
        for i in array_1:
            d = 0
            for q in array_2:
                if i == q:
                    d += 1
            array_4.append(d)
        for i in array_1:
            d = 0
            for q in array_3:
                if i == q:
                    d += 1
            array_5.append(d)
        array_6 = [array_4, array_5]
        return array_6


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)

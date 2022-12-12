from math import log


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


class TfidfTransformer:
	def tf_transform(self, count_matrix):
		tf_matrix = []
		for part in count_matrix:
			sum_of_part = sum(part)
			new_part = []
			for el in part:
				new_part.append(round(el / sum_of_part, 3))
			tf_matrix.append(new_part)
		return tf_matrix

	def idf_transform(self, count_matrix):
		if not count_matrix:
			return []
		idf_vector = []
		all_documents = len(count_matrix)
		for term in range(len(count_matrix[0])):
			docs_with_term = 0
			for i in range(all_documents):
				docs_with_term += bool(count_matrix[i][term])
			idf = log((all_documents + 1) / (docs_with_term + 1)) + 1
			idf_vector.append(round(idf, 1))
		return idf_vector

	def fit_transform(self, count_matrix):
		vector = self.idf_transform(count_matrix)
		matrix = self.tf_transform(count_matrix)
		fit_matrix = []
		for row in matrix:
			fit_matrix.append([round(tf * idf, 3) for tf, idf in zip(row, vector)])
		return fit_matrix


class TfidfVectorizer(CountVectorizer):
	def __init__(self):
		super().__init__()
		self.tf_idf = TfidfTransformer()

	def fit_transform(self, corpus):
		count_matrix = super().fit_transform(corpus)
		return self.tf_idf.fit_transform(count_matrix)


if __name__ == '__main__':
	corpus = [
		'Crock Pot Pasta Never boil pasta again',
		'Pasta Pomodoro Fresh ingredients Parmesan to taste'
	]
	vectorizer = TfidfVectorizer()
	tfidf_matrix = vectorizer.fit_transform(corpus)
	assert vectorizer.get_feature_names() == ['crock', 'pot', 'pasta', 'never', 'boil', 'again',
										'pomodoro', 'fresh', 'ingredients', 'parmesan', 'to', 'taste']
	assert tfidf_matrix == [[0.2, 0.2, 0.286, 0.2, 0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
							[0.0, 0.0, 0.143, 0.0, 0.0, 0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]
	print(vectorizer.get_feature_names())
	print(tfidf_matrix)

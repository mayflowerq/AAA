from math import log


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


if __name__ == '__main__':
	count_matrix = [
		[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
		[0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
	]
	transformer = TfidfTransformer()
	tfidf_matrix = transformer.fit_transform(count_matrix)
	assert tfidf_matrix == [[0.2, 0.2, 0.286, 0.2, 0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
							[0.0, 0.0, 0.143, 0.0, 0.0, 0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]
	print(tfidf_matrix)

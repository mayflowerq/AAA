from math import log


def idf_transform(count_matrix):
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


if __name__ == '__main__':
    count_matrix = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    idf_matrix = idf_transform(count_matrix)
    assert idf_matrix == [1.4, 1.4, 1.0, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4]
    print(idf_matrix)

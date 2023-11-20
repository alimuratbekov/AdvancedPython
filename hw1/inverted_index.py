from __future__ import annotations

from typing import Dict, List
import json


class InvertedIndex:
    def __init__(self, inverted_index: Dict[str, list]):
        if inverted_index is None:
            raise ValueError
        self.inverted_index = inverted_index

    def query(self, words: List[str]) -> List[int]:
        """Return the list of relevant documents for the given query"""

        words_occ = [self.inverted_index[word] for word in words]

        if len(words) == 1:
            return words_occ[0]
        else:
            common_ind = list(set(words_occ[0]).intersection(*map(set, words_occ[1:])))
            return common_ind

    @staticmethod
    def set_default(obj):
        if isinstance(obj, set):
            return list(obj)
        raise TypeError

    def dump(self, filepath: str) -> None:
        with open(filepath, 'w') as f:
            json.dump(self.inverted_index, f, default=self.set_default)

    @classmethod
    def load(cls, filepath: str) -> InvertedIndex:
        with open(filepath, 'r') as f:
            inv_index_dict = json.load(f)

        return cls(inv_index_dict)


def load_documents(filepath: str) -> Dict[int, str]:
    with open(filepath, 'rb') as f:
        dataset = f.read()
    dataset = dataset.decode()

    d = dict()
    for page in dataset.split('\n'):
        if page == '':
            continue
        split_page = page.split('\t')
        ind = int(split_page[0])
        text = ' '.join(split_page[1:])
        d[ind] = text

    return d


def build_inverted_index(documents: Dict[int, str]) -> InvertedIndex:
    from collections import defaultdict
    import re

    all_indexes = list()
    for ind, text in documents.items():

        words = set(re.sub('[^a-zA-Z0-9 \n]', '', text).lower().split())
        all_indexes.extend([(word, ind) for word in words])

    inv_index_dict = defaultdict(set)
    for word_ind in all_indexes:
        word = word_ind[0]
        ind = word_ind[1]

        inv_index_dict[word].update({ind})

    inv_index_dict = dict(sorted(inv_index_dict.items()))
    inverted_index = InvertedIndex(inv_index_dict)

    return inverted_index


def main():
    documents = load_documents("wikipedia_sample")
    inverted_index = build_inverted_index(documents)
    inverted_index.dump("inverted_index.json")
    inverted_index = InvertedIndex.load("inverted_index.json")
    document_ids = inverted_index.query(["two", "words"])


if __name__ == "__main__":
    main()

import pytest

from inverted_index import InvertedIndex
from inverted_index import load_documents
from inverted_index import build_inverted_index


def test_load_documents():
    # from pdb import set_trace; set_trace()
    documents = load_documents('wikipedia_sample')


def test_inverted_index_exception_with_none_input():
    with pytest.raises(ValueError):
        InvertedIndex(inverted_index=None)


def test_build_inverted_index():
    # from pdb import set_trace; set_trace()
    documents = load_documents('wikipedia_sample')
    inverted_index = build_inverted_index(documents)

    assert type(inverted_index) == InvertedIndex


def test_inverted_index_dump():
    documents = load_documents('wikipedia_sample')
    inverted_index = build_inverted_index(documents)

    inverted_index.dump(filepath='inverted_index.json')


def test_inverted_index_load():
    inverted_index = InvertedIndex.load('inverted_index.json')


def test_inverted_index_has_many_links():
    inverted_index = InvertedIndex.load('inverted_index.json')

    max_len = max([len(v) for k, v in inverted_index.inverted_index.items()])

    assert max_len > 1


def test_inverted_index_query_one_word():
    inverted_index = InvertedIndex.load('inverted_index.json')

    expected_index = [956, 2869, 2222]
    outcome_index = inverted_index.query(['chamomile'])

    assert expected_index == outcome_index


def test_inverted_index_query_many_words():
    inverted_index = InvertedIndex.load('inverted_index.json')

    expected_index = [6021, 6667, 2581, 7575, 5783, 8864, 4266, 6698, 5295, 6834, 9010, 6840, 5311, 8904, 2899, 5213, 4320, 7392, 4706, 5739, 4086, 2807, 4214]
    outcome_index = inverted_index.query(['python', 'code'])

    assert expected_index == outcome_index

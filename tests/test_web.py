import pytest
import duckgo


@pytest.mark.network
def test_web_search_basic():
    results = duckgo.web('panda')

    assert results
    assert len(results) > 0

    assert results[0].title
    assert results[0].snippet
    assert results[0].url
    assert 'panda' in results[0].title.lower()
    assert 'panda' in results[0].snippet.lower()


@pytest.mark.network
def test_web_search_large_n():
    results = duckgo.web('panda', n_results=201)

    assert results
    assert len(results) > 0

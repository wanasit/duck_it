import pytest
import duckgo


@pytest.mark.network
def test_image_search_basic():
    results = duckgo.image('panda')

    assert results
    assert len(results) > 0

    assert results[0].title
    assert results[0].image_url
    assert results[0].width > 0
    assert results[0].height > 0
    assert 'panda' in results[0].title.lower()


@pytest.mark.network
def test_image_search_large_n():
    results = duckgo.image('panda', n_results=201)

    assert results
    assert len(results) > 0

    assert results[0].title
    assert results[0].image_url
    assert 'panda' in results[0].title.lower()
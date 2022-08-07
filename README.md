# DuckGo
Search DuckDuckGo for websites, images, etc.

## Usage

Install the library via pip:
```bash
pip install duckgo
```

Then, import `duckgo` to search webs, images, or videos via DuckDuckGo:
```python
import duckgo

results = duckgo.web('panda', n_results=20)

# len(results) == 20
# results[0].title == 'Giant panda - Wikipedia'
# results[0].url == 'https://en.wikipedia...'
# results[0].snippet == 'The giant <b>panda</b>...'
```

### Image Search
(Search results similar to the _Images_ tab on DuckDuckGo)

```python
import duckgo

results = duckgo.image('panda')

# results[0].title == '...'
# results[0].image_url == '.....jpg'
```


### Video Search
(Search results similar to the _Videos_ tab on DuckDuckGo)

```python
import duckgo

results = duckgo.video('panda')

# results[0].title == '...'
# results[0].url == 'http://youtube.com/watch?v=...'
```
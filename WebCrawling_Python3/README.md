# WebCrawling-Python

## Beautiful Soup 설치
```
pip install beautifulsoup4
```

### import
```
from bs4 import BeautifulSoup
```
```
import bs4
```

### HTML file Open
```python
with open("example.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
```
# Scholar google related articles scraper

This repository search the scholar google according to the query input, it scrapes the result articles and continue searching relatd articles. It repeat the proces five times. The best input of the program is an article name. 

Program requires several libraries:
- requests
- BeautifulSoup
- scholarly - however, I commented the code using this library, therefore it can be removed from the program

```pyton
pip install requests
pip install BeautifulSoup4
python gs_related_work.py.py "Product quantization for nearest neighbor search"
```


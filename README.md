# Scholar google related articles scraper

This program searches the scholar google according to the query input, it scrapes the result articles and continues searching for related articles. It repeats the process five times. The best input of the program is an article name. 

The program requires several libraries:
- requests
- BeautifulSoup

```bash
pip install requests
pip install BeautifulSoup4
python gs_related_work.py "Product quantization for nearest neighbor search"
```

Warning: The scholar.google.com start to verify your requests after several attempts of this program and the program will stop working.

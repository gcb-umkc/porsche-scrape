The base URL specifies the newsroom website. 
```python
base = 'https://newsroom.porsche.com'
```

Then it uses requests to get a response from the newsroom website. 
```python
reponse = requests.get(base)
html = reponse.text
```

It then parses that HTML document into BeautifulSoup4 to allow easier extraction of information, finding the HTML elements of each article.
```python
soup = BeautifulSoup(html, 'html.parser')
articles = soup.find_all('article', 'teaser')
```

Using BS4 I filter out the relevant information: the date and the URL information using elements of the HTML DOM. 
```python
	try:
		date = article.time['datetime']
		date = datetime.strptime(date, "%d/%m/%Y")
		month = date.month
	except:
		month = '0'
	
	try:
		link = article.find_all('a')[0].get('href')

		if link[0] == "/":
			url = base + link
		else:
			url = link
```

Then if it is a valid entry, I add the URL to a list and then it can append the list. 
```python
except:
		url = 'None'
	if month == 6 :
		if(url != "#"):
			urls.append(url)
```

The program then prints the list of URLs for validation. 
```python
print(urls)
```
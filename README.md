# Porsche Scrape

In this we take PDFs from the Porsche Newsroom and try to extract meaningful data from them in a JSON format. 

First is a basic scrape of all the PDFs within the month of July from the first to the 15th, resulting in 25 PDFs.

We then use PyMuPDF to extract information from that and convert it into a JSON format. 

Finally we process the PDFs to remove extraneous data to allow for proper usage during the NN training stages, which are next. 

### from cgitb import text
### from turtle import clear
### from urllib.request import HTTPDefaultErrorHandler
### import fitz, sys, json, jsonlines

This is is a script that will turn the pdf into a JSONLines file of all of the paragaphs in the pdf. This code also includes a script that will automatically scrape the headers and apply the headers to the paragraphs that fall under such header


	def web_scraper(filename):

    # Opens the PDF and scrapes all of the text within the PDF
    doc = fitz.open(filename)
    text_blocks = []
    heading_list = []
    count = 0
    for page in doc:
        text = page.get_text("blocks")
        for block in text:
            if(block[4][0:7] == "<image:"): # If the block is an image, it does not include it in the text_block list
                continue
            if(block[4][-1] != "." and block[4][-1] != "\"" and len(block[4]) < 100):
                heading_list.append(block[4])
            
            dict = {
                "url" : "https://newsroom.porsche.com/en/2022/motorsports/porsche-tag-heuer-esports-supercup-saison-2022-race-10-monza-28628.html",
                "heading" : "",
                "prompt" : "",
                "paragraph" : block[4]
            }
            text_blocks.append(dict) # Puts all of the text_blocks into a dictionary with the url and the string as the paragraph, which is then stored in a list

    # Saving the first text block which contains the name of the article
    filename = text_blocks[0]["paragraph"] + ".jsonl"


    # Automatically applies headers to the text based on whether the text is after one after and before another header
    heading_counter = 0
    current_header = heading_list[heading_counter]
    for text in text_blocks:
        if(heading_counter != len(heading_list)):
            if(heading_list[heading_counter + 1] == text["paragraph"]):
                current_header = heading_list[heading_counter + 1]
                heading_counter += 1
                

        text["heading"] = current_header

    

    # removes the any JSONs where the text is a header
    count = len(heading_list) - 1
    for i in range(len(text_blocks) -1, -1, -1):
        if text_blocks[i]["paragraph"] == heading_list[count]:
            text_blocks.pop(i)
            count -= 1
        
        
    

    # Transforms the dictionaries into JSONs and writes all of them into a JSONLines file
    with open(filename, "w") as outfile:
        for i in range(0,len(text_blocks)):
            outfile.write(json.dumps(text_blocks[i]) + "\n")
                
    


web_scraper(sys.argv[1])

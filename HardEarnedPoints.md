### from cgitb import text
### from turtle import clear
### import fitz, sys, json, jsonlines


Scrapes from the Hard earned points Porsche article and will turn each pdf into a JSONLines file which includes all of the paragraphs from the acticle, with each paragraph labled with a header and a prompt to questions.

	  
	def web_scraper(filename):
	# Opens the PDF and scrapes all of the text within the PDF
	doc = fitz.open(filename)
    text_blocks = []
    count = 0
    for page in doc:
        text = page.get_text("blocks")
        for block in text:
            if(block[4][0:7] == "<image:"): # If the block is an image, it does not include it in the text_block list
                continue
            else:
                if block[4].count(" ") > 5:
                    dict = {
                        "url" : "https://newsroom.porsche.com/en/2022/motorsports/porsche-abb-fia-formel-e-championship-2022-race-9-jakarta-indonesia-28554.html",
                        "heading" : "",
                        "prompt" : "",
                        "paragraph" : block[4]
                    }
                    text_blocks.append(dict) # Puts all of the text_blocks into a dictionary with the url and the string as the paragraph, which is then stored in a list
    # Saving the first text block which contains the name of the article
    >filename = text_blocks[0]["paragraph"] + ".jsonl"

    
    # Popping out unnecessary paragraphs
	 for i in range(51, 35, -1):
        text_blocks.pop(i)
     text_blocks.pop(29)
    text_blocks.pop(28)
    text_blocks.pop(25)
    text_blocks.pop(23)
    text_blocks.pop(21)
    text_blocks.pop(18)
    text_blocks.pop(16)
    text_blocks.pop(14)
    text_blocks.pop(13)
    text_blocks.pop(5)
    text_blocks.pop(0)


    # Labeling every paragraph with a header
    for i in range(1,4):
        text_blocks[i]["heading"] = "Race 9"

    for i in range(4,6):
        text_blocks[i]["heading"] = "Comments on the Jakarta E-Prix, Race 9"

    text_blocks[6]["heading"] = "Next Up"

    for i in range(6,11):
        text_blocks[i]["heading"] = "The preview"

    for i in range(11,13):
        text_blocks[i]["heading"] = "Florian Modlinger (Director Factory Motorsport Formula E)"

    for i in range(13,16):
        text_blocks[i]["heading"] = "André Lotterer (Porsche works driver, #36)"

    for i in range(16,18):
        text_blocks[i]["heading"] = "Pascal Wehrlein (Porsche works driver, #94)"

    text_blocks[18]["heading"] = "The racetrack"

    text_blocks[19]["heading"] = "Porsche Taycan Turbo S als Safety Car"

    text_blocks[20]["heading"] = "The Media Service"

    text_blocks[21]["heading"] = "The Porsche 99X Electric"

    for i in range(22,24):
        text_blocks[i]["heading"] = "Formula E"

    text_blocks[24]["heading"] = "Porsche in Formula E"
    

    # Labeling the paragraphs with question prompts
    text_blocks[11]["prompt"] = "Formula E heads into the second half of season 8 in Jakarta. What have been the highlights so far and what needs to improve?"

    text_blocks[12]["prompt"] = "How much more preparation is needed to tackle a new racetrack like in Jakarta?"

    text_blocks[13]["prompt"] = "You're the only driver this season to progress into the knock-out qualifying duels at all races. What makes you so strong and how do you feel about this record? "

    text_blocks[14]["prompt"] = "You're the only driver this season to progress into the knock-out qualifying duels at all races. What makes you so strong and how do you feel about this record? "

    text_blocks[15]["prompt"] = "How would you sum up your first half of the season and what do you expect for the remaining races?"

    text_blocks[16]["prompt"] = "This is the first outing in Jakarta for Formula E. Are you excited about the new track?"

    text_blocks[17]["prompt"] = "You claimed the first Formula E victory for Porsche in Mexico. Are you satisfied with the first half of your season?"



    # Transforms the dictionaries into JSONs and writes all of them into a JSONLines file
    with open(filename, "w") as outfile:
        for i in range(1,len(text_blocks)):
            outfile.write(json.dumps(text_blocks[i]) + "\n")
                
    


web_scraper(sys.argv[1])

from cgitb import text
import fitz, sys, json, jsonlines

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
                        "url" : "https://newsroom.porsche.com/en/2022/motorsports/porsche-fia-wec-world-endurance-championship-round-3-24-hour-race-le-mans-france-28615.html",
                        "heading" : "",
                        "prompt" : "",
                        "paragraph" : block[4]
                    }
                    text_blocks.append(dict) # Puts all of the text_blocks into a dictionary with the url and the string as the paragraph, which is then stored in a list


    # Saving the first text block which contains the name of the article
    filename = text_blocks[0]["paragraph"] + ".jsonl"

    # Popping away useless information
    for i in range(92, 81, -1):
        text_blocks.pop(i)

    text_blocks.pop(74)
    text_blocks.pop(73)
    text_blocks.pop(62)
    text_blocks.pop(61)
    text_blocks.pop(53)
    text_blocks.pop(52)
    text_blocks.pop(51)
    text_blocks.pop(46)
    text_blocks.pop(45)
    text_blocks.pop(14)
    text_blocks.pop(13)
    text_blocks.pop(0)


    # Labeling every paragraph with a header
    for i in range(1,8):
        text_blocks[i]["heading"] = "Race"

    for i in range(9,11):
        text_blocks[i]["heading"] = "Drivers' comments after the race"

    for i in range(12,13):
        text_blocks[i]["heading"] = "Newsflash"

    for i in range(14,15):
        text_blocks[i]["heading"] = "Interim report 2"

    for i in range(16,18):
        text_blocks[i]["heading"] = "Interim report 1"

    for i in range(19,21):
        text_blocks[i]["heading"] = "Makowiecki and Estre start the 24-hour-race"
    
    for i in range(23,24):
        text_blocks[i]["heading"] = "Drivers' comments after 16 hours of racing"

    for i in range(25,27):
        text_blocks[i]["heading"] = "Interim report 1"

    for i in range(28,31):
        text_blocks[i]["heading"] = "Makowiecki and Estre start the 24-hour-race"

    for i in range(32,35):
        text_blocks[i]["heading"] = "Drivers' comments on the starting phase"

    for i in range(36,39):
        text_blocks[i]["heading"] = "Hyperbole"

    for i in range(40,41):
        text_blocks[i]["heading"] = "Drivers' impressions of the Hyperbole"

    for i in range(42,44):
        text_blocks[i]["heading"] = "Qualifying"

    text_blocks[45]["heading"] = "Drivers' impressions after the qualifying"

    for i in range(46,50):
        text_blocks[i]["heading"] = "Test Day"

    for i in range(51,52):
        text_blocks[i]["heading"] = "Drivers' comments after the pre-test"

    for i in range(53,59):
        text_blocks[i]["heading"] = "The preview"

    for i in range(60,61):
        text_blocks[i]["heading"] = "The Porsche GT Team Drivers"

    text_blocks[62]["heading"] = "The customer teams"

    for i in range(63,69):
        text_blocks[i]["heading"] = "Drivers' comments before the race"

    # A text block that I forgot to pop earlier
    text_blocks.pop(22)


    # Transforms the dictionaries into JSONs and writes all of them into a JSONLines file
    with open(filename, "w") as outfile:
        for i in range(1,len(text_blocks)):
            outfile.write(json.dumps(text_blocks[i]) + "\n")
                
    
   

web_scraper(sys.argv[1])

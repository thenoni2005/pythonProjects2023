# ANTHONY TRUJILLO
# 9/22/2022
# MADLIB TAKE 2

# imports


# globals
OGTEXT2 = """
The (body) (text) or (body) copy is the (text) forming the main content of a 
(book), (magazine), (web_page), or any other (printed) or (digital_work). 
This is as a contrast to both additional components such as 
(headings), (images), (charts), (footnotes) etc. on each (page), 
and also the (pages) of front matter that form the introduction to a (book). 
"""

OGTEXT2 = OGTEXT2.replace("body","(body)")
OGTEXT2 = OGTEXT2.replace("book","(book)")
OGTEXT2 = OGTEXT2.replace("text","(text)")
#print(OGTEXT2)
#functions


#main

def main():
    text2 = OGTEXT2

    body = input("give me a name")
    text = input("give me an object")
    book = input("give me an object")
    magazine = input("give me an object")
    web_page = input("give me anything")
    printed = input("give me an action")
    digital_work = input("give me an action")
    headings = input("give me a thing")
    images = input("give me an object")
    charts = input("give me an object")
    footnotes = input ("give me a thing")
    pages = input ("give me an object")

    text2 = text2.replace("(body)",body)
    text2 = text2.replace("(text)",text)
    text2 = text2.replace("(book)",book)
    text2 = text2.replace("(magazine)",magazine)
    text2 = text2.replace("(web_page)",web_page)
    text2 = text2.replace("(printed)",printed)
    text2 = text2.replace("(digital_work)",digital_work)
    text2 = text2.replace("(headings)",headings)
    text2 = text2.replace("(images)",images)
    text2 = text2.replace("(charts)",charts)
    text2 = text2.replace("(footnotes)",footnotes)
    text2 = text2.replace("(pages)",pages)
    print(text2)
main()
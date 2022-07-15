from tkinter.messagebox import RETRY
from traceback import print_tb
from bs4 import BeautifulSoup
import requests
import pdfkit  
import sys

# function to extract html document from given url
def getHTMLdocument(url):
      
    # request for HTML document of given url
    response = requests.get(url)
      
    # response will be provided in JSON format
    return response.text

def getSoup(url):
    html_document = getHTMLdocument(url)
    return BeautifulSoup(html_document, 'html.parser')

def geProblemList(soup):
    problems = []
    for detailsSection in soup.findAll("details"):
        for table in detailsSection.findAll("table"):
            for idx, tableRows in enumerate(table.findAll("tr")):
                if idx != 0 :
                    for index, tableData in enumerate(tableRows.findAll("td")):
                        if index == 0:
                            for a in tableData.find_all('a', href=True):
                                problems.append(a['href'])
    return problems


def generateHTML(url, language):
    html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body>
{}
<body>
</html>
""".format(extractArticle(url, language))
    return html_content

def extractArticle(url, language):
    soup = getSoup(url)
    content = soup.find('div', id = 'content')
    article = content.find_all("article")
    for idx, heading in enumerate(article[0].find_all("h2", {"class":"tabtitle"})):
        if language == "java" and idx %2 == 0:
            heading.decompose()
        if language == "cpp" and idx %2 == 1:
            heading.decompose()
    
    for idx, codeblock in enumerate(article[0].find_all("div", {"class":"tabcontent"})):
        if language == "java" and idx %2 == 0:
            codeblock.decompose()
        if language == "cpp" and idx %2 == 1:
            codeblock.decompose()
            

    for footer in article[0].find_all("footer"):
        footer.decompose()
    for blockquote in article[0].find_all("blockquote"):    
        blockquote.decompose()
    for figure in article[0].find_all("figure"):
        figure.decompose()
    for ins in article[0].find_all("ins"):
        ins.decompose()
    for script in article[0].find_all("script"):
        script.decompose()
    return article[0].prettify()

if __name__ == "__main__":
    langauge = "java"
    if len(sys.argv) > 1:
        langauge = sys.argv[1]
    print("Welcome to the PDF generator, You have choose the language {}".format(langauge))
    url_to_scrape = "https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems/"
    problems = geProblemList(getSoup(url_to_scrape))
    
    index = 74

    for problem in problems[74:]:
        result = ""
        name = problem.split("/")[-2]
        print("Working for problem {}".format(problem))
        try: 
            result = generateHTML(problem, langauge)
            pdfkit.from_string(result, "./{}.pdf".format(name))
            index= index+1
            print(index)
        except:
            print("Error getting content for the problem : {}".format(name))






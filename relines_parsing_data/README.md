#PARSING DATA from the sites

##1) input data:
###url: url of page
###width: width of text's line in output
###link: to save links to images or not in the text
###result: to save result to the file or not

##2) rules of using script:
###1) cd relines_parsing_data/
###1)  python .\parsing_cmd.py  
###--url="link_to_the_page"  
###--width=width_of_line
###--link="Choose True or False if you want to save links of images in the text"   
###--result="Choose True or False if you want to save result to the file or not"

### P.S. You should pass first parameter in another case You will get error message
### url param should be type str
### width param should be type number (default=70)
### link param should be type str and ("False" or "True") (default=True)
### result param should be type str and ("True" or "False") (default=True)

### Examples of input:
...

###installed_packages
pip install lxml
pip install requests
pip install beautifulsoup4
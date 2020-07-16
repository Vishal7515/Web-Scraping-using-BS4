import requests
import bs4
res = requests.get('#url')
#to get to know the type of variable that holds the requests.
type(res)
#to obtain all the html code of a particular website.
res.text
#convert the soup variable to type soup (vvimp)
soup = bs4.BeautifulSoup(res.text,'#html,lxml etc')
hi = soup.select('title')
hi # gives array of all tags with whatever is selected.
hi[0].getText() #gives us the text in that particular array entry.
'''you can save this information into a text file or a csv etc which can be
later on used for various purposes.
Module used are Beautiful Soup 4 and Request'''

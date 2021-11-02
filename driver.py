import requests
import datetime
from datetime import date

#imports date and then formats to string so that we can take out dashes.
today = date.today()
today_str = datetime.datetime.strftime(today,'%Y%m%d')

#url with f string so that we can insert todays date from above
url = f"https://marketdata.theocc.com/flex-reports?reportType=PR&optionType=E&reportDate={today_str}"
r = requests.get(url, allow_redirects=True)

print("\n\nEnter symbol as shown on file\nfor exampe, if underlying is EIX enter 1EIX\n\n")
security = str(input())

#opens download and saves it to current working directory
open('prices.txt', 'wb').write(r.content)


#opens price file up
local_file = open("prices.txt","r")


#sets flag and index to 0
flag = 0
index = 0

#loops through file
for line in local_file:
    index += 1

    #checking to see if string is on that line
    if security in line:
        flag = 1
        break

if flag == 0:
    print("security not found")

else:
    print(line)


local_file.close()



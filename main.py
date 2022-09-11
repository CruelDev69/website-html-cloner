import httpx
print('''
     _    _               _ 
    / \  | |__   __ _  __| |
   / _ \ | '_ \ / _` |/ _` |
  / ___ \| | | | (_| | (_| |
 /_/   \_\_| |_|\__,_|\__,_|
                            
Author: Ahad#3257                            
Website: https://itscruel.cf
Github: https://github.com/CruelDev69/website-html-cloner                           
''')
url = input("Enter your website URL: ")
r = httpx.get(url)

with open("code.txt", "a") as f:
    f.write(f"Website: {url}\n\nCode:\n{r.text}\n\n\n")
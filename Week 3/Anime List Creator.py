import requests
import sys
import redis

loop=False




animeList = open('animeList.txt', 'a')

    
print('Type the corresponding number to navigate.\n \n 1. Search Title\n 2. View or delete anime list\n 3. Sync list with database \n ')
mainMenu=int(input())
print("\n ")

if mainMenu == 1:

 while loop== False:
    
    url = "https://anime-db.p.rapidapi.com/anime"

    print("Search Anime: ")
    print("\n")
    search=input("")
    print("\n")

    querystring = {"page":"1","size":"10","search":search,"sortBy":"ranking","sortOrder":"asc"}


    headers = {
    	"x-rapidapi-key": "8e3b7b1dffmsh12c88794e9a472ap136f75jsncdfcd468c995",
    	"x-rapidapi-host": "anime-db.p.rapidapi.com"
    }
    
    try:
      response = requests.get(url, headers=headers, params=querystring).json()


     

      title1 = response['data'][0]['title']
      title2 = response['data'][1]['title']
      title3 = response['data'][2]['title']
      title4 = response['data'][3]['title']
      title5 = response['data'][4]['title']
      title6 = response['data'][5]['title']
      title7 = response['data'][6]['title']
      title8 = response['data'][7]['title']
      title9 = response['data'][8]['title']
      title10 = response['data'][9]['title']
     


      print(" 1.",title1,"\n 2.",title2,"\n 3.",title3,"\n 4.",title4,"\n 5.",title5,"\n 6.",title6,"\n 7.",title7,
          "\n 8.",title8,"\n 9.",title9,"\n 10.",title10,"\n"  )
      loop=True
 
         

    except:
      print("Error: Title not found.\n")
      loop=False
     
    
 titleList=['',title1,title2,title3,title4,title5,title6,title7,title8,title9,title10]
   

 print('\n Press the corresponding number to add to your list or "0" to exit.\n')
   
 addAnime=int(input())
    
    
 listVar=str(titleList[addAnime])
    
    

    
 with open('animeList.txt', "a") as animeList:
        animeList.write("\n")
        animeList.write(listVar)
 print("\n")       
 print("Save to File Successful.")


elif mainMenu==2:
 with open('animeList.txt', 'r') as animeList:
    print(animeList.read())
    
 print("\n")
 print("Press '1' to start a new list or any key to exit. ")
 print("\n")
 
 menu2=input("")
 if menu2== "1":
     animeList = open('animeList.txt', 'w')
     
 else:
     sys.exit()
     
    
elif mainMenu==3:
    
    r = redis.Redis(
        host='redis-19361.c280.us-central1-2.gce.redns.redis-cloud.com',
        port=19361,
        decode_responses=True,
        username="default",
        password="wclKLrcJLv0pSDo0c11boi4PZ7C5Le33",
    )
    
    with open('animeList.txt', 'r') as file:
           text_content = file.read()
           r.set('key_name', text_content)
           result= r.get('key_name')
           print('List sync successful')
          
    


else:
     print("That is not a valid option number.")   
    

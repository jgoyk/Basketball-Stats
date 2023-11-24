import requests
from tabulate import tabulate
from bs4 import BeautifulSoup

def powerRank():
  URLRank = "http://powerrankingsguru.com/nba/team-power-rankings.php"
  pageRank = requests.get(URLRank)
  soupRank = BeautifulSoup(pageRank.content, "html.parser")
  count = 0
  for div in soupRank.find_all("div", {"class": "team-name-v2"}):
    count = count + 1
    span = div.find("span", {"class": "full-name"})
    abbr = div.find("span", {"class": "abbrv"})
    abbrv = abbr.get_text()
    divName = span.get_text()
    print(str(count) + ". " + divName + " (" + abbrv + ")")
  print("\n")
        
def standings():
  teamList = []
  winList = []
  lossList = []
  winlossList = []

  
  URLrank = "https://basketball.realgm.com/nba/standings"
  pageStand = requests.get(URLrank)
  soupStand = BeautifulSoup(pageStand.content, "html.parser")
  standBody = soupStand.find_all("tbody")
  for thing in standBody:
    for item in thing:
      for item2 in item.find_all("td"):
        item3 = item2.find(attrs={"rel" : "stainfo"})
    ##teamList.append(item.select('th[data-stat="team_name"]')[0].get_text())
   ## winList.append(item.select('th[data-stat="wins"]')[0].get_text())
   ## lossList.append(item.select('th[data-stat="losses"]')[0].get_text())
   ## winlossList.append(item.select('th[data-stat="win_loss_pct"]')[0].get_text())
  
  ##print(teamList)
 ## print(winList)

##standings()
def player(league):
 
  first = input("\nWhat is the players full name?\n \n ")
  year = input("\nWhat year would you like stats from? \n \n ")
  fullName = first.strip() 
  fullName= fullName.lower()
  location = int(fullName.find(" ")) +1
  if league == "NBA":
    URL1= "https://www.basketball-reference.com/players/" + fullName[location].lower() + "/"
  if league == "CBB":
    URL1 = "https://www.sports-reference.com/cbb/players/" + fullName[location].lower() + "-index.html"
  page1 = requests.get(URL1)
  soup1 = BeautifulSoup(page1.content, "html.parser")
  
  if league == "NBA":
    bodyNBA = soup1.find("tbody")
    for tr in bodyNBA.find_all('tr'):
        th = tr.find('th')
        name = th.get_text()
        name = name.lower()
        if name == fullName :
          links = th.find('a')
          link = links.get('href')
    URL = "https://www.basketball-reference.com" + link.removesuffix('.html')  + "/gamelog/" + year
  if league == "CBB":
    body1 = soup1.find("div")
    for tr in body1.find_all('p'):
        name = tr.get_text()
        location = name.find("(")
        name = name[:location].lower()
        name = name.strip()
        if name.lower() == fullName :
          links = tr.find('a')
          link = links.get('href')
    URL = "https://www.sports-reference.com" + link.removesuffix('.html')  + "/gamelog/" + year
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  body = soup.find("tbody")
  

  dateList = []
  oppList = []
  minList = []
  fgList = []
  fgaList = []
  fgpctList = []
  fg3List = []
  fg3aList = []
  fg3pctList = []
  ftList = []
  ftaList = []
  ftpctList = []
  ptsList = []
  orbList = []
  drbList = []
  trbList = []
  astList = []
  stlList = []
  blkList = []
  tovList = []



  
  count = 0
  if league == "NBA":
    for trs in body.find_all("tr", id=lambda value: value and value.startswith('pgl_basic.')):
      count = count + 1
      dateList.append(trs.select('td[data-stat="date_game"]')[0].get_text())
      oppList.append(trs.select('td[data-stat="opp_id"]')[0].get_text())
      minList.append(trs.select('td[data-stat="mp"]')[0].get_text())
      fgList.append(trs.select('td[data-stat="fg"]')[0].get_text())
      fgaList.append(trs.select('td[data-stat="fga"]')[0].get_text())
      fgpctList.append(trs.select('td[data-stat="fg_pct"]')[0].get_text())
      fg3List.append(trs.select('td[data-stat="fg3"]')[0].get_text())
      fg3pctList.append(trs.select('td[data-stat="fg3_pct"]')[0].get_text())
      fg3aList.append(trs.select('td[data-stat="fg3a"]')[0].get_text())
      ftList.append(trs.select('td[data-stat="ft"]')[0].get_text())
      ftaList.append(trs.select('td[data-stat="fta"]')[0].get_text())
      ftpctList.append(trs.select('td[data-stat="ft_pct"]')[0].get_text())
      ptsList.append(trs.select('td[data-stat="pts"]')[0].get_text())
      orbList.append(trs.select('td[data-stat="orb"]')[0].get_text())
      drbList.append(trs.select('td[data-stat="drb"]')[0].get_text())
      trbList.append(trs.select('td[data-stat="trb"]')[0].get_text())
      astList.append(trs.select('td[data-stat="ast"]')[0].get_text())
      stlList.append(trs.select('td[data-stat="stl"]')[0].get_text())
      blkList.append(trs.select('td[data-stat="blk"]')[0].get_text())
      tovList.append(trs.select('td[data-stat="tov"]')[0].get_text())
  if league == "CBB":
    for trs in body.find_all("tr", id=lambda value: value and value.startswith('gamelog.')):
      count = count + 1
      dateList.append(trs.select('td[data-stat="date"]')[0].get_text())
      oppList.append(trs.select('td[data-stat="opp_name"]')[0].get_text())
      minList.append(trs.select('td[data-stat="mp"]')[0].get_text())
      fgList.append(trs.select('td[data-stat="fg"]')[0].get_text())
      fgaList.append(trs.select('td[data-stat="fga"]')[0].get_text())
      fgpctList.append(trs.select('td[data-stat="fg_pct"]')[0].get_text())
      fg3List.append(trs.select('td[data-stat="fg3"]')[0].get_text())
      fg3aList.append(trs.select('td[data-stat="fg3a"]')[0].get_text())
      fg3pctList.append(trs.select('td[data-stat="fg3_pct"]')[0].get_text())
      ftList.append(trs.select('td[data-stat="ft"]')[0].get_text())
      ftaList.append(trs.select('td[data-stat="fta"]')[0].get_text())
      ftpctList.append(trs.select('td[data-stat="ft_pct"]')[0].get_text())
      ptsList.append(trs.select('td[data-stat="pts"]')[0].get_text())
      orbList.append(trs.select('td[data-stat="orb"]')[0].get_text())
      drbList.append(trs.select('td[data-stat="drb"]')[0].get_text())
      trbList.append(trs.select('td[data-stat="trb"]')[0].get_text())
      astList.append(trs.select('td[data-stat="ast"]')[0].get_text())
      stlList.append(trs.select('td[data-stat="stl"]')[0].get_text())
      blkList.append(trs.select('td[data-stat="blk"]')[0].get_text())
      tovList.append(trs.select('td[data-stat="tov"]')[0].get_text())
    

  table = {
    "Date": dateList,
    "Opponent" : oppList, 
    "Mins" : minList, 
    "FG" : fgList, 
    "FGA" : fgaList, 
    "FG%": fgpctList, 
    "3pt FG" : fg3List, 
    "3pt FGA" : fg3List,
    "3pt FG%" : fg3pctList,
    "FTs"  : ftList,
    "FTa" : ftaList,
    "FT%" : ftpctList,
    "Pts" : ptsList,
    "ORB" : orbList,
    "DRB" : drbList,
    "TRB" : trbList,
    "ASTS" : astList,
    "STL" : stlList,
    "BLK" : blkList,
    "TOV" : tovList
  }
  def gameLoged():
    print(tabulate(table, headers='keys', tablefmt="fancy_grid"))
    print("\n")

  
  def gameAverage():
    print("[1] Points")
    print("[2] Total Rebounds")
    print("[3] Assists")
    print("[4] Steals")
    print("[5] Blocks")
    print("[6] Turnovers")
    print("[7] Exit")
    
    total = 0
    linesPrompts = True
    while linesPrompts == True: 
      linesPrompts = input("\nSelect an option.\n\n ")
      if linesPrompts == "1":
        stat = ptsList
        break
      elif linesPrompts == "2":
        stat = trbList
      elif linesPrompts == "3":
        stat = stlList
      elif linesPrompts == "4":
        stat = blkList
      elif linesPrompts == "5":
        stat = tovList
        break
      elif linesPrompts == "6":
        stat = ptsList
        break
      elif linesPrompts == "7":
        linesPrompts = False
      else:
        print("Select a valid option")

    
    for num in stat:
      total += int(num)
      average = total / count
    print("Average Points per Game:" + str(average)[:5])
    length = len(stat)
    game = input("\nHow many games would you like the average of?\n\n ")
    counts = int(game)
    num = length - counts 
    totals = 0
    while counts > 0 and num < length: 
      number = stat[num]
      totals += int(number)
      counts -= 1
      num += 1
    if counts == 0:
      avg = totals / int(game)
      print("\nAverage points per game for the last " + game + " game(s): " + str(avg)[:5] + "\n")
      percent = ((avg - average)*100)/average 
      if percent > 0: 
        print("This is a " + str(percent)[0:4] + "% increase")
      else : 
        print("This is a " + str(percent)[1:5] + "% decrease")
    else:
      print("\nNot enough games available\n")


  def lineCheck(): 
    print("Lines to Check: ")
    print("[1] Points")
    print("[2] Total Rebounds")
    print("[3] Assists")
    print("[4] Steals")
    print("[5] Blocks")
    print("[6] Turnovers")
    print("[7] Threes")
    linePrompt = input("\nSelect an option.\n\n ")
    line = input("\nWhat is the line you would like to check?\n\n ")
    team = input("\nWhat team are they playing?\n\n ")
    if linePrompt == "1":
      lineType = ptsList
    elif linePrompt == "2":
      lineType = trbList
    elif linePrompt == "3":
      lineType = astList
    elif linePrompt == "4":
      lineType = stlList
    elif linePrompt == "5":
      lineType = blkList
    elif linePrompt == "6":
      lineType = tovList
    elif linePrompt == "7":
      lineType = fg3List
      
    length = len(lineType)
    gamesHit = 0
    totalGames = length
    oppHit = 0
    numLine = float(line)
    totalopp = 0
    while length > 0: 
      length = length - 1
      number = float(lineType[length])
      team1 = oppList[length]
      
      if number > numLine:
        gamesHit += 1
        
      if team1 == team and number > numLine:
        oppHit += 1
        
      if team == team1:
        totalopp +=1
  
    print("\nYour player has scored over " + line + " in "+ str(gamesHit) + " out of "+ str(totalGames) + " games")
    print("\nAgainst this specific team, your player has scored over in "+ str(oppHit) +" out of " + str(totalopp) + " games\n")

  def overView():
    number = 0 
    for key, value in table.items():
      number = int(number) + 1
      if number == 13 or number == 16 or number == 15 or number == 18 or number == 19 or number == 20:
        pass
      else :
        continue
      total = 0
      for num in value:
        total += float(num)
        average = total / count
     
      length = len(value)
      game = 5
      counts = int(game)
      num = length - counts 
      totals = 0
      while counts > 0 and num < length: 
        number = value[num]
        totals += int(number)
        counts -= 1
        num += 1
      if counts == 0:
        avg = totals / int(game)
        percent = ((avg - average)*100)/average 
        print("Average "+ key + " per Game:" + str(average)[:5])
        if percent > 0: 
          print("\nAverage "+ key + " per game for the last " + str(game) + " games: " + str(avg)[:5] + " (a " + str(percent)[0:4] + "% increase)\n")
        else : 
          print("\nAverage "+ key + " per game for the last " + str(game) + " games: " + str(avg)[1:5] + " (a " + str(percent)[1:5] + "% decrease)\n")


  

  choice1 = True
  while choice1 != "5":
    print("\nOptions:\n")
    print("[1] Check the player's gamelog")
    print("[2] Get a player overview")
    print("[3] Check the player's point averages")
    print("[4] Check a line for the player")
    print("[5] Return to main menu")
    choice1 = input("\nSelect an option.\n\n ")
    print("\n")
    if choice1 == "1":
      choice1 = True
      gameLoged()
    elif choice1 == "2":
      choice1 = True
      overView() 
    elif choice1 == "3":
      choice1 = True
      gameAverage()
    elif choice1 == "4":
      choice1 = True
      lineCheck()
    elif choice1 == "5":
      break
    else :
      print("Select a valid option")
    
  


choice = True
while choice:
  print("[1] Select a NBA player")
  print("[2] Select a CBB player")
  print("[3] View Current Power Rankings")
  print("[4] Quit Program")
  choice = input("Select an option.\n\n ")
  choice = choice.lower()
  if choice == "1":
    choice = True
    player("NBA")
  elif choice == "2":
    choice = True
    player("CBB")
  elif choice == "3":
    choice = True
    powerRank()
  elif choice == "3":
    choice = False
  else :
    print("\nPlease select a valid option\n")

  
    
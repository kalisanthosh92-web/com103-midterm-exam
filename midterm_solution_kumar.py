IGN = input("In Game Name (IGN): ")
Rank = input("Current Rank: ")
Hero = ['Layla','Tigreal','Gusion','Kagura','Chou']
roles =['Marksman','Tank','Assassin','Mage','Fighter']
  
print()
   


print('=' * 50)
print(f'{'MOBILE LEGENDS --HERO ROSTER':^50}')
print('='*50)
for i in range(1,6):
    print(f'    {i}.  {Hero[i-1]:<20}[{roles[i-1]}] ')
print('='*50)
print()

matches = []
matches_played = 0
wins = 0
loss = 0
best_played = 0 


for j in range(1,5):
    print()
    print(f'--- MATCH {j} ---')
    hero_number = int(input('Hero number (0 to skip): '))
    if hero_number == 0 or hero_number <1 or hero_number > 5 :
        continue
    else: 
        kills = int(input('Kills: '))
        Deaths = int(input('Deaths: '))
        Assists = int(input('Assists: '))
        Result = input('Result(W/L): ').lower()
        
        if Result == 'w':
            match_result = 'Win'
            wins += 1
        else :
            match_result = 'Loss'
            loss += 1 

        while Deaths == 0:
            KDA = (kills + Assists)/1 
        else : 
            KDA = (kills + Assists)/Deaths
            

        if KDA >= 5 and Result == 'w':
            tag = 'DOMINATION!'
        elif KDA >= 5 and Result == 'l':
            tag = "Carried Hard"
        elif KDA < 5 and Result == 'w':
            tag = 'Team Effort'
        elif KDA < 5 and Result == 'l':
            tag = 'Better Luck Next Game'
        matches_played += 1

        


        each_match = [matches_played,Hero[hero_number-1],KDA,match_result,tag]
        matches.insert(matches_played,each_match)

        if KDA > best_played:
            best_played = KDA



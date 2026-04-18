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
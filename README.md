so basically this program first asks the USER to input the "INU" (In Game Name ), and the Rank.

then it prints a table titled "MOBILE LEGENDS --HERO ROSTER" and displys the index,Name & Role of the heros in a clear tabular form.

The it asks the user for hero number (1–5). 
If the hero number is valid (1–5), ask for kills, deaths, assists, and match result (W for win, L for loss) 
for 4 match entries.

IT also counts the match.and doesnt count if its skipped.

If the user types 0 or invalid input, that match slot is skipped (no stats recorded).

it saves the details of each match played in  a 2D list for later use.



then it Computes the KDA per match: KDA = (kills + assists) / deaths. If deaths is 0, use 1 as the denominator.

Then it Assigns a performance tag based on KDA and result: KDA ≥ 5 and W → 'DOMINATION!'; KDA ≥ 5 and L → 'Carried Hard'; KDA < 5 and W → 'Team Effort'; KDA < 5 and L → 'Better Luck Next Game'.

After all entries: it counts wins and losses among logged matches, computes win rate as a whole-number percentage (wins / matches_played × 100)

ANd it also identifies the match with the highest KDA as the Best Match.


then it prints a formatted match log table showing: IGN, rank, each logged match (sequential number, hero, KDA, result, tag), win/loss record, win rate, and best match label


event = input('What happened today?')

daily_journal = open('daily_journal.txt', 'w')

daily_journal.write(event)

daily_journal.close()

print('Journal Saved!')
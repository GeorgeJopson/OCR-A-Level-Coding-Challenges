classificationTree=['Is it domesticated? [y/n]',['Is it a farm animal? [y/n]',['Is it taller than 1m? [y/n]',['Do you ride it? [y/n]','Horse','Cow'],['Do you get wool from it? [y/n]','Sheep','Pig']],['Is it feline? [y/n]','Cat','Dog']],['Can it swim? [y/n]',['Does it have tentacles? [y/n]',['Does it live in dens on the sea floor? [y/n]','Octupus','Squid'],['Does it live only in the sea? [y/n]',['Is it a mammal? [y/n]','Dolphin','Whale'],['Does it have feathers? [y/n]','Penguin','Seal']]],['Is it a bug? [y/n]',['Can all of the species fly? [y/n]',['Can it produce honey? [y/n]','Bee','Wasp'],['Can it build webs? [y/n]','Spider',['Do they have eyes? [y/n]','Ant','Termite']]],['Is it a feline? [y/n]',['Does it have stripes? [y/n]','Tiger','Lion'],['Can it fly? [y/n]','Sparrow','Ostrich']]]]]
currentSection=classificationTree.copy()
while True:
    userInput= input(currentSection[0])
    if userInput=='y':
        currentSection=currentSection[1]
    else:
        currentSection=currentSection[2]
    if type(currentSection)==str:
        print(currentSection)
        break

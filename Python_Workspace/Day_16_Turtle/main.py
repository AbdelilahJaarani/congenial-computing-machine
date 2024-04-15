

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Shiggy","Glumanda"])
table.add_column("Type",["Electric","Water","Fire"]) 
#hier handelt es sich um ein Attribute welches einen Eigenschaft hat,
#die kann man verändern in dem man das Attribute umschreibt in den eigenschaften 
#die gespeichert sind.
table.align = "l"
print(table)
from rich import print # this module helps to print the data in a more readable format
from rich.console import Console
from rich.theme import Theme
from rich.traceback import install # this module helps to print the traceback in a more readable format


shrek_info = {
  "title": "Shrek",
  "release_year": 2001,
  "genre": ["Animation", "Adventure", "Comedy"],
  "director": "Andrew Adamson, Vicky Jenson",
  "producers": ["Jeffrey Katzenberg", "John H. Williams", "Aron Warner"],
  "writers": ["William Steig (book)", "Ted Elliott", "Terry Rossio", "Joe Stillman", "Roger S.H. Schulman"],
  "voice_cast": {
    "Shrek": "Mike Myers",
    "Donkey": "Eddie Murphy",
    "Princess Fiona": "Cameron Diaz",
    "Lord Farquaad": "John Lithgow"
  },
  "plot_summary": "A mean lord exiles fairytale creatures to the swamp of a grumpy ogre, who must go on a quest and rescue a princess for the lord in order to get his land back.",
  "box_office": {
    "budget": "$60 million",
    "gross_usa": "$267.7 million",
    "cumulative_worldwide_gross": "$484.4 million"
  },
  "awards": [
    "Academy Award for Best Animated Feature",
    "BAFTA Award for Best Adapted Screenplay",
    "MTV Movie Award for Best Villain (John Lithgow)"
  ],
  "sequels": [
    "Shrek 2 (2004)",
    "Shrek the Third (2007)",
    "Shrek Forever After (2010)"
  ]
}

print(shrek_info) # more readable than the default print function

install() # this will install the rich traceback handler

custom_theme = Theme({
  "info": "bold blue",
  "warning": "bold yellow",
  "danger": "bold red"
})

console = Console(theme=custom_theme)

def compare_numbers(a,b):
  console.log(log_locals=True)
  if a > b:
    console.print(f"{a} is greater than {b}", style="bold green")
  elif a < b:
    console.print(f"{a} is less than {b}", style="bold red")
  else:
    console.print(f"{a} is equal to {b}", style="bold blue")

compare_numbers(10, 5)
compare_numbers(5, 10)
compare_numbers(5, 5)

#compare_numbers(5, "0")
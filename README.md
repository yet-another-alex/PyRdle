# PyRdle
 A Python Tkinter GUI version of the game 'wordle'.  
 The popular word game ['Wordle'](https://www.powerlanguage.co.uk/wordle/) is lots of fun, so I thought *yeah, I can do that*.  
 This is not really a "best practice" code project or anything. Basically I had some spare minutes throughout the day and had fun rebuilding the game.
 
 ## How it works
 
 It works exactly like Wordle. Run *main.py* and the GUI will open:
 
 ![empty PyRdle GUI](https://raw.githubusercontent.com/yet-another-alex/PyRdle/main/screens/screen1.png)
 
 Then you can start typing.  
 **RETURN/ENTER** will process the input. The text at the bottom will show if a word is invalid.
 **BACKSPACE** will delete an entered letter. There is some "not quite right"-stuff involved which sometimes causes backspace to do weird stuff.
 **RESET** is a button to reset the entire game. A *new* word will be chosen.
 
 ## Guessing?
 
 Simply type a word and hit *return*:
 
 ![a cruel guess](https://raw.githubusercontent.com/yet-another-alex/PyRdle/main/screens/screen2.png)
 
 If you guessed correctly, you'll win:
 
 ![a won game](https://raw.githubusercontent.com/yet-another-alex/PyRdle/main/screens/screen3.png)
 
 If you run out of guesses, the word will appear at the bottom:
 
 ![a lost game](https://raw.githubusercontent.com/yet-another-alex/PyRdle/main/screens/screen4.png)
 
 If you won or lost, you can click *reset* and a new game starts!

## What about Umlauts?

ÄÖÜ are supported. Pretty much everything should be supported. If you use a different wordlist and something doesn't work, let me know and I'll see if I can fix it.

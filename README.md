# deutsch-book-vocab-generator
Want to learn German vocabulary specific to a certain book or article? This project takes a German word corpus (e.g., Faust) of one's choosing, and uses it to generate a corresponding German-English vocabulary list. The vocabulary list can then be easily imported as a flashcard deck to study apps such as Anki.



## PROJECT STATUS
WORK IN PROGRESS

To initiate this project, open gutenberg_vocab_generator.ipynb. 



## PROJECT INPUT
The variables described below are available to edit in the gutenberg_vocab_generator.ipynb file.


### response:
Replace the current url with your chosen url.
Given the current BeautifulSoup setup, the url must be from a German book at ProjectGutenberg.com.  When obtaining the url, sure to select .html as the book's format.
(E.g., Faust: https://www.gutenberg.org/cache/epub/2229/pg2229-images.html)


### file_name_txt and file_name_csv:
Replace the current file names with file names of your choice.


### stop_words:
Add stop words to the existing list as needed.  Stop words will be excluded from the final word list.




## PROJECT OUTPUT

A unique list of German words (and their english counterparts) in .txt and .csv file format.
Note: The .csv file is currently formatted to match the import requirements for the Anki flashcard app.



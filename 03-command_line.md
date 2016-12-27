# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls` lists contents of directory
`ls -a`   list all contents of directory including those beginning with '.'
`ls -l`   list in long format
`ls -lh`  list in long format with unit suffixes
`ls -lah` list in all in long format with unit suffixes
`ls -t`   list contents in directory sorted by most recently modified
`ls -Glp` list contents colorized by type and have sub-directory names trail with '/'

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

 1. -G colorize - helps with distinguishing content types
 2. -p sort by most recent time modified - always an important tool
 3. -1 list out with new lines - makes contents easier to read
 4. -R list out contents Recursively - efficient way of viewing everything in sub-directories
 5. -r reverse order of alphabetical sort- another way to sort and sorting is a powerful tool

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs allows you to pass multiple commands. For example, I can use ls *.txt | xargs cat to stream all files in a directory.

 


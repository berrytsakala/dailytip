# dailytip
A humane alternative to the monstrous fortune-cookie*: prints at login a random line from a text file

## Raison d'être:
Fortune cookie requires a compiler(!) and manually doing funny stuff to make it work. And even after doing everything it didn't work! and the documentation is hard-to get. Seriously?

## Usage:
Just bring your text file, one sentence per line,
and add command in your shell rc file (e.g. .bashrc)

## Notes:
This process is not the most efficient: it'll load all the lines and choose a random one. for files under 10mb, in modern desktops, it goes unnoticed.

## Todo:
 - Predefined line separator symbols support
 - user-defined line separators via command line 
 

* pun intended

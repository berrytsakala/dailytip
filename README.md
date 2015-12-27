# dailytip
A humane alternative to the monstrous fortune-cookie*: prints at login a random line from a text file

## Raison d'être:
Fortune cookie's files are too complicated to edit!

## Install
 1. copy dailytip.py to your $PATH, e.g. /usr/local/bin
 1. chmod a+x /usr/local/bin/dailytip.py
 1. copy .dailytiprc to your $HOME
 1. put a text file, (line delimited), in $HOME/.dailytip.txt   (configurable via .dailytiprc)
 1. add to your shell's rc file (e.g. .bashrc) the command "dailytip.py"

## Usage:
Just bring your text file, one sentence per line,
and add command in your shell rc file (e.g. .bashrc)

## Notes:
This process is not the most efficient: it'll load all the lines and choose a random one. for files under 10mb, in modern desktops, it goes unnoticed.

## Todo:
 - Predefined line separator symbols support
 - user-defined line separators via command line 
 

_* pun intended

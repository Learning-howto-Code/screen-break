# screen-break
A friendly little app that reminds you to take a break every hour.

Built with TKinter and Python Screen Break opens a pop up window every hour with a firendly remidner to take a break, a recomendation for what to do and a streak counter.
Works on Mac, Windows and Linux, but only tested on Mac(for now)

<img width="495" height="326" alt="Screen Shot 2025-08-07 at 1 41 21 PM" src="https://github.com/user-attachments/assets/55ecb5ce-05b4-461e-bcd9-1d4fcb75d7ad" />

## FAQ
how do I set it up, look below
how can I edit the activity list?   Just add or delete the lines from ideas.txt
how do I reset/edit my streak?  your streak is the number in counter.txt

## How to set up
Mac
open terminal
type crontab -e
0 * * * * "put path to python here" "put path to folder here", like this: 0 * * * *  /Library/Frameworks/Python.framework/Versions/3.12/bin/python3 /Users/jakehopkins/Downloads/screen_break 
one you paste that type :qa to exit vim and save
let it run!


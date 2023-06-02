# TinyTeleProjects
Just a basic telegram bot for now, Gives all whois dates for specified website.

DISCLAIMER: USE AT YOUR OWN RISK THIS IS MY FIRST BOT FOR TELEGRAM.
DON'T LEAVE YOUR BOT TOKEN EXPOSED, MOVE THE BOT TOKEN TO AN ENV FILE IF YOU PLAN ON USING THIS CODE ON ANY APPLICATION THAT LEAVES THE CODE VISIBLE TO OTHERS.

DEPENDENCIES:python-telegram-bot 12.8,python-whois 0.8.0, and telegram. 

INSTALL PROCESS:
1. Install python-telegram-bot 12.8,python-whois 0.8.0, and telegram (I used pip install for the first 2)
2. use the botfather bot on telegram to recieve a bot token
3. REPLACEWITHBOTTOKEN on line 40 should be replaced with your bot token, An env file will replace this soon for safety reasons.
4. Once all of the libraries are installed and the token is plugged run the .py
5. Use the command /start on a telegram chat with your bot, then you can send it a link and it will give you the whois dates.

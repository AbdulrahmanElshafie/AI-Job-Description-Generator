# AI-Job-Description-Generator
Ever seen HR having lots of trouble creating many job descriptions?
This automation is a solution for this issue. It uses ChatGPT through poe.com to create many job descriptions in a few minutes.

All you have to do is:
1.  Create account on poe.com
2.  Add the positions you need in positions.txt file
3.  Run the app
4.  Enter company's name, industry in the GUI, and any additional info or requirements you need
5.  Watch the magic happens!!

**NOTE:**
You may need to update the selectors as the webiste of poe.com may update it later.

Code Explanation:
I used Selenium, an automation and testing library for web applications and can be used for web scraping too.

The first task is to login to the website which should be done manually as the website detects bots and this can't be avoided unless you login manually (login function).
Then it takes the positions and send each one of them to the bot by filling the txt box and clicking send button, then waits for the message to be completed (prompt and send prompt functions). 
The waiting function is done through checking send button state, if its disabled then it assumes that the message has been completed, if not it waits (waiting function). 
After message completion, it takes the description generated and save it to a csv file as title column and description column. 

This process will be repeated untill all positions in the file is finished. 

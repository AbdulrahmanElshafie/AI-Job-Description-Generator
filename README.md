# AI-Job-Description-Generator
Have you ever seen HR having lots of trouble creating many job descriptions?
This automation is a solution for this issue. It uses ChatGPT through poe.com to create many job descriptions in a few minutes.

All you have to do is:
1.  Create an account on poe.com
2.  Add the positions you need in the positions.txt file
3.  Run the app
4.  Enter the company's name, industry in the GUI, and any additional info or requirements you need
5.  Watch the magic happen!!

**NOTE:**
You may need to update the selectors as the website of poe.com may update it later.

Code Explanation:
I used Selenium, an automation and testing library for web applications that can be used for web scraping too.

The first task is to log in to the website which should be done manually as the website detects bots and this can't be avoided unless you log in manually (login function).

Then it takes the positions and sends each of them to the bot by filling the text box and clicking the send button, then waits for the message to be completed (prompt and send prompt functions).

The waiting function is done by checking the send button state, if it's disabled then it assumes that the message has been completed, if not it waits (waiting function). 

After message completion, it takes the description generated and saves it to a CSV file as a title column and description column. 

This process will be repeated until all positions in the file are finished. 

Background:

People can invest in mutual funds that hold many stocks and bonds. Funds list what they own every quarter, so investors can get a sense of what they are actually exposed to, e.g. a "21st Century Tactical Technology Fund" does not just own 50% AAPL and 50% GOOG. Fund holdings are listed on the SEC website, EDGAR.

Challenge:

Write code in Python that parses fund holdings pulled from EDGAR, given a ticker or CIK, and generates a .tsv file from them. 

Example:

For this example, we will use this CIK: 0001166559
Start on this page: http://www.sec.gov/edgar/searchedgar/companysearch.html
Enter in the CIK (or ticker), and it will take you here.
Find the “13F” report documents from the ones listed. Here is a “13F-HR”.
Parse and generate tab-delimited text from the xml
Write the text to a file
Goals:

Your code should be able to use any mutual fund ticker. Try morningstar.com or lipperweb.com to find valid tickers.
Assume you need to fetch only the most recent report, but consider how you could get previous ones.
Be sure to check multiple tickers, since the format of the 13F reports can differ.
Let us know your thoughts on how to deal with different formats.  
Additional Instructions:
Please keep all code and other project files in a directory labeled with your full name. Submit this directory as a zip (or rar, 7z, tar, etc.) file. You are free to use any easily available Python library; please use what you think is appropriate and are comfortable with. If you choose to use an IPython Notebook, please also submit proper .py files with the code. 

Lastly, we’re not looking for perfection. We want you to have fun coding and show us your skills.  Please return in the next couple days, and feel free to reach out if you have any questions!

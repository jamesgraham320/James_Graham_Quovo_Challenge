# James Graham - Quovo Submission

## Instructions
1. Install package dependencies with command:
	`pip install -r requirements.txt`
2. Navigate to folder `./quovoCrawler/`
3. run command: `scrapy crawl holdings_spider`
4. View output data in file `sec-data.tsv` in same directory

Code I have written is in the directory `./quovoCrawler/quovoCrawler/spiders/holdings_spider.py`

## Personal Thoughts
This was my first time using the Scrapy library. Usually I do most work in Javascript but after this I don't think I will ever do web scraping in JS again. I enjoyed the challenge and the opportunity to use a new library. There's a lot of room for extensibility and customization. You can input any ticker and can change the target download file very easily. I was also unfamiliar with XPATH but it's far more efficient for navigating web pages with relative paths as oppsed to hard coded HTML tag names. 

The script can adapt to different formats of data because the XML data is parsed generically using tag names as column headers. This script only searches for documents titled "13F-HR" but can be adapted with regex to find any files titled "13F." The script already finds all "13F-HR" documents but only follows through crawling the first one. To retrieve more than the last few documents would require the crawler to travel through the pagination. If more "13F" documents had very different formats you can crawl all of them and generate a master list of column headers before going through the data again and mapping it to said headers.

Mutual fund holding data like this could be used in a number of ways including watching and updating a master list of what top mutual funds are holding. As reports update, you would be able to see when targets change their holdings and what they're buying. You could also use the data to build a picture of which companies have majority holdings.

## Assignment Details
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

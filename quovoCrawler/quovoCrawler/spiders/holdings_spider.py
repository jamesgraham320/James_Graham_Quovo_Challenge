#Using Scrapy package for web page crawling
import scrapy
from bs4 import BeautifulSoup

class HoldingsSpider(scrapy.Spider):
    name = "holdings_spider"
    start_urls = [
        "https://www.sec.gov/cgi-bin/browse-edgar?CIK=0001166559&Find=Search&owner=exclude&action=getcompany"
    ]

    def parse(self, response):

        # Find link to next page next to table data that contains text "13F-HR"
        # Replace text with regex to search for 13F
        url = response.xpath("//tr[td='13F-HR']/td/following-sibling::td/a/@href").get()
        yield { 'first response url to follow':  url }

        yield response.follow(url, callback=self.parse_documents_page)


    def parse_documents_page(self, response):

        # Find link next to text "INFORMATION TABLE"
        # Substitute to "INFORMATION TABLE" to get download links to other pages
        url = response.xpath("//tr[td='INFORMATION TABLE']/td/following-sibling::td/a/@href").getall()[1]
        yield response.follow(url, callback=self.parse_sec_data)


    def parse_sec_data(self, response):

        #parse response body into beautifulsoup for easier handling
        soup = BeautifulSoup(response.body, "xml")

        # each infoTable tag is a data "row"
        info_tables = soup.findAll("infoTable")
        
        filename = "sec_data.tsv"
        with open (filename, 'w') as f:

            # Find nested tag names to act as headers in TSV file
            for tag in info_tables[0].findChildren():
                f.write(tag.name + "\t")
            f.write("\n")

            for info_table in info_tables:
                
                # Iterate through data row children and append data or placeholder if no data
                # Accounts for different formats of data
                for tag in info_table.findChildren():
                    if hasattr(tag, "content") and tag.string != None:
                        f.write(tag.string + "\t")
                    elif tag.name != None:
                        f.write("N/A\t")
                f.write("\n")


            # Original attempt to hard code column titles and column data
            # f.write("N/A\tN/A\tN/A\tValue\tSHRS OR\tSH/\tPUT/\tINVESTMENT\tOTHER\tVOTING AUTHORITY\n")
            # f.write("NAME OF ISSUER\tTITLE OF CLASS\tCUSIP\t(x$1000)\tPRN AMT\tPRN\tCALL\tDISCRETION\tMANAGER\tSOLE\tSHARED\tNONE\n")
            # f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
                # info_table.nameOfIssuer.string,
                # info_table.titleOfClass.string,
                # info_table.cusip.string,
                # info_table.value.string,
                # info_table.shrsOrPrnAmt.sshPrnamt.string,
                # info_table.shrsOrPrnAmt.sshPrnamtType.string,
                # "N/A",
                # info_table.investmentDiscretion.string,
                # "N/A",
                # info_table.votingAuthority.Sole.string,
                # info_table.votingAuthority.Shared.string,
                # 0,
                # ))


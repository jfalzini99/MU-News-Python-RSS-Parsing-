# MU-News-Python-RSS-Parsing-

A Python script which generates an RSS feed XML file from the first two pages of articles at the MU news site (https://www.monmouth.edu/news/archives and https://www.monmouth.edu/news/archives/page/2/). 


- Retrieves the news pages using the requests module and then parse  the individual headlines as well as the corresponding links to be included in the output XML file.
- Uses the PyRSSGen module to format the RSS XML File


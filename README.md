# scrapy-evasion
## Description
This repository contains scrapy project preconfigured for blocking-mechanism evasion. Sometimes websites block scrapers undeservingly, and I tried to solve this problem.
>Remember to crawl responsibly and not cause DoS!

## Requirements
* Scrapy (http://scrapy.org/)
* Stem (https://stem.torproject.org/)
* TOR (https://www.torproject.org/)
* Privoxy (https://www.privoxy.org/) or another http-to-socks proxy

## Installation
First, create the **torrc** file in TOR folder. This file should contain following string:
`ControlPort 9051`
After that, start TOR instance that will use this **torrc** file. On Windows, command will look like `tor.exe -f torrc`
Then start Privoxy.
Now you can create your spiders and run them through TOR network with User-Agent rotation.
## Configuration
### Handle HTTP codes
In spider class, add an array containing status codes. When crawler receives one of them, it will change TOR exit node.
## Output
In **pipelines.py** file configure _CsvExporterPipeline_ class to change the output.

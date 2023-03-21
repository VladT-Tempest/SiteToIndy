# SiteToIndy

This is a task completed inside a Job Testing. The challenge established the following:


Developer Trial Task - Copy ClassCentral Pages and Translate to Hindi 

• Scrape pages one level deep using HT Track, your custom script, or another app. 

• Use Google Translate to Translate the text inside the HTML to Hindi. The hindi will be hard-coded into the page.

• Upload to a webserver. 

• Make sure all the javascript/gSetc. is loading correctly.

• In your trial task form submission:

 	• Include a URL to the live website on your server so we can see that successfully copied it.
    
 	• Let me know how you scraped the pages. Did you use httrack, another piece of software. or a script you wrote your self? 


To complete the task I cannot use HTTrack as the site has scraping protection. So with GhatGPT help I used wget with the command line:

wget -mkxKE -r -w 1 --level=1 --convert-links --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"  https://www.classcentral.com/

With wget I could bypass the scrapping protection and get the raw files locally. Next step use Python program to translate all the visible text in all HTML files of a directory. This is the siteToHindi.py.

and finally site translated was deployed yo (ClassCentral)[https://github.com/VladT-Tempest/classcentral]



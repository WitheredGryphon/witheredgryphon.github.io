#!/usr/bin/python

#This is about to get real long

HTML_16x9 = [
"<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'><meta http-equiv='X-UA-Compatible' content='IE=edge'><meta name='viewport' content='width=device-width, initial-scale=1'><title>",
"</title><!-- Bootstrap core CSS --><link href='css/bootstrap.min.css' rel='stylesheet'><!-- Custom CSS -->",
"<!-- Flickity --><link rel='stylesheet' href='css/flickity.css' media='screen'><link href='css/docs.css' rel='stylesheet'><link href='css/flag-icon.min.css' rel='stylesheet'><link rel='manifest' href='manifest.json'><link rel='apple-touch-icon' sizes='180x180' href='images/apple-touch-icon.png'><link rel='icon' type='image/png' sizes='32x32' href='images/favicon-32x32.png'><link rel='icon' type='image/png' sizes='16x16' href='images/favicon-16x16.png'><link rel='manifest' href='images/site.webmanifest'><link rel='mask-icon' href='images/safari-pinned-tab.svg' color='#4d4dff'><link rel='shortcut icon' href='images/favicon.ico'><meta name='msapplication-TileColor' content='#4d4dff'><meta name='msapplication-config' content='images/browserconfig.xml'><meta name='theme-color' content='#4d4dff'></head><body><nav class='mobileNav navbar navbar-default navbar-fixed-top'><div class='container-fluid'><div class='navbar-header'><a href='index.html'><span class='navbar-brand glyphicon glyphicon-home' style='cursor:pointer'></span></a><span class='navbar-brand webNav' style='pointer-events: none; float: right; text-align: right; padding-top: 16px;'>/r/vn's 2018 Recommendations</span><span class='navbar-brand mobileNav' style='pointer-events: none; float: right; text-align: right; padding-top: 16px;'>/r/vn's 2018 Chart</span></div></div></nav><nav class='webNav navbar navbar-default'><div class='container-fluid'><div class='navbar-header'><a href='index.html'><span class='navbar-brand glyphicon glyphicon-home' style='cursor:pointer'></span></a><span class='navbar-brand webNav' style='pointer-events: none; float: right; text-align: right; padding-top: 16px;'>/r/vn's 2018 Recommendations</span><span class='navbar-brand mobileNav' style='pointer-events: none; float: right; text-align: right; padding-top: 16px;'>/r/vn's 2018 Chart</span></div></div></nav><div class='contentWrapper'><div class='topWrapper'><div class = 'container-fluid'><div class='row valign' style = 'margin-right: 0;'><div class='col-sm-7' style='padding-right: 0; padding-left: 16px; padding-top: 8px;' align='center'><div class='carousel carousel-main js-flickity' data-flickity='{ \"pageDots\": false, \"fullscreen\": true, \"imagesLoaded\": true }'>",
"</div><div class='carousel carousel-nav js-flickity' data-flickity='{ \"asNavFor\": \".carousel-main\", \"contain\": true, \"pageDots\": false, \"imagesLoaded\": true }'>",
"</div></div><div class='col-sm-5' style='margin-left: 16px;'><div class='novelTitle'>",
"</div><div class='row' style='margin-left: 0; padding-left: 0;'><div class='col-xs-5' style='padding-left: 0; margin-right: 4px;'><div class='infoTag'>Release Date:</div></div><div class='col-xs-6' style='margin-left: 0; padding-left: 0;'><div class='novelReleaseDate'>",
"</div></div></div><br /><div class='row' style='margin-left: 0; padding-left: 0;'><div class='row' style='margin-left: 0; padding-left: 0;'><div class='col-xs-5' style='padding-left: 0;'><div class='infoTag'>Developer:</div></div><div class='col-sm-6' style='padding-left: 0;'><div class='novelDeveloper'><a href='",
"' rel='noopener' target='_blank'>",
"</a></div></div></div><div class='row' style='margin-left: 0; padding-left: 0;'><div class='col-xs-5' style='padding-left: 0;'><div class='infoTag'>",
"</div></div><div class='col-sm-5' style='padding-left: 0;'><div class='novelPublisher'><a href='",
"' rel='noopener' target='_blank'>",
"</a></div></div></div></div><br /><div class='row' style='margin-left: 0; padding-left: 0;'><div class='col-xs-5' style='padding-left: 0; margin-right: 8px;'><div class='infoTag'>Genres:</div></div><div class='col-xs-5' style='margin-left: 0; padding-left: 0;'><div class='novelReleaseDate'>",
"</div></div></div><br /><div class='row' style='margin-left: 0; padding-left: 0;'><div class='col-xs-5' style='padding-left: 0; margin-right: 8px;'><div class='infoTag'><a data-toggle='tooltip' title='Includes all regions that a fully translated patch was released, regardless of platform.' style='border-bottom: 1px dotted #787878; color: #e1e5e8; text-decoration: none;'>Regions Available:</a></div></div><div class='col-xs-4' style='margin-left: 0; padding-left: 0;'><div class='novelRegions'>",
"</div></div></div><br/><div class='row' style='margin-left: 0; padding-left: 0;'><div class='col-xs-5' style='padding-left: 0; margin-right: 8px;'><div class='infoTag'>Novel Length:</div></div><div class='col-sm-6' style='margin-left: 0; padding-left: 0;'><div class='novelLength'><a data-toggle='tooltip' title='Based on all play styles from HowLongToBeat.' style='border-bottom: 1px dotted #8989ff; text-decoration: none;'>",
"</a></div></div></div><br /><div class='row' style='margin-left: 0; padding-left: 0;'><div class='col-xs-5' style='padding-left: 0; margin-right: 8px;'><div class='infoTag'>Anime Adaptation:</div></div><div class='col-xs-6' style='padding-left: 0; padding-right: 0; margin-right: 8px;'><div class='novelAdaptation'>",
"</div></div></div><br /><div class='row' style='margin-left: 0; padding-left: 0;'><div class='col-xs-5' style='padding-left: 0; margin-right: 8px;'><div class='infoTag'>Prequel:</div></div><div class='novelAdaptation'>",
"</div></div><div class='row' style='margin-left: 0; padding-left: 0;'><div class='col-xs-5' style='padding-left: 0; margin-right: 8px;'><div class='infoTag'>Sequel:</div></div><div class='novelAdaptation'>",
"</div></div><br /><div class='row' style='margin-left: 0; padding-left: 0; max-width: 90%'><div class='col-xs-7' style='padding-left: 0;'>",
"</div></div></div></div></div></div><div class='midWrapper'><div class='container-fluid'><div class='col-lg-8'><div class='row'><!-- Make sure you change the color in the CSS file for 'contentWarningWeb' and 'contentWarningMobile' --><div class='contentWarningMobile'>",
"<span style='margin-left: 8px; text-align: center;'>",
"</span></div><div class='contentWarningWeb'>",
"</span></div></div><br /><div class='row'><div class='sectionHead'>Reviews</div></div><br /><div class='row'>",
"</div><div class='row'>",
"</div><br /><div class='row'>",
"</div><div class='row'>",
"</div><br /><div class='row'>",
"</div><div class='row'>",
"</div><br /><div class='row'><div class='sectionHead'>About This Novel</div></div><br /><div class='row'>",
"<br /><div class='row'>(From VNDB)</div><br /><div class='row'><div class='sectionHead'>Technical Details</div></div><br /><div class='row' style='border-bottom: 1px dashed #4d4dff50'><div class='col-xs-3' style='margin-left: 0; padding-left: 0; padding-bottom: 4px;'><span style='color: #8989ff'>Platforms: </span></div><div class='col-xs-9' style='margin-left: 0; padding-right: 0; text-align: right;'>",
"</div></div><div class='row' style='border-bottom: 1px dashed #4d4dff50'><div class='col-xs-3' style='margin-left: 0; padding-left: 0; padding-bottom: 4px; padding-top: 4px;'><span style='color: #8989ff'>Resolution: </span></div><div class='col-xs-9' style='margin-left: 0; padding-right: 0; text-align: right; padding-bottom: 4px; padding-top: 4px;'>",
"</div></div><div class='row' style='border-bottom: 1px dashed #4d4dff50'><div class='col-xs-3' style='margin-left: 0; padding-left: 0; padding-bottom: 4px; padding-top: 4px;'><span style='color: #8989ff'>English:</span></div><div class='col-xs-9' style='margin-left: 0; padding-right: 0; text-align: right; padding-bottom: 4px; padding-top: 4px;'>",
"</div></div><div class='row' style='border-bottom: 1px dashed #4d4dff50'><div class='col-xs-3' style='margin-left: 0; padding-left: 0; padding-bottom: 4px; padding-top: 4px;'><span style='color: #8989ff'>Animated Scenes: </span></div><div class='col-xs-9' style='margin-left: 0; padding-right: 0; text-align: right; padding-bottom: 4px; padding-top: 4px;'>",
"</div></div><div class='row' style='border-bottom: 1px dashed #4d4dff50'><div class='col-xs-3' style='margin-left: 0; padding-left: 0; padding-bottom: 4px; padding-top: 4px;'><span style='color: #8989ff'>Voiced: </span></div><div class='col-xs-9' style='margin-left: 0; padding-right: 0; text-align: right; padding-bottom: 4px; padding-top: 4px;'>",
"</div></div></div><div class='col-lg-3' id='webBar' style='float: right;'><div class='reccNovelsContainer'><div class='row'><div class='similarNovelsHead'>You Might Also Like</div></div><br /><div class='row'><div class='bannerThumb'>",
"</div></div><br /><div class='row'><div class='bannerThumb'>",
"</div></div><br /><div class='row'><div class='bannerThumb'>",
"</div></div><br /></div><div class='row'><div class='linksHead'>Get It Now</div></div><br />",
"</div><br /><div class='row' id='mobileBar'><div class='col-xs-5'><div class = 'row'><div class='similarNovelsHead'>Recommended</div></div><br /><div class='row'><div class='bannerThumb'>",
"</div></div><br /><div class='row'><div class='bannerThumb'>",
"</div></div><br /><div class='row'><div class='bannerThumb'>",
"</div></div></div><div class='col-xs-5 pull-right'><div class = 'row'><div class='linksHead'>Get It</div></div><br />",
"</div></div></div></div></div><!-- jQuery (necessary for Bootstrap's JavaScript plugins) --><script src='js/jquery-3.3.1.min.js'></script><!-- Include all compiled plugins (below), or include individual files as needed --><script src='js/bootstrap.min.js'></script><script src='js/flickity.pkgd.min.js'></script><!-- Lazy Loader --><script src='js/lazysizes.min.js'></script><script src='js/ls.unveilhooks.min.js'></script><script>$(document).ready(function(){$('.carousel-main').flickity();$('.carousel-nav').flickity({asNavFor: '.carousel-main',contain: true,pageDots: false});$('[data-toggle=\"tooltip\"]').tooltip();});</script></body></html>"
]

finalHTML = []

#Novel's title
title = input("Enter the novel's title: \n")
finalHTML.append(HTML_16x9[0])
finalHTML.append(title)

#Just the novel title again, mostly here for customization options
cssTitle = input("\n\nEnter the CSS Title (This is usually just the novel title again with no spaces): \n")
finalHTML.append(HTML_16x9[1])
finalHTML.append(cssTitle)

#Typically just the novel title but lowercase
imageTitle = input("\n\nEnter the title for images\n(Usually the novel title but lowercase): \n")
finalHTML.append(HTML_16x9[2])
for i in range(8):
	finalHTML.append(imageTitle)
	
finalHTML.append(HTML_16x9[3])
for i in range(8):
	finalHTML.append(imageTitle)

#Release date, self-explanatory, NEEDS TO BE (MONTH DAY, YEAR) FORMAT, e.g. January 1, 2000
release = input("\n\nEnter the release date\nFormat is MONTH DAY, YEAR (e.g. January 1, 2000): \n")
finalHTML.append(HTML_16x9[4])
finalHTML.append(release)

#Direct link to developer's URL, if one isn't available use a Twitter page or something THIS IS NOT THE PUBLISHER
developerURL = input("\n\nEnter the developer's URL: \n")
finalHTML.append(HTML_16x9[5])
finalHTML.append(developerURL)

#Novel developer
developer = input("\n\nEnter the name of the developer: \n")
finalHTML.append(HTML_16x9[6])
finalHTML.append(developer)

#Either the novel had a publisher or a fan translator
translatorFlag = input("\n\nDid a fan translator do this project? N = Publisher did it (Y / N): \n")
if translatorFlag == "N" or translatorFlag == "No":
	publisherURL = input("\n\nEnter the publisher's URL: \n")
	finalHTML.append(HTML_16x9[7])
	finalHTML.append(publisherURL)
else:
	translatorURL = input("\n\nEnter the translator's URL: \n")
	finalHTML.append(HTML_16x9[7])
	finalHTML.append(translatorURL)

#See above
if translatorFlag == "N" or translatorFlag == "No":
	publisher = input("\n\nEnter the publisher's name: \n")
	finalHTML.append(HTML_16x9[8])
	finalHTML.append(publisher)
else:
	translator = input("\n\nEnter the translator's name: \n")
	finalHTML.append(HTML_16x9[8])
	finalHTML.append(translator)

#PUT THE THREE GENRES LISTED ON THE FRONT PAGE FOR THE NOVEL
#These should be comma delimited as such: "Comedy, Romance, Drama"
#No quotes
genres = input("\n\nEnter the three genres on the front page for the novel: \n")
finalHTML.append(HTML_16x9[9])
finalHTML.append(genres)

#Enter the number of flags
#Then enter the ISO code associated
#Look it up if you don't know it, if you don't you'll screw it up
#It's two letters (Popular ones are: GB for English, CN for Chinese, JP for Japanese, ES for Spanish, FR for French, IT for Italian, RU for Russian)
flagsNum = int(input("\n\nEnter the number of flags (languages with full translations): \n"))
flags = []
while flagsNum > 0:
	f = input("\n\nEnter the ISO flag code (it's two letters): \n")
	flags.append(f)
	flagsNum = flagsNum - 1
finalHTML.append(HTML_16x9[9])
finalHTML.append(flags)

#Get it from HowLongToBeat, otherwise pull from VNDB
lengthHLTB = input("\n\nEnter time to beat from HLTB, leave blank and press Enter if none: \n")
lengthVNDB = ""
if lengthHLTB != "":
	finalHTML.append(HTML_16x9[10])
	finalHTML.append(lengthHLTB)
else:
	lengthVNDB = input("\n\nEnter time length from VNDB: \n")
	finalHTML.append(HTML_16x9[10])
	finalHTML.append(lengthVNDB)

#Anime adaptations, put how many then put the URL
adaptationsNum = int(input("\n\nEnter the number of adaptations: \n"))
adaptations = []
while adaptationsNum > 0:
	adapURL = input("\n\nEnter the adaptation URL: \n")
	adapName = input("\n\nEnter the adaptation Name: \n")
	adaptations.append( (adapURL, adapName) )
	adaptationsNum = adaptationsNum - 1
finalHTML.append(HTML_16x9[11])
finalHTML.append(adaptations)

#If there's a prequel and/or sequel list it
prequel = input("\n\nEnter the prequel if there is one, leave blank if not: \n")
sequel = input("\n\nEnter the sequel if there is one, leave blank if not: \n")
finalHTML.append(HTML_16x9[12])
finalHTML.append(prequel)
finalHTML.append(HTML_16x9[13])
finalHTML.append(sequel)

#Reddit and VNDB, post links
reddit = input("\n\nEnter the Reddit link if there is one, leave blank if not: \n")
vndb = input("\n\nEnter the VNDB link: \n")
finalHTML.append(HTML_16x9[14])
if reddit != "":
	finalHTML.append(reddit)
finalHTML.append(vndb)

#Age
#Valid inputs are:
#0 for all ages, 15, 17, 18
#Get the age rating from VNDB
#If there's a patch, put the link
age = input("\n\nEnter the age for the novel (found on VNDB): \n")
patch = input("\n\nEnter the adult patch link if there is one, leave blank if not: \n")
finalHTML.append(HTML_16x9[15])
finalHTML.append(age)
if patch != "":
	finalHTML.append(patch)

#Reviews
review1Text = input("\n\nEnter the first review text: \n")
review1URL = input("\n\nEnter the first review URL: \n")
review1Name = input("\n\nEnter the first review name: \n")
finalHTML.append(HTML_16x9[16])
finalHTML.append(review1Text)
finalHTML.append(HTML_16x9[17])
finalHTML.append(review1URL)
finalHTML.append(HTML_16x9[18])
finalHTML.append(review1Name)

review2Text = input("\n\nEnter the second review text: \n")
review2URL = input("\n\nEnter the second review URL: \n")
review2Name = input("\n\nEnter the second review name: \n")
finalHTML.append(review2Text)
finalHTML.append(review2URL)
finalHTML.append(review2Name)

review3Text = input("\n\nEnter the third review text: \n")
review3URL = input("\n\nEnter the third review URL: \n")
review3Name = input("\n\nEnter the third review name: \n")
finalHTML.append(review3Text)
finalHTML.append(review3URL)
finalHTML.append(review3Name)

#Novel's Description, try \n for new lines?
aboutText = input("\n\nEnter the novel's about text (found on VNDB or Steam): \n")
finalHTML.append(aboutText)

#Platforms available on in English (probably)
platforms = input("\n\nEnter the list of platforms it's available on: \n")
finalHTML.append(platforms)

#Resolution, either 16:9 or 4:3, pick one
resolution = input("\n\nEnter the resolution (16:9 or 4:3): \n")
finalHTML.append(resolution)

#If there's a patch, fill it in with the URL. Otherwise LEAVE IT BLANK
patch = input("\n\nEnter the English patch URL if there's a fully translated one, leave blank if not: \n")
if patch != "":
	finalHTML.append(patch)

#Animated scenes, either Full, Simple, or None
#Get it from VNDB, if it isn't listed then put None
animated = input("\n\nEnter if there's animated scenes (Full, Simple, None; found on VNDB): \n")
finalHTML.append(animated)

#Voiced, either Full, Partial, or None
#Get it from VNDB, if it isn't listed then put None
voiced = input("\n\nEnter if the novel is voiced (Full, Partial, None; found on VNDB): \n")
finalHTML.append(voiced)

#Recommendations
#Name and image name needed
#e.g.
#r1Name = Little Busters
#r1URL = lb (this will turn into images/lb_banner.jpg)
r1Name = input("\n\nEnter recommendation 1's name (Novel Title): \n")
r1URL = input("\n\nEnter recommendation 1's banner image name (lb for Little Busters): \n")
r2Name = input("\n\nEnter recommendation 2's name (Novel Title): \n")
r2URL = input("\n\nEnter recommendation 2's banner image name (lb for Little Busters): \n")
r3Name = input("\n\nEnter recommendation 3's name (Novel Title): \n")
r3URL = input("\n\nEnter recommendation 3's banner image name (lb for Little Busters): \n")
finalHTML.append(r1Name)
finalHTML.append(r1URL)
finalHTML.append(r2Name)
finalHTML.append(r2URL)
finalHTML.append(r3Name)
finalHTML.append(r3URL)

#Store Availability
#First the number of stores
#Then the name of the stores (Steam, MangaGamer, J-List, Amazon, Itch.io, etc. List of buttons is in the files, just search for "button")
#Then the link to the purchase site
#VNDB usually has these if you click the specific revision of the game and hit "Official Link"
storeNumber = int(input("\n\nEnter the number of stores the novel is sold from: \n"))
stores = []
while storeNumber > 0:
	sURL = input("\n\nEnter the store URL: \n")
	sName = input("\n\nEnter the store name: \n")
	stores.append( (sURL, sName) )
	storeNumber = storeNumber - 1
finalHTML.append(stores)

print(finalHTML)
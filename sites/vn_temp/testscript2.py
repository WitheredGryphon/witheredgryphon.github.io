#!/usr/bin/python

import csv
import sys
import argparse
	
#This is about to get real long

HTML = [
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
"</div></div></div><br/><div class='row' style='margin-left: 0; padding-left: 0;'><div class='col-xs-5' style='padding-left: 0; margin-right: 8px;'><div class='infoTag'>Novel Length:</div></div><div class='col-sm-6' style='margin-left: 0; padding-left: 0;'><div class='novelLength'><a data-toggle='tooltip' title='",
"' style='border-bottom: 1px dotted #8989ff; text-decoration: none;'>",
"</a></div></div></div><br /><div class='row' style='margin-left: 0; padding-left: 0;'><div class='col-xs-5' style='padding-left: 0; margin-right: 8px;'><div class='infoTag'>Anime Adaptation:</div></div><div class='col-xs-6' style='padding-left: 0; padding-right: 0; margin-right: 8px;'><div class='novelAdaptation'>",
"</div></div></div><br /><div class='row' style='margin-left: 0; padding-left: 0;'><div class='col-xs-5' style='padding-left: 0; margin-right: 8px;'><div class='infoTag'>Prequel:</div></div><div class='novelAdaptation'>",
"</div><div class='row' style='margin-left: 0; padding-left: 0;'><div class='col-xs-5' style='padding-left: 0; margin-right: 8px;'><div class='infoTag'>Sequel:</div></div><div class='novelAdaptation'>",
"</div><br /><div class='row' style='margin-left: 0; padding-left: 0; max-width: 90%'><div class='col-xs-7' style='padding-left: 0;'>",
"</div></div></div></div></div></div><div class='midWrapper'><div class='container-fluid'><div class='col-lg-8'><div class='row'><!-- Make sure you change the color in the CSS file for 'contentWarningWeb' and 'contentWarningMobile' --><div class='contentWarning contentWarningMobile'>",
"<span style='margin-left: 8px; text-align: center;'>",
"</span></div><div class='contentWarning contentWarningWeb'>",
"<span style='margin-left: 8px; text-align: center;'>",
"</span></div></div><br /><div class='row'><div class='sectionHead'>Reviews</div></div><br /><div class='row'>",
"</div><div class='row'><a href='",
"' rel='noopener' target='_blank'>",
"</a></div><br /><div class='row'>",
"</div><div class='row'><a href='",
"' rel='noopener' target='_blank'>",
"</a></div><br /><div class='row'>",
"</div><div class='row'><a href='",
"' rel='noopener' target='_blank'>",
"</a></div><br /><div class='row'><div class='sectionHead'>About This Novel</div></div><br />",
"<div class='row'>(From VNDB)</div><br /><div class='row'><div class='sectionHead'>Technical Details</div></div><br /><div class='row' style='border-bottom: 1px dashed #4d4dff50'><div class='col-xs-3' style='margin-left: 0; padding-left: 0; padding-bottom: 4px;'><span style='color: #8989ff'>Platforms: </span></div><div class='col-xs-9' style='margin-left: 0; padding-right: 0; text-align: right;'>",
"</div></div><div class='row' style='border-bottom: 1px dashed #4d4dff50'><div class='col-xs-3' style='margin-left: 0; padding-left: 0; padding-bottom: 4px; padding-top: 4px;'><span style='color: #8989ff'>Resolution: </span></div><div class='col-xs-9' style='margin-left: 0; padding-right: 0; text-align: right; padding-bottom: 4px; padding-top: 4px;'>",
"</div></div><div class='row' style='border-bottom: 1px dashed #4d4dff50'><div class='col-xs-3' style='margin-left: 0; padding-left: 0; padding-bottom: 4px; padding-top: 4px;'><span style='color: #8989ff'>English:</span></div><div class='col-xs-9' style='margin-left: 0; padding-right: 0; text-align: right; padding-bottom: 4px; padding-top: 4px;'>",
"</div></div><div class='row' style='border-bottom: 1px dashed #4d4dff50'><div class='col-xs-3' style='margin-left: 0; padding-left: 0; padding-bottom: 4px; padding-top: 4px;'><span style='color: #8989ff'>Animated Scenes: </span></div><div class='col-xs-9' style='margin-left: 0; padding-right: 0; text-align: right; padding-bottom: 4px; padding-top: 4px;'>",
"</div></div><div class='row' style='border-bottom: 1px dashed #4d4dff50'><div class='col-xs-3' style='margin-left: 0; padding-left: 0; padding-bottom: 4px; padding-top: 4px;'><span style='color: #8989ff'>Voiced: </span></div><div class='col-xs-9' style='margin-left: 0; padding-right: 0; text-align: right; padding-bottom: 4px; padding-top: 4px;'>",
"</div></div></div><div class='col-lg-3' id='webBar' style='float: right;'><div class='reccNovelsContainer'><div class='row'><div class='similarNovelsHead'>You Might Also Like</div></div><br /><div class='row'><div class='bannerThumb'><a href='",
"'><img class='lazyload' data-src='images/",
"_banner.jpg' /></a></div></div><br /><div class='row'><div class='bannerThumb'><a href='",
"'><img class='lazyload' data-src='images/",
"_banner.jpg' /></a></div></div><br /><div class='row'><div class='bannerThumb'><a href='",
"'><img class='lazyload' data-src='images/",
"_banner.jpg' /></a></div></div><br /></div><div class='row'><div class='linksHead'>Get It Now</div></div><br />",
"</div><br /><div class='row' id='mobileBar'><div class='col-xs-5'><div class = 'row'><div class='similarNovelsHead'>Recommended</div></div><br /><div class='row'><div class='bannerThumb'><a href='",
"'><img class='lazyload' data-src='images/",
"_banner.jpg' /></a></div></div><br /><div class='row'><div class='bannerThumb'><a href='",
"'><img class='lazyload' data-src='images/",
"_banner.jpg' /></a></div></div><br /><div class='row'><div class='bannerThumb'><a href='",
"'><img class='lazyload' data-src='images/",
"_banner.jpg' /></a></div></div></div><div class='col-xs-5 pull-right'><div class = 'row'><div class='linksHead'>Get It</div></div><br />",
"</div></div></div></div></div><!-- jQuery (necessary for Bootstrap's JavaScript plugins) --><script src='js/jquery-3.3.1.min.js'></script><!-- Include all compiled plugins (below), or include individual files as needed --><script src='js/bootstrap.min.js'></script><script src='js/flickity.pkgd.min.js'></script><!-- Lazy Loader --><script src='js/lazysizes.min.js'></script><script src='js/ls.unveilhooks.min.js'></script><script>$(document).ready(function(){$('.carousel-main').flickity();$('.carousel-nav').flickity({asNavFor: '.carousel-main',contain: true,pageDots: false});$('[data-toggle=\"tooltip\"]').tooltip();});</script></body></html>"
]

CSS_16x9 = [
"* {color: #e1e5e8;}img {width: inherit;}a {color:#8989ff;}a:hover {color:#8989ff;}body {background-color: #0b0c10;background-image: url('../images/",
"_wp.jpg');background-size: contain;background-repeat: no-repeat;padding-top: 24px;}.navbar {border: none;margin-bottom: 12px;}.navbar-default {background-color: #4d4dff;border-radius: 0px;border-color: unset;color: #0a0a0aab;border: 1px solid #000;box-shadow: 0px 1px 9px 2px;margin-left: 10%;margin-right: 10%;}.navbar-default .navbar-brand {font-weight: bold;color: #e1e5e8;}.navbar-default .navbar-brand:focus, .navbar-default .navbar-brand:hover {color: #b0b9bf;}/* side nav css */.sidenav {height: 100%;width: 0;position: fixed;z-index: 2;top: 0;left: 0;background-color: #0b0c10;overflow-x: hidden;transition: 0.35s;padding-top: 50px;}.sidenav .sideNavItem a {padding: 16px 8px 16px 8px;text-decoration: none;font-size: 1.2em;color: #e1e5e8;display: block;transition: 0.3s;width: max-content;}.sidenav .sideNavItem {border-bottom: solid 1px #333;width: 100%;}.sidenav a:hover {color: #b0b9bf;}.contentWrapper {margin-left: 10%;margin-right: 10%;background: linear-gradient(to top, rgba(19, 21, 27, 1) 50%, rgba(19, 21, 27, 0.8));color: #0a0a0a;box-shadow: 0px 1px 9px 2px;border: 1px solid #000;}.topWrapper {border-bottom: 2px solid #4d4dff;padding-bottom: 30px;}.midWrapper {padding-bottom: 30px;}.novelDeveloper2, .novelPublisher2 {color: #4d4dff;}.midWrapper {padding-top: 30px;padding-left: 15px;padding-right: 15px;background-color: #13151b;}.sectionHead {font-size: 24px;border-bottom: 1px solid #4d4dff;}.novelPublisher, .novelDeveloper {color: #8989ff;}.similarNovelsHead {font-size: 20px;background-color: #4d4dffbb;text-align: center;padding: 2px;}.linksHead {font-size: 20px;background-color: #4d4dffbb;text-align: center;padding: 2px;}.bannerThumb {width: 100%;}.bannerThumb img {width: 100%;}#mobileBar {display: none;}.valign {display: flex;vertical-align: middle;align-items: center;justify-content: center;}.lbWindow {width: 100%;}.lightbox .lb-image {border: 4px solid #1F2833 !important;}.lb-data .lb-number {color: #e1e5e8 !important;}.mobileNav {display: none;}.novelTitle {margin-bottom: 16px;font-size: 48px;text-align: left;}.content-slider li{text-align: center;}.developer {font-weight: normal;font-size: 24px;}.contentWarning a {color: inherit; border-bottom: 1px dashed; text-decoration: none; cursor: pointer;}.contentWarningMobile,.contentWarningWeb {border: 1px solid ",
";border-radius: 1px}.contentWarningMobile {display: none}.carousel {padding-top: 8px;margin-bottom: 20px;}.carousel img {max-height: 720px;max-width: 1280px;}.carousel-cell {width: 100%;height: auto;margin-right: 8px;counter-increment: carousel-cell;}.carousel-nav .carousel-cell img {}.carousel-nav .flickity-button {display: none;}.carousel-cell:before {display: block;text-align: center;font-size: 80px;}.carousel-nav .carousel-cell {height: auto;width: 100px;}.carousel-nav .carousel-cell:before {font-size: 50px;}.carousel-nav .carousel-cell.is-nav-selected img {border-radius: 6px;}@media screen and (max-width: 1199px) {body {padding-top: 50px;}.contentWrapper {margin: 0;}.item {margin-top: 16px;}#webBar {display: none;}#mobileBar {display: block;}.webNav {display: none;}.mobileNav {display: block;}.navbar-default {margin-left: 0;margin-right: 0;border: none;border-bottom: 1px solid #0b0c10;}}@media screen and (max-width: 767px) {.clearfix {max-width: 1024px !important;}body {background: unset;}.valign {display: block;}.novelTitle {font-size: 2.5em;}.contentWrapper {background: unset;background-color: #0b0c10;}}@media screen and (max-width:375px) {.contentWarningMobile,.contentWarningWeb {display: none}.contentWarningMobile {display: block}}"
]

CSS_4x3 = [
"/*#0b0C10 - background#1F2833 - deep blue#e1e5e8 - gray (font)#4d4dff - neon blue*/* {color: #e1e5e8;}img {width: inherit;}a {color:#8989ff;}a:hover {color:#8989ff;}body {background-color: #0b0c10;background-image: url('../images/",
"_wp.jpg');background-size: contain;background-repeat: no-repeat;padding-top: 24px;}.navbar {border: none;margin-bottom: 12px;}.navbar-default {background-color: #4d4dff;border-radius: 0px;border-color: unset;color: #0a0a0aab;border: 1px solid #000;box-shadow: 0px 1px 9px 2px;margin-left: 10%;margin-right: 10%;}.navbar-default .navbar-brand {font-weight: bold;color: #e1e5e8;}.navbar-default .navbar-brand:focus, .navbar-default .navbar-brand:hover {color: #b0b9bf;}/* side nav css */.sidenav {height: 100%;width: 0;position: fixed;z-index: 2;top: 0;left: 0;background-color: #0b0c10;overflow-x: hidden;transition: 0.35s;padding-top: 50px;}.sidenav .sideNavItem a {padding: 16px 8px 16px 8px;text-decoration: none;font-size: 1.2em;color: #e1e5e8;display: block;transition: 0.3s;width: max-content;}.sidenav .sideNavItem {border-bottom: solid 1px #333;width: 100%;}.sidenav a:hover {color: #b0b9bf;}.contentWrapper {margin-left: 10%;margin-right: 10%;background: linear-gradient(to top, rgba(19, 21, 27, 1) 50%, rgba(19, 21, 27, 0.8));color: #0a0a0a;box-shadow: 0px 1px 9px 2px;border: 1px solid #000;}.topWrapper {border-bottom: 2px solid #4d4dff;padding-bottom: 30px;}.midWrapper {padding-bottom: 30px;}.novelDeveloper2, .novelPublisher2 {color: #4d4dff;}.midWrapper {padding-top: 30px;padding-left: 15px;padding-right: 15px;background-color: #13151b;}.sectionHead {font-size: 24px;border-bottom: 1px solid #4d4dff;}.novelPublisher, .novelDeveloper {color: #8989ff;}.similarNovelsHead {font-size: 20px;background-color: #4d4dffbb;text-align: center;padding: 2px;}.linksHead {font-size: 20px;background-color: #4d4dffbb;text-align: center;padding: 2px;}.bannerThumb {width: 100%;}.bannerThumb img {width: 100%;}#mobileBar {display: none;}.valign {display: flex;vertical-align: middle;align-items: center;justify-content: center;}.lbWindow {width: 100%;}.lightbox .lb-image {border: 4px solid #1F2833 !important;}.lb-data .lb-number {color: #e1e5e8 !important;}.mobileNav {display: none;}.novelTitle {margin-bottom: 16px;font-size: 48px;text-align: left;}.content-slider li{text-align: center;}.developer {font-weight: normal;font-size: 24px;}.contentWarningMobile,.contentWarningWeb {border: 1px solid ",
";border-radius: 1px}.contentWarningMobile {display: none}.carousel {padding-top: 8px;margin-bottom: 20px;max-height: 800px;}.carousel img {max-width: 600px;max-height: 800px;}.carousel-cell {width: 100%;height: auto;margin-right: 8px;counter-increment: carousel-cell;}.carousel-nav .carousel-cell img {}.carousel-nav .flickity-button {display: none;}.carousel-cell:before {display: block;text-align: center;font-size: 80px;}.carousel-nav .carousel-cell {height: auto;width: 100px;}.carousel-nav .carousel-cell:before {font-size: 50px;}.carousel-nav .carousel-cell.is-nav-selected img {border-radius: 6px;}@media screen and (max-width: 1199px) {body {padding-top: 50px;}.contentWrapper {margin: 0;}.item {margin-top: 16px;}#webBar {display: none;}#mobileBar {display: block;}.webNav {display: none;}.mobileNav {display: block;}.navbar-default {margin-left: 0;margin-right: 0;border: none;border-bottom: 1px solid #0b0c10;}}@media screen and (max-width: 767px) {.clearfix {max-width: 1024px !important;}body {background: unset;}.valign {display: block;}.novelTitle {font-size: 2.5em;}.contentWrapper {background: unset;background-color: #0b0c10;}}@media screen and (max-width:375px) {.contentWarningMobile,.contentWarningWeb {display: none}.contentWarningMobile {display: block}}"
]

def main():	
	parser = argparse.ArgumentParser()
	parser.add_argument('-x', action='store_true')
	parser.add_argument('-c', action='store_true')
	
	options = parser.parse_args()
	if options.x:
		hd_gen()
	elif options.c:
		sd_gen()
	else:
		usage()
		sys.exit(2)

def usage():
	print("    Flags\n\t-x: Generates all 16:9 novels\n\t-c: Generates all 4:3 novels")

def sd_gen():
	data = []
	with open('NovelsSD.csv') as csvDataFile2:
		data=list(csv.reader(csvDataFile2))
		
	for m in range(1, len(data)):
		finalHTML = []
		finalCSS = []

		#Novel's title
		title = data[m][0]
		
		print("Generating " + title + " HTML...")
		
		finalHTML.append(HTML[0])
		finalHTML.append(title)

		#Just the novel title again, mostly here for customization options
		cssTitle = data[m][1]
		finalHTML.append(HTML[1])
		finalHTML.append("<link href='css/" + cssTitle + ".css' rel='stylesheet'>")

		#Typically just the novel title but lowercase
		imageTitle = data[m][2]
		finalHTML.append(HTML[2])
		for i in range(8):
			finalHTML.append("<div class='carousel-cell'><img class='lazyload' data-src='images/" + imageTitle + "_img" + str(i + 1) + ".jpg'></div>")

		finalHTML.append(HTML[3])
		for i in range(8):
			finalHTML.append("<div class='carousel-cell'><img class='lazyload' data-src='images/" + imageTitle + "_img" + str(i + 1) + ".jpg'></div>")
			
		finalHTML.append(HTML[4])
		finalHTML.append(title)

		#Release date, self-explanatory, NEEDS TO BE (MONTH DAY, YEAR) FORMAT, e.g. January 1, 2000
		release = data[m][3]
		finalHTML.append(HTML[5])
		finalHTML.append(release)

		#Direct link to developer's URL, if one isn't available use a Twitter page or something THIS IS NOT THE PUBLISHER
		developerURL = data[m][4]
		finalHTML.append(HTML[6])
		finalHTML.append(developerURL)

		#Novel developer
		developer = data[m][5]
		finalHTML.append(HTML[7])
		finalHTML.append(developer)

		#Either the novel had a publisher or a fan translator
		if data[m][6] == "N":
			publisherURL = data[m][7]
			finalHTML.append(HTML[8])
			finalHTML.append("Publisher")
			finalHTML.append(HTML[9])
			finalHTML.append(publisherURL)
			publisher = data[m][9]
			finalHTML.append(HTML[10])
			finalHTML.append(publisher)
		else:
			translatorURL = data[m][8]
			finalHTML.append(HTML[8])
			finalHTML.append("Translator")
			finalHTML.append(HTML[9])
			finalHTML.append(translatorURL)
			translator = data[m][10]
			finalHTML.append(HTML[10])
			finalHTML.append(translator)

		#PUT THE THREE GENRES LISTED ON THE FRONT PAGE FOR THE NOVEL
		#These should be comma delimited as such: "Comedy, Romance, Drama"
		#No quotes
		genres = data[m][11]
		finalHTML.append(HTML[11])
		finalHTML.append(genres)

		#Enter the number of flags
		#Then enter the ISO code associated
		#Look it up if you don't know it, if you don't you'll screw it up
		#It's two letters (Common ones are: GB for English, CN for Chinese, JP for Japanese, ES for Spanish, FR for French, IT for Italian, RU for Russian)
		flags = [x.strip() for x in data[m][12].split(',')]
		finalHTML.append(HTML[12])
		for x in flags:
			finalHTML.append("<span class='flag-icon flag-icon-" + x + " flag-icon-squared' style='margin-right: 4px;'></span>")

		#Get it from HowLongToBeat, otherwise pull from VNDB
		lengthHLTB = data[m][13]
		lengthVNDB = ""
		if lengthHLTB != "":
			finalHTML.append(HTML[13])
			finalHTML.append("Based on all play styles from HowLongToBeat.")
			finalHTML.append(HTML[14])
			finalHTML.append(lengthHLTB + " Hours")
		else:
			lengthVNDB = data[m][14]
			finalHTML.append(HTML[13])
			finalHTML.append("Based on estimated average from VNDB.")
			finalHTML.append(HTML[14])
			finalHTML.append(lengthVNDB + " Hours")

		#Anime adaptations, put how many then put the URL
		adaptations = [x.strip() for x in data[m][15].split(',')]
		finalHTML.append(HTML[15])

		if adaptations[0] != "":
			for i in range(len(adaptations)):
				if i % 2 == 0:
					finalHTML.append("<div class='row' style='margin: 0;'><a href='" + adaptations[i] + "' rel='noopener' target='_blank'>")
				else:
					finalHTML.append(adaptations[i] + "</a></div>")
		else:
			finalHTML.append("<div class='row' style='margin: 0;'>None</div>")

		#If there's a prequel and/or sequel list it
		prequel = [x.strip() for x in data[m][16].split(',')]
		sequel = [x.strip() for x in data[m][17].split(',')]
		if prequel[0] != "None":
			finalHTML.append(HTML[16])
			finalHTML.append("<a href='" + prequel[0] + "' rel='noopener' target='_blank'>" + prequel[1] + "</a></div>")
		else:
			finalHTML.append(HTML[16])
			finalHTML.append(prequel[0] + "</div>")
			
		if sequel[0] != "None":
			finalHTML.append(HTML[17])
			finalHTML.append("<a href='" + sequel[0] + "' rel='noopener' target='_blank'>" + sequel[1] + "</a></div>")
		else:
			finalHTML.append(HTML[17])
			finalHTML.append(sequel[0] + "</div>")

		#Reddit and VNDB, post links
		reddit = data[m][18]
		vndb = data[m][19]
		finalHTML.append(HTML[18])
		finalHTML.append("<a data-toggle='tooltip' title='VNDB' style='font-size: 32px;' href='" + vndb + "' rel='noopener' target='_blank'><img class='lazyload' data-src='images/vndb_button.png' style='padding-right: 8px;'></a>")
		if reddit != "":
			finalHTML.append("<a data-toggle='tooltip' title='Reddit' style='font-size: 32px;' href='" + reddit + "' rel='noopener' target='_blank'><img class='lazyload' data-src='images/reddit_button.png' style='padding-right: 8px;'></a>")

		#Age
		#Valid inputs are:
		#0 for all ages, 15, 17, 18
		#Get the age rating from VNDB
		#If there's a patch, put the link
		age = data[m][20]
		patch = data[m][21]
		finalHTML.append(HTML[19])
		
		if age != "0":
			finalHTML.append("<img class='lazyload' data-src='images/" + age + "up_icon.jpg'>")
		else:
			finalHTML.append("<img class='lazyload' data-src='images/AllAges_icon.jpg'>")

		finalHTML.append(HTML[20])

		if patch != "N":
			if age == "0":
				finalHTML.append("<a data-toggle='tooltip' title='18+ patch available'>This game is rated all ages.</a>")
			else:
				finalHTML.append("<a data-toggle='tooltip' title='18+ patch available'>This game is rated ages " + age + "+</a>")
		else:
			if age == "0":
				finalHTML.append("This game is rated all ages.")
			else:
				finalHTML.append("This game is rated ages " + age + "+")

			
		finalHTML.append(HTML[21])

		if age != "0":
			finalHTML.append("<img class='lazyload' data-src='images/" + age + "up_icon.jpg'>")
		else:
			finalHTML.append("<img class='lazyload' data-src='images/AllAges_icon.jpg'>")

		finalHTML.append(HTML[22])

		if patch != "N":
			if age == "0":
				finalHTML.append("<a data-toggle='tooltip' title='18+ patch available'>This game is intended for all ages.</a>")
			else:
				finalHTML.append("<a data-toggle='tooltip' title='18+ patch available'>This game is intended for ages " + age + "+</a>")
		else:
			if age == "0":
				finalHTML.append("This game is intended for all ages.")
			else:
				finalHTML.append("This game is intended for ages " + age + "+")

		#Reviews
		review1Text = data[m][22]
		review1URL = data[m][23]
		review1Name = data[m][24]
		finalHTML.append(HTML[23])
		finalHTML.append(review1Text)
		finalHTML.append(HTML[24])
		finalHTML.append(review1URL)
		finalHTML.append(HTML[25])
		finalHTML.append(review1Name)

		review2Text = data[m][25]
		review2URL = data[m][26]
		review2Name = data[m][27]
		finalHTML.append(HTML[26])
		finalHTML.append(review2Text)
		finalHTML.append(HTML[27])
		finalHTML.append(review2URL)
		finalHTML.append(HTML[28])
		finalHTML.append(review2Name)

		review3Text = data[m][28]
		review3URL = data[m][29]
		review3Name = data[m][30]
		finalHTML.append(HTML[29])
		finalHTML.append(review3Text)
		finalHTML.append(HTML[30])
		finalHTML.append(review3URL)
		finalHTML.append(HTML[31])
		finalHTML.append(review3Name)

		#Novel's Description, try \n for new lines?
		aboutText = [x for x in data[m][31].split('`')]
		finalHTML.append(HTML[32])
		for row in aboutText:
			finalHTML.append("<div class='row'>" + row + "</div><br />")

		#Platforms available on in English (probably)
		platforms = [x.strip() for x in data[m][32].split(',')]
		finalHTML.append(HTML[33])
		for p in platforms:
			if p == platforms[-1]:
				finalHTML.append(p)
			else:
				finalHTML.append(p + ", ")

		#Resolution, either 16:9 or 4:3, pick one
		resolution = data[m][33]
		finalHTML.append(HTML[34])
		finalHTML.append(resolution)

		#If there's a patch, fill it in with the URL. Otherwise LEAVE IT BLANK
		patch = data[m][34]
		finalHTML.append(HTML[35])
		if patch != "":
			if patch == "Unavailable":
				finalHTML.append("Unavailable")
			else:
				finalHTML.append("<a data-toggle='tooltip' title='English Patch for PC Version' href='" + patch + "'>Patched</a>")
		else:
			finalHTML.append("Fully Translated")
			
		#Animated scenes, either Full, Simple, or None
		#Get it from VNDB, if it isn't listed then put None
		animated = data[m][35]
		finalHTML.append(HTML[36])
		finalHTML.append(animated)

		#Voiced, either Fully, Partial, or None
		#Get it from VNDB, if it isn't listed then put None
		voiced = data[m][36]
		finalHTML.append(HTML[37])
		finalHTML.append(voiced)

		#Recommendations
		#Name and image name needed
		#e.g.
		#r1Name = lb (this will turn into images/lb_banner.jpg)
		#r1URL = relative URL to the page (LittleBusters.html, etc.)
		r1Name = data[m][37]
		r1URL = data[m][38]
		r2Name = data[m][39]
		r2URL = data[m][40]
		r3Name = data[m][41]
		r3URL = data[m][42]
		finalHTML.append(HTML[38])
		finalHTML.append(r1URL)
		finalHTML.append(HTML[39])
		finalHTML.append(r1Name)
		finalHTML.append(HTML[40])
		finalHTML.append(r2URL)
		finalHTML.append(HTML[41])
		finalHTML.append(r2Name)
		finalHTML.append(HTML[42])
		finalHTML.append(r3URL)
		finalHTML.append(HTML[43])
		finalHTML.append(r3Name)

		#Store Availability
		#First the number of stores
		#Then the name of the stores (Steam, MangaGamer, J-List, Amazon, Itch.io, etc. List of buttons is in the files, just search for "button")
		#Then the link to the purchase site
		#VNDB usually has these if you click the specific revision of the game and hit "Official Link"

		stores = [x.strip() for x in data[m][43].split(',')]
		finalHTML.append(HTML[44])

		for i in range(len(stores)):
			if i == len(stores) - 1:
				finalHTML.append(stores[i] + "_button.png' style='width: 100%;'></a></div>")
				break
			if i % 2 == 0:
				finalHTML.append("<div class='row' style='text-align: center'><a href='" + stores[i] + "' rel='noopener' target='_blank'><img class='lazyload' data-src='images/")
			else:
				finalHTML.append(stores[i] + "_button.png' style='width: 100%;'></a></div><br />")

		finalHTML.append(HTML[45])
		finalHTML.append(r1URL)
		finalHTML.append(HTML[46])
		finalHTML.append(r1Name)
		finalHTML.append(HTML[47])
		finalHTML.append(r2URL)
		finalHTML.append(HTML[48])
		finalHTML.append(r2Name)
		finalHTML.append(HTML[49])
		finalHTML.append(r3URL)
		finalHTML.append(HTML[50])
		finalHTML.append(r3Name)

		finalHTML.append(HTML[51])
		for i in range(len(stores)):
			if i == len(stores) - 1:
				finalHTML.append(stores[i] + "_button.png' style='width: 100%;'></a></div>")
				break
			if i % 2 == 0:
				finalHTML.append("<div class='row' style='text-align: center'><a href='" + stores[i] + "' rel='noopener' target='_blank'><img class='lazyload' data-src='images/")
			else:
				finalHTML.append(stores[i] + "_button.png' style='width: 100%;'></a></div><br />")


		finalHTML.append(HTML[52])

		Html_file = open(cssTitle + ".html","w")
		Html_file.write("".join(finalHTML))
		Html_file.close()
		
		print("Generating " + title + " CSS...")

		finalCSS.append(CSS_4x3[0])
		wallpaper = imageTitle
		finalCSS.append(wallpaper)

		finalCSS.append(CSS_4x3[1])
		if age == "18":
			finalCSS.append("#fe0000")
		elif age == "17":
			finalCSS.append("#ff6302")
		elif age == "15":
			finalCSS.append("#feb043")
		else:
			finalCSS.append("#86c341")
			
		finalCSS.append(CSS_4x3[2])

		Css_file = open("css/" + cssTitle + ".css","w")
		Css_file.write("".join(finalCSS))
		Css_file.close()
		
		print("Generation for " + title + " complete.")

	print("All titles generated.")

def hd_gen():
	data = []
	with open('NovelsHD.csv') as csvDataFile:
		data=list(csv.reader(csvDataFile))

	print(len(data))
		
	for m in range(1, len(data)):
		finalHTML = []
		finalCSS = []

		#Novel's title
		title = data[m][0]
		
		print("Generating " + title + " HTML...")
		
		finalHTML.append(HTML[0])
		finalHTML.append(title)

		#Just the novel title again, mostly here for customization options
		cssTitle = data[m][1]
		finalHTML.append(HTML[1])
		finalHTML.append("<link href='css/" + cssTitle + ".css' rel='stylesheet'>")

		#Typically just the novel title but lowercase
		imageTitle = data[m][2]
		finalHTML.append(HTML[2])
		for i in range(8):
			finalHTML.append("<div class='carousel-cell'><img class='lazyload' data-src='images/" + imageTitle + "_img" + str(i + 1) + ".jpg'></div>")

		finalHTML.append(HTML[3])
		for i in range(8):
			finalHTML.append("<div class='carousel-cell'><img class='lazyload' data-src='images/" + imageTitle + "_img" + str(i + 1) + ".jpg'></div>")
			
		finalHTML.append(HTML[4])
		finalHTML.append(title)

		#Release date, self-explanatory, NEEDS TO BE (MONTH DAY, YEAR) FORMAT, e.g. January 1, 2000
		release = data[m][3]
		finalHTML.append(HTML[5])
		finalHTML.append(release)

		#Direct link to developer's URL, if one isn't available use a Twitter page or something THIS IS NOT THE PUBLISHER
		developerURL = data[m][4]
		finalHTML.append(HTML[6])
		finalHTML.append(developerURL)

		#Novel developer
		developer = data[m][5]
		finalHTML.append(HTML[7])
		finalHTML.append(developer)

		#Either the novel had a publisher or a fan translator
		if data[m][6] == "N":
			publisherURL = data[m][7]
			finalHTML.append(HTML[8])
			finalHTML.append("Publisher")
			finalHTML.append(HTML[9])
			finalHTML.append(publisherURL)
			publisher = data[m][9]
			finalHTML.append(HTML[10])
			finalHTML.append(publisher)
		else:
			translatorURL = data[m][8]
			finalHTML.append(HTML[8])
			finalHTML.append("Translator")
			finalHTML.append(HTML[9])
			finalHTML.append(translatorURL)
			translator = data[m][10]
			finalHTML.append(HTML[10])
			finalHTML.append(translator)

		#PUT THE THREE GENRES LISTED ON THE FRONT PAGE FOR THE NOVEL
		#These should be comma delimited as such: "Comedy, Romance, Drama"
		#No quotes
		genres = data[m][11]
		finalHTML.append(HTML[11])
		finalHTML.append(genres)

		#Enter the number of flags
		#Then enter the ISO code associated
		#Look it up if you don't know it, if you don't you'll screw it up
		#It's two letters (Common ones are: GB for English, CN for Chinese, JP for Japanese, ES for Spanish, FR for French, IT for Italian, RU for Russian)
		flags = [x.strip() for x in data[m][12].split(',')]
		finalHTML.append(HTML[12])
		for x in flags:
			finalHTML.append("<span class='flag-icon flag-icon-" + x + " flag-icon-squared' style='margin-right: 4px;'></span>")

		#Get it from HowLongToBeat, otherwise pull from VNDB
		lengthHLTB = data[m][13]
		lengthVNDB = ""
		if lengthHLTB != "":
			finalHTML.append(HTML[13])
			finalHTML.append("Based on all play styles from HowLongToBeat.")
			finalHTML.append(HTML[14])
			finalHTML.append(lengthHLTB + " Hours")
		else:
			lengthVNDB = data[m][14]
			finalHTML.append(HTML[13])
			finalHTML.append("Based on estimated average from VNDB.")
			finalHTML.append(HTML[14])
			finalHTML.append(lengthVNDB + " Hours")

		#Anime adaptations, put how many then put the URL
		adaptations = [x.strip() for x in data[m][15].split(',')]
		finalHTML.append(HTML[15])

		if adaptations[0] != "":
			for i in range(len(adaptations)):
				if i % 2 == 0:
					finalHTML.append("<div class='row' style='margin: 0;'><a href='" + adaptations[i] + "' rel='noopener' target='_blank'>")
				else:
					finalHTML.append(adaptations[i] + "</a></div>")
		else:
			finalHTML.append("<div class='row' style='margin: 0;'>None</div>")

		#If there's a prequel and/or sequel list it
		prequel = [x.strip() for x in data[m][16].split(',')]
		sequel = [x.strip() for x in data[m][17].split(',')]
		if prequel[0] != "None":
			finalHTML.append(HTML[16])
			finalHTML.append("<a href='" + prequel[0] + "' rel='noopener' target='_blank'>" + prequel[1] + "</a></div>")
		else:
			finalHTML.append(HTML[16])
			finalHTML.append(prequel[0] + "</div>")
			
		if sequel[0] != "None":
			finalHTML.append(HTML[17])
			finalHTML.append("<a href='" + sequel[0] + "' rel='noopener' target='_blank'>" + sequel[1] + "</a></div>")
		else:
			finalHTML.append(HTML[17])
			finalHTML.append(sequel[0] + "</div>")

		#Reddit and VNDB, post links
		reddit = data[m][18]
		vndb = data[m][19]
		finalHTML.append(HTML[18])
		finalHTML.append("<a data-toggle='tooltip' title='VNDB' style='font-size: 32px;' href='" + vndb + "' rel='noopener' target='_blank'><img class='lazyload' data-src='images/vndb_button.png' style='padding-right: 8px;'></a>")
		if reddit != "":
			finalHTML.append("<a data-toggle='tooltip' title='Reddit' style='font-size: 32px;' href='" + reddit + "' rel='noopener' target='_blank'><img class='lazyload' data-src='images/reddit_button.png' style='padding-right: 8px;'></a>")

		#Age
		#Valid inputs are:
		#0 for all ages, 15, 17, 18
		#Get the age rating from VNDB
		#If there's a patch, put the link
		age = data[m][20]
		patch = data[m][21]
		finalHTML.append(HTML[19])
		
		if age != "0":
			finalHTML.append("<img class='lazyload' data-src='images/" + age + "up_icon.jpg'>")
		else:
			finalHTML.append("<img class='lazyload' data-src='images/AllAges_icon.jpg'>")

		finalHTML.append(HTML[20])

		if patch != "N":
			if age == "0":
				finalHTML.append("<a data-toggle='tooltip' title='18+ patch available'>This game is rated all ages.</a>")
			else:
				finalHTML.append("<a data-toggle='tooltip' title='18+ patch available'>This game is rated ages " + age + "+</a>")
		else:
			if age == "0":
				finalHTML.append("This game is rated all ages.")
			else:
				finalHTML.append("This game is rated ages " + age + "+")

			
		finalHTML.append(HTML[21])

		if age != "0":
			finalHTML.append("<img class='lazyload' data-src='images/" + age + "up_icon.jpg'>")
		else:
			finalHTML.append("<img class='lazyload' data-src='images/AllAges_icon.jpg'>")

		finalHTML.append(HTML[22])

		if patch != "N":
			if age == "0":
				finalHTML.append("<a data-toggle='tooltip' title='18+ patch available'>This game is intended for all ages.</a>")
			else:
				finalHTML.append("<a data-toggle='tooltip' title='18+ patch available'>This game is intended for ages " + age + "+</a>")
		else:
			if age == "0":
				finalHTML.append("This game is intended for all ages.")
			else:
				finalHTML.append("This game is intended for ages " + age + "+")

		#Reviews
		review1Text = data[m][22]
		review1URL = data[m][23]
		review1Name = data[m][24]
		finalHTML.append(HTML[23])
		finalHTML.append(review1Text)
		finalHTML.append(HTML[24])
		finalHTML.append(review1URL)
		finalHTML.append(HTML[25])
		finalHTML.append(review1Name)

		review2Text = data[m][25]
		review2URL = data[m][26]
		review2Name = data[m][27]
		finalHTML.append(HTML[26])
		finalHTML.append(review2Text)
		finalHTML.append(HTML[27])
		finalHTML.append(review2URL)
		finalHTML.append(HTML[28])
		finalHTML.append(review2Name)

		review3Text = data[m][28]
		review3URL = data[m][29]
		review3Name = data[m][30]
		finalHTML.append(HTML[29])
		finalHTML.append(review3Text)
		finalHTML.append(HTML[30])
		finalHTML.append(review3URL)
		finalHTML.append(HTML[31])
		finalHTML.append(review3Name)

		#Novel's Description, try \n for new lines?
		aboutText = [x for x in data[m][31].split('`')]
		finalHTML.append(HTML[32])
		for row in aboutText:
			finalHTML.append("<div class='row'>" + row + "</div><br />")

		#Platforms available on in English (probably)
		platforms = [x.strip() for x in data[m][32].split(',')]
		finalHTML.append(HTML[33])
		for p in platforms:
			if p == platforms[-1]:
				finalHTML.append(p)
			else:
				finalHTML.append(p + ", ")

		#Resolution, either 16:9 or 4:3, pick one
		resolution = data[m][33]
		finalHTML.append(HTML[34])
		finalHTML.append(resolution)

		#If there's a patch, fill it in with the URL. Otherwise LEAVE IT BLANK
		patch = data[m][34]
		finalHTML.append(HTML[35])
		if patch != "":
			if patch == "Unavailable":
				finalHTML.append("Unavailable")
			else:
				finalHTML.append("<a data-toggle='tooltip' title='English Patch for PC Version' href='" + patch + "'>Patched</a>")
		else:
			finalHTML.append("Fully Translated")
			
		#Animated scenes, either Full, Simple, or None
		#Get it from VNDB, if it isn't listed then put None
		animated = data[m][35]
		finalHTML.append(HTML[36])
		finalHTML.append(animated)

		#Voiced, either Fully, Partial, or None
		#Get it from VNDB, if it isn't listed then put None
		voiced = data[m][36]
		finalHTML.append(HTML[37])
		finalHTML.append(voiced)

		#Recommendations
		#Name and image name needed
		#e.g.
		#r1Name = lb (this will turn into images/lb_banner.jpg)
		#r1URL = relative URL to the page (LittleBusters.html, etc.)
		r1Name = data[m][37]
		r1URL = data[m][38]
		r2Name = data[m][39]
		r2URL = data[m][40]
		r3Name = data[m][41]
		r3URL = data[m][42]
		finalHTML.append(HTML[38])
		finalHTML.append(r1URL)
		finalHTML.append(HTML[39])
		finalHTML.append(r1Name)
		finalHTML.append(HTML[40])
		finalHTML.append(r2URL)
		finalHTML.append(HTML[41])
		finalHTML.append(r2Name)
		finalHTML.append(HTML[42])
		finalHTML.append(r3URL)
		finalHTML.append(HTML[43])
		finalHTML.append(r3Name)

		#Store Availability
		#First the number of stores
		#Then the name of the stores (Steam, MangaGamer, J-List, Amazon, Itch.io, etc. List of buttons is in the files, just search for "button")
		#Then the link to the purchase site
		#VNDB usually has these if you click the specific revision of the game and hit "Official Link"

		stores = [x.strip() for x in data[m][43].split(',')]
		finalHTML.append(HTML[44])

		for i in range(len(stores)):
			if i == len(stores) - 1:
				finalHTML.append(stores[i] + "_button.png' style='width: 100%;'></a></div>")
				break
			if i % 2 == 0:
				finalHTML.append("<div class='row' style='text-align: center'><a href='" + stores[i] + "' rel='noopener' target='_blank'><img class='lazyload' data-src='images/")
			else:
				finalHTML.append(stores[i] + "_button.png' style='width: 100%;'></a></div><br />")

		finalHTML.append(HTML[45])
		finalHTML.append(r1URL)
		finalHTML.append(HTML[46])
		finalHTML.append(r1Name)
		finalHTML.append(HTML[47])
		finalHTML.append(r2URL)
		finalHTML.append(HTML[48])
		finalHTML.append(r2Name)
		finalHTML.append(HTML[49])
		finalHTML.append(r3URL)
		finalHTML.append(HTML[50])
		finalHTML.append(r3Name)

		finalHTML.append(HTML[51])
		for i in range(len(stores)):
			if i == len(stores) - 1:
				finalHTML.append(stores[i] + "_button.png' style='width: 100%;'></a></div>")
				break
			if i % 2 == 0:
				finalHTML.append("<div class='row' style='text-align: center'><a href='" + stores[i] + "' rel='noopener' target='_blank'><img class='lazyload' data-src='images/")
			else:
				finalHTML.append(stores[i] + "_button.png' style='width: 100%;'></a></div><br />")


		finalHTML.append(HTML[52])

		Html_file = open(cssTitle + ".html","w")
		Html_file.write("".join(finalHTML))
		Html_file.close()
		
		print("Generating " + title + " CSS...")

		finalCSS.append(CSS_16x9[0])
		wallpaper = imageTitle
		finalCSS.append(wallpaper)

		finalCSS.append(CSS_16x9[1])
		if age == "18":
			finalCSS.append("#fe0000")
		elif age == "17":
			finalCSS.append("#ff6302")
		elif age == "15":
			finalCSS.append("#feb043")
		else:
			finalCSS.append("#86c341")
			
		finalCSS.append(CSS_16x9[2])

		Css_file = open("css/" + cssTitle + ".css","w")
		Css_file.write("".join(finalCSS))
		Css_file.close()
		
		print("Generation for " + title + " complete.")

	print("All titles generated.")
	
if __name__ == "__main__":
    main()

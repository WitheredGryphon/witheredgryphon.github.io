"use strict";

var version = 'v1::';

self.addEventListener('install', function(event) {
	event.waitUntil(
    	caches.open(version + '-cache').then(function(cache) {
			return cache.addAll(
        	[
				'/sites/vn_temp/',
				'/sites/vn_temp/css/bootstrap.min.css',
				'/sites/vn_temp/css/bootstrap.min.css.map',
				'/sites/vn_temp/css/main.css',
				'/sites/vn_temp/css/bootstrap-theme.min.css',
				'/sites/vn_temp/css/docs.css',
				'/sites/vn_temp/css/fa-brands.min.css',
				'/sites/vn_temp/css/fa-regular.min.css',
				'/sites/vn_temp/css/fa-solid.min.css',
				'/sites/vn_temp/css/fakeloader.css',
				'/sites/vn_temp/css/flag-icon.min.css',
				'/sites/vn_temp/css/fontawesome-all.min.css',
				'/sites/vn_temp/css/KatawaShoujo.css',
				'/sites/vn_temp/css/lightbox.css',
				'/sites/vn_temp/css/lightslider.css',
				'/sites/vn_temp/css/LittleBusters.css',
				'/sites/vn_temp/js/bootstrap.min.js',
				'/sites/vn_temp/js/jquery-3.3.1.min.js',
				'/sites/vn_temp/js/fakeloader.min.js',
				'/sites/vn_temp/js/jcarousel.connected-carousels.js',
				'/sites/vn_temp/js/jcarousel.responsive.js',
				'/sites/vn_temp/js/jquery.jcarousel.min.js',
				'/sites/vn_temp/js/lightbox.js',
				'/sites/vn_temp/js/lightslider.js',
				'/sites/vn_temp/js/npm.js',
				'/sites/vn_temp/index.html',
				'/sites/vn_temp/KatawaShoujo.html',
				'/sites/vn_temp/LittleBusters.html',
				'/sites/vn_temp/images/999_thumb.png',
				'/sites/vn_temp/images/amnesia_thumb.png',
				'/sites/vn_temp/images/busters_img1.jpg',
				'/sites/vn_temp/images/busters_img2.jpg',
				'/sites/vn_temp/images/busters_img3.jpg',
				'/sites/vn_temp/images/busters_img4.jpg',
				'/sites/vn_temp/images/busters_img5.jpg',
				'/sites/vn_temp/images/busters_img6.jpg',
				'/sites/vn_temp/images/busters_img7.jpg',
				'/sites/vn_temp/images/busters_img8.jpg',
				'/sites/vn_temp/images/busters_img9.jpg',
				'/sites/vn_temp/images/busters_img10.jpg',
				'/sites/vn_temp/images/busters_img11.jpg',
				'/sites/vn_temp/images/busters_img12.jpg',
				'/sites/vn_temp/images/busters_img13.jpg',
				'/sites/vn_temp/images/busters_wp.png',
				'/sites/vn_temp/images/clannad_banner.jpg',
				'/sites/vn_temp/images/clannad_thumb.png',
				'/sites/vn_temp/images/close.png',
				'/sites/vn_temp/images/controls.png',
				'/sites/vn_temp/images/devil_on_g_string_thumb.png',
				'/sites/vn_temp/images/dies_irae.png',
				'/sites/vn_temp/images/dramatical_murder_thumb.png',
				'/sites/vn_temp/images/fate_stay_night_thumb.png',
				'/sites/vn_temp/images/grisaia_banner.jpg',
				'/sites/vn_temp/images/hifm.png',
				'/sites/vn_temp/images/higurashi.png',
				'/sites/vn_temp/images/Katawa_Shoujo_choices_menu.png',
				'/sites/vn_temp/images/katawa_shoujo_thumb.png',
				'/sites/vn_temp/images/lb_banner.jpg',
				'/sites/vn_temp/images/little_busters_thumb.png',
				'/sites/vn_temp/images/loading.gif',
				'/sites/vn_temp/images/monster_girl_quest_thumb.png',
				'/sites/vn_temp/images/next.png',
				'/sites/vn_temp/images/phoenix_wright_thumb.png',
				'/sites/vn_temp/images/planetarian_thumb.png',
				'/sites/vn_temp/images/prev.png',
				'/sites/vn_temp/images/rewrite_banner.jpg',
				'/sites/vn_temp/images/rewrite_thumb.png',
				'/sites/vn_temp/images/saya_no_uta_thumb.png',
				'/sites/vn_temp/images/shoujo_img1.jpg',
				'/sites/vn_temp/images/shoujo_img2.jpg',
				'/sites/vn_temp/images/shoujo_img3.jpg',
				'/sites/vn_temp/images/shoujo_img4.jpg',
				'/sites/vn_temp/images/shoujo_img5.jpg',
				'/sites/vn_temp/images/shoujo_img6.jpg',
				'/sites/vn_temp/images/shoujo_img7.jpg',
				'/sites/vn_temp/images/shoujo_img8.jpg',
				'/sites/vn_temp/images/shoujo_img9.jpg',
				'/sites/vn_temp/images/shoujo_img10.jpg',
				'/sites/vn_temp/images/shoujo_img11.jpg',
				'/sites/vn_temp/images/shoujo_img12.jpg',
				'/sites/vn_temp/images/shoujo_img13.jpg',
				'/sites/vn_temp/images/shoujo_wp.png',
				'/sites/vn_temp/images/android-chrome-192x192.png',
				'/sites/vn_temp/images/android-chrome-512x512.png',
				'/sites/vn_temp/images/apple-touch-icon.png',
				'/sites/vn_temp/images/browserconfig.xml',
				'/sites/vn_temp/images/favicon-16x16.png',
				'/sites/vn_temp/images/favicon-32x32.png',
				'/sites/vn_temp/images/mstile-150x150.png',
				'/sites/vn_temp/images/site.webmanifest',
				'/sites/vn_temp/images/safari-pinned-tab.svg',
				'/sites/vn_temp/images/15up_icon.jpg',
				'/sites/vn_temp/images/17up_icon.jpg',
				'/sites/vn_temp/images/18up_icon.jpg',
				'/sites/vn_temp/images/AllAges_icon.jpg',
				'/sites/vn_temp/images/steam_button.png',
				'/sites/vn_temp/images/vndb_button.png',
				'/sites/vn_temp/images/website_button.png',
				'/sites/vn_temp/images/reddit_button.png',
				'/sites/vn_temp/images/jlist_button.png',
				'/sites/vn_temp/images/itch_button.png',
				'/sites/vn_temp/images/jast_button.png',
				'/sites/vn_temp/images/mangagamer_button.png',
				'/sites/vn_temp/images/denpasoft_button.png',
				'/sites/vn_temp/images/rightstuf_button.png',
				'/sites/vn_temp/images/gog_button.png',
				'/sites/vn_temp/fonts/glyphicons-halflings-regular.woff2',
				'/sites/vn_temp/fonts/glyphicons-halflings-regular.woff',
				'/sites/vn_temp/fonts/glyphicons-halflings-regular.ttf',
				'/sites/vn_temp/flags/4x3/br.svg',
				'/sites/vn_temp/flags/4x3/pl.svg',
				'/sites/vn_temp/flags/4x3/es.svg',
				'/sites/vn_temp/flags/4x3/ru.svg',
				'/sites/vn_temp/flags/4x3/hu.svg',
				'/sites/vn_temp/flags/4x3/de.svg',
				'/sites/vn_temp/flags/4x3/fr.svg',
				'/sites/vn_temp/flags/4x3/jp.svg',
				'/sites/vn_temp/flags/4x3/cn.svg',
				'/sites/vn_temp/flags/4x3/it.svg',
				'/sites/vn_temp/flags/4x3/it.svg',
				'/sites/vn_temp/flags/4x3/gb.svg',
				'/sites/vn_temp/flags/1x1/br.svg',
				'/sites/vn_temp/flags/1x1/pl.svg',
				'/sites/vn_temp/flags/1x1/es.svg',
				'/sites/vn_temp/flags/1x1/ru.svg',
				'/sites/vn_temp/flags/1x1/hu.svg',
				'/sites/vn_temp/flags/1x1/de.svg',
				'/sites/vn_temp/flags/1x1/fr.svg',
				'/sites/vn_temp/flags/1x1/jp.svg',
				'/sites/vn_temp/flags/1x1/cn.svg',
				'/sites/vn_temp/flags/1x1/it.svg',
				'/sites/vn_temp/flags/1x1/it.svg',
				'/sites/vn_temp/flags/1x1/gb.svg',
				'/sites/vn_temp/webfonts/fa-solid-900.woff',
				'/sites/vn_temp/webfonts/fa-solid-900.woff2',
				'/sites/vn_temp/webfonts/fa-solid-900.ttf',
				'/sites/vn_temp/webfonts/fa-brands-400.ttf',
				'/sites/vn_temp/webfonts/fa-brands-400.woff',
				'/sites/vn_temp/webfonts/fa-brands-400.woff2'
			]);
    	})
		.then(function() {
			//console.log('WORKER: install complete');
		})
	);
});

// https://css-tricks.com/serviceworker-for-offline/
// NICOLAS BEVACQUA ON NOVEMBER 10, 2015
self.addEventListener('fetch', function(event) {
	//console.log('WORKER: fetch started')

	// Fix by Paul Irish for Chromium dev tools bug generating errors
	if (event.request.cache === 'only-if-cached' && event.request.mode !== 'same-origin') {
		return;
	}
	if (event.request.method !== 'GET') {
		//console.log('WORKER: fetch ignored', event.request.method, event.request.url);
		return;
	}

	event.respondWith(
		caches.match(event.request).then(function(cached) {
			var netReq = fetch(event.request)
				.then(fetchedFromNetwork, unableToResolve)
				.catch(unableToResolve);

			//console.log('WORKER: fetch event', cached ? '(cached)' : '(network)', event.request.url);
			return cached || netReq; // return true if we have a cached or networked match

			function fetchedFromNetwork(repsonse) {
				var cacheCopy = response.clone();

				//console.log('WORKER: fetch response from network', event.request.url);

				caches.open(version + 'pages').then(function add(cache) {
					cache.put(event.request, cacheCopy);
				})
				.then(function() {
					//console.log('WORKER: fetch response stored in cache', event.request.url);
				});

				return response;
			}

			function unableToResolve() {
				//console.log('WORKER: fetch request from both cache and network failed');

				return new Response('<h1>Service Unavailable</h1>', {
					status: 503,
					statusText: 'Service Unavailable',
					headers: new Headers({
						'Content-Type': 'text/html'
					})
				});
			}
		})
	);
});

self.addEventListener('activate', function(event) {
	//console.log('WORKER: activation in progress');

	event.waitUntil(
		caches.keys().then(function(keys) {
			return Promise.all(
				keys.filter(function(key) {
					return !key.startsWith(version);
				}).map(function(key) {
					return caches.delete(key);
				})
			);
		})
		.then(function() {
			//console.log('WORKER: activation complete');
		})
	);
});

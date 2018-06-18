"use strict";

var version = 'v1::';

self.addEventListener('install', function(event) {
	event.waitUntil(
    	caches.open(version + '-cache').then(function(cache) {
			return cache.addAll(
        	[
				'/sites/vn_temp/',
				'/sites/vn_temp/css/bootstrap.css',
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
				'/sites/vn_temp/css/lightslider.min.css',
				'/sites/vn_temp/css/LittleBusters.css',
				'/sites/vn_temp/js/bootstrap.min.js',
				'/sites/vn_temp/js/jquery-3.3.1.min.js',
				'/sites/vn_temp/js/fakeloader.min.js',
				'/sites/vn_temp/js/jcarousel.connected-carousels.js',
				'/sites/vn_temp/js/jcarousel.responsive.js',
				'/sites/vn_temp/js/jquery.jcarousel.min.js',
				'/sites/vn_temp/js/lightbox.js',
				'/sites/vn_temp/js/lightslider.min.js',
				'/sites/vn_temp/js/npm.js',
				'/sites/vn_temp/index.html',
				'/sites/vn_temp/GandBNovels.html',
				'/sites/vn_temp/KatawaShoujo.html',
				'/sites/vn_temp/LittleBusters.html'
			]);
    	})
		.then(function() {
			console.log('WORKER: install complete');
		})
	);
});

// https://css-tricks.com/serviceworker-for-offline/
// NICOLAS BEVACQUA ON NOVEMBER 10, 2015
self.addEventListener('fetch', function(event) {
	console.log('WORKER: fetch started')

	// Fix by Paul Irish for Chromium dev tools bug generating errors
	if (event.request.cache === 'only-if-cached' && event.request.mode !== 'same-origin') {
		return;
	}
	if (event.request.method !== 'GET') {
		console.log('WORKER: fetch ignored', event.request.method, event.request.url);
		return;
	}

	event.respondWith(
		caches.match(event.request).then(function(cached) {
			var netReq = fetch(event.request)
				.then(fetchedFromNetwork, unableToResolve)
				.catch(unableToResolve);

			console.log('WORKER: fetch event', cached ? '(cached)' : '(network)', event.request.url);
			return cached || networked; // return true if we have a cached or networked match

			function fetchedFromNetwork(repsonse) {
				var cacheCopy = response.clone();

				console.log('WORKER: fetch response from network', event.request.url);

				caches.open(version + 'pages').then(function add(cache) {
					cache.put(event.request, cacheCopy);
				})
				.then(function() {
					console.log('WORKER: fetch response stored in cache', event.request.url);
				});

				return response;
			}

			function unableToResolve() {
				console.log('WORKER: fetch request from both cache and network failed');

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
	console.log('WORKER: activation in progress');

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
			console.log('WORKER: activation complete');
		})
	);
});

var version = 'v1::';

self.addEventListener('install', function(event) {
	event.waitUntil(
    	caches.open(version + '-cache').then(function(cache) {
			return cache.addAll(
        	[
				'/',
				'/css/bootstrap.css',
				'/css/main.css',
				'/css/bootstrap-theme.min.css',
				'/css/docs.css',
				'/css/fa-brands.min.css',
				'/css/fa-regular.min.css',
				'/css/fa-solid.min.css',
				'/css/fakeloader.css',
				'/css/flag-icon.min.css',
				'/css/fontawesome-all.min.css',
				'/css/KatawaShoujo.css',
				'/css/lightbox.css',
				'/css/lightslider.min.css',
				'/css/LittleBusters.css',
				'/js/bootstrap.min.js',
				'/js/jquery-3.3.1.min.js',
				'/js/fakeloader.min.js',
				'/js/jcarousel.connected-carousels.js',
				'/js/jcarousel.responsive.js',
				'/js/jquery.jcarousel.min.js',
				'/js/lightbox.js',
				'/js/lightslider.min.js',
				'/js/npm.js',
				'/index.html',
				'/GandBNovels.html',
				'/KatawaShoujo.html',
				'/LittleBusters.html'
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
	if (e.request.cache === 'only-if-cached' && e.request.mode !== 'same-origin') {
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

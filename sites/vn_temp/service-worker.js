self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(cacheName).then(function(cache) {
      return cache.addAll(
        [
          'css/bootstrap.css',
          'css/main.css',
		  'css/bootstrap-theme.min.css',
		  'css/docs.css',
		  'css/fa-brands.min.css',
		  'css/fa-regular.min.css',
		  'css/fa-solid.min.css',
		  'css/fakeloader.css',
		  'css/flag-icon.min.css',
		  'css/fontawesome-all.min.css',
		  'css/KatawaShoujo.css',
		  'css/lightbox.css',
		  'css/lightslider.min.css',
		  'css/LittleBusters.css',
          'js/bootstrap.min.js',
          'js/jquery-3.3.1.min.js',
		  'js/fakeloader.min.js',
		  'js/jcarousel.connected-carousels.js',
		  'js/jcarousel.responsive.js',
		  'js/jquery.jcarousel.min.js',
		  'js/lightbox.js',
		  'js/lightslider.min.js',
		  'js/npm.js',
          'index.html',
		  'GandBNovels.html',
		  'KatawaShoujo.html',
		  'LittleBusters.html'
        ]
      );
    })
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request).then(function(response) {
      return response || fetch(event.request);
    })
  );
});

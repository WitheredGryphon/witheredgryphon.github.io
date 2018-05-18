(function($) {
	$(function() {
		var jcarousel = $('.jcarousel');

		jcarousel
			.on('jcarousel:reload jcarousel:create', function () {
				var carousel = $(this),
					width = carousel.innerWidth();

				if (width >= 1700) {
					width = width / 10;
				} else if (width >= 1500) {
					width = width / 9;
				}
				else if (width >= 1350) {
					width = width / 8;
				}
				else if (width >= 1200) {
					width = width / 7;
				}
				else if (width >= 1050) {
					width = width / 6;
				}
				else if (width >= 900) {
					width = width / 5;
				}
				else if (width >= 750) {
					width = width / 4;
				}
				else if (width >= 540) {
					width = width / 3;
				}
				else if (width >= 330) {
					width = width / 2;
				}

				carousel.jcarousel('items').css('width', Math.ceil(width) + 'px');
			})
		.jcarousel({
			wrap: 'circular'
		});

		$('.jcarousel-control-prev')
			.jcarouselControl({
				target: '-=1'
			});

		$('.jcarousel-control-next')
			.jcarouselControl({
				target: '+=1'
			});

		$('.jcarousel-pagination')
			.on('jcarouselpagination:active', 'a', function() {
				$(this).addClass('active');
			})
			.on('jcarouselpagination:inactive', 'a', function() {
				$(this).removeClass('active');
			})
			.on('click', function(e) {
				e.preventDefault();
			})
			.jcarouselPagination({
				perPage: 1,
				item: function(page) {
					return '<a href="#' + page + '">' + page + '</a>';
				}
			});
	});
})(jQuery);

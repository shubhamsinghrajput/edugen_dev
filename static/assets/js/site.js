$(document).ready(function () {
	$(".menu-btn").click(function () {
		$("#collapsibleNavbar").toggleClass("show");
		$(this).children("i.fa").removeClass("fa-bars").addClass("fa-close");
		var l = $("#collapsibleNavbar").offset().left;
		if (l == 0) {
			$(this).children("i.fa").removeClass("fa-close").addClass("fa-bars");
		}
	});

	$(document).click(function (event) {
		if (!$(event.target).closest("#collapsibleNavbar,.menu-btn").length) {
			$("body").find("#collapsibleNavbar").removeClass("show");
			var l = $("#collapsibleNavbar").offset().left;
			if (l == 0) {
				$("body").find("i.fa").removeClass("fa-close").addClass("fa-bars");
			}
		}
	});

	/*-------------remove "chapter" word form mobile view-----------*/
	var W = $(window).width();
	if (W < 768) {
		$('div.chap-count').text(function (i, t) {
			return t.replace('Chapter', '');
		});
	}
	

});
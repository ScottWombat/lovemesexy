$(document).ready(function() {
	//mobile menu
	$("#mobileMenuToggle").click(function() {
		$(".mobileMenuContent").slideToggle();
	});
	//mega menu
	$(".hasMegaMenu").hover(function() {
		$(this).addClass("active");
		$(this)
			.children(".megaMenu")
			.fadeIn(250);
	});
	$(".hasMegaMenu").mouseleave(function() {
		$(this).removeClass("active");
		$(this)
			.children(".megaMenu")
			.fadeOut(250);
	});
});
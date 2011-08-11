function mailoverlay() {
	
	$(".modalInput").css('display', 'block');
	$(".modal").hide();
	
	var triggers = $(".modalInput").overlay({

		// some mask tweaks suitable for modal dialogs
		mask: {
			color: '#444',
			loadSpeed: 200,
			opacity: 0.9
		},

		closeOnClick: false
	});	
	
}

(function($) {
    $(document).ready(mailoverlay);
})(jQuery);

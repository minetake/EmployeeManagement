(function($) {
	'use strict';
	
	var Sample = function() {
		console.log('Sample');
		app.Common_Cxt.Chk('test');
	};
	
	app.Sample = Sample;
})(app.jQuery);
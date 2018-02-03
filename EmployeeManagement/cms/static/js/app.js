(function(){
	//'use strict';
	
	/**
	 * jQuery
	 */
	var $ = window._app_jQuery || jQuery;
	
	var promises = [];
	
	var init = function(callback) {
	
		console.log('init');
		
		$.when.apply($, promises).done(function(){
			callback();
		});
		
	};
		
	window.app = {
			jQuery : $,
			init : init
	};
	
	
})();
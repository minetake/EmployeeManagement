(function($) {
	
	var SubClass = function(obj) {
		
		obj.textPrint = function() {
			
			console.log("test 2 : " + name);
			
		}		
		
	};
	
	app.SubClass = SubClass;
	
})(app.jQuery);
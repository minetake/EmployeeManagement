(function($) {
	'use strict';
	
	var SuperClass = function() {
		
		var obj = this;
		
		obj._init = function() {
			
			obj.textPrint();
			
		}
		
		var name = "textPrint";
		
		obj.textPrint = function() {
			
			console.log("test 1 : " + name);
			
		}
		
		var context = {
				_init : obj._init,
		};
		
		app.SuperClass_Ctx = context;
			
	};
	
	app.SuperClass = SuperClass; 
	
})(app.jQuery);
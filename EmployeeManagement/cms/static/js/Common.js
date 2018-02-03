(function($) {
	'use strict';
	
	var Common = function() {
		console.log('common read');
		
		var Chk = function(i){
			console.log("chk : " + i);
		};
		
		
		app.Common_Cxt = {
				Chk : Chk
		};
		
		this.name = "first";
		
		this.checking = function(){
			console.log(this.name);
		};
				
	};
	
//	var Second = function() {
//			this.name = "second";
//	};
//		
//	var c = new Common();	
//	c.checking();
//	c.checking.call(new Second());
//		
//	function Dog(){};
//	Dog.prototype.bark = function() {
//		console.log('wan wan');
//	};
//	
//	var dog = new Dog();
//	dog.bark();
	
	app.Common = Common;
	
	
	
	
})(app.jQuery);
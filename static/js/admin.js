window.addEventListener("load", function() {
	// init categories click event
	var buttons = document.getElementsByName("type");
	for (var i=0; i<buttons.length; i++) {
		buttons[i].onchange = function() {
			if (this.value=="product") {
				document.getElementById("sel-categories").removeAttribute("disabled");
				document.getElementById("price").removeAttribute("disabled");
			} else {
				document.getElementById("sel-categories").setAttribute("disabled","");
				document.getElementById("price").setAttribute("disabled","");
			}
		}
	}
	// var edits = document.getElementsByClassName("edit");
	// for (var e=0; e<edits.length; e++) {
	// 	var parent = edits[e].parentElement;
	// 	var name = parent.getElementsByClassName("name").textContent;
	// 	document.get

	// }
});
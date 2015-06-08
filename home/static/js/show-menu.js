function show_menu()
{
	var doc;
	doc = document.getElementsByClassName('menu');
	var n_clase = doc[0].classList.length;
	if (n_clase == 2){
		doc[0].classList.remove("menu-is_active");
		return;
	}
	doc[0].classList.add("menu-is_active");
}
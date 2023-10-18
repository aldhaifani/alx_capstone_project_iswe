/*=============
    Layout 
===============*/

const sidebar_items = document.getElementsByClassName('sidebar_links');
let current_page = '';
if (window.location.href.split('/').length == 4) {
	current_page = window.location.href.split('/').slice(-1)[0];
}

let current_page_sidebar = '';
if (current_page) {
	let current = document.getElementsByClassName('active');
	if (current.length > 0) {
		current[0].className = current[0].className.replace(' active', '');
	}
	current_page_sidebar = document.getElementById(current_page);
	current_page_sidebar.className += ' active';
}

const nav_bar_menu = document.getElementById('menu_bars');
const side_bar = document.getElementById('sidebar');
const nav_bar_menu_bars = document.getElementById('nav_bar_menu_bars');
const nav_bar_menu_x = document.getElementById('nav_bar_menu_x');

nav_bar_menu.addEventListener('click', () => {
	if (nav_bar_menu_bars.style.display == '') {
		side_bar.style.display = 'flex';
		nav_bar_menu_bars.style.display = 'none';
		nav_bar_menu_x.style.display = 'flex';
	} else if (nav_bar_menu_x.style.display == 'flex') {
		side_bar.style.display = 'none';
		nav_bar_menu_bars.style.display = '';
		nav_bar_menu_x.style.display = 'none';
	}
});

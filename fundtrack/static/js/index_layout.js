/*=============
    Layout 
===============*/
let to_select = '';
let current_page_url = window.location.href.split('/');

if (
	current_page_url.slice(-1) == '' ||
	Number.isInteger(current_page_url.slice(-1) * 1)
) {
	to_select = current_page_url.slice(-2, -1);
} else {
	to_select = current_page_url.slice(-1);
}

const to_select_map = {
	assets: 'assets',
	add_assets: 'assets',
	edit_assets: 'assets',
	equity_liability: 'equity_liability',
	add_liability: 'equity_liability',
	edit_liability: 'equity_liability',
	equity_liability: 'equity_liability',
	add_equity: 'equity_liability',
	edit_equity: 'equity_liability',
	reports: 'reports',
};

let current_selected = '';
if (to_select_map[to_select]) {
	let current_selected = document.getElementsByClassName('active');
	if (current_selected.length > 0) {
		current_selected[0].className = current_selected[0].className.replace(
			' active',
			''
		);
	}
	let to_select_page = document.getElementById(to_select_map[to_select]);
	to_select_page.className += ' active';
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

/* ============
		edit db
==============*/
/**
 * deleteEquity - functions that fetches the route
 * to delete a equity instance from the db
 *
 * @param {*} id
 */
function deleteEquity(id) {
	fetch('/delete-equity', {
		method: 'POST',
		body: JSON.stringify({ equityId: id }),
	}).then((_res) => {
		window.location.href = '/equity_liability';
	});
}

/**
 * deleteLiability - functions that fetches the route
 * to delete a liability instance from the db
 *
 * @param {*} id
 */
function deleteLiability(id) {
	fetch('/delete-liability', {
		method: 'POST',
		body: JSON.stringify({ liabilityId: id }),
	}).then((_res) => {
		window.location.href = '/equity_liability';
	});
}

/**
 * deleteAsset - functions that fetches the route
 * to delete a asset instance from the db
 *
 * @param {*} id
 */
function deleteAsset(id) {
	fetch('/delete-asset', {
		method: 'POST',
		body: JSON.stringify({ assetId: id }),
	}).then((_res) => {
		window.location.href = '/assets';
	});
}

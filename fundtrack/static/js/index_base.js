/*
    Global JS script
*/

/*==================
    Form Validation 
==================*/
const form = document.getElementById('form');
const error = document.getElementById('error_msg');

form.addEventListener('submit', (e) => {
	if (!validateEmail() || !validatePassword() || !validateCPassword()) {
		e.preventDefault();
	}
});

/*------------------------
  Password validation 
------------------------*/
/**
 * validatePassword - check for the validity of the used password
 * returns true if the password is valid and false otherwise
 *
 * @return {true, false}
 */
let validatePassword = () => {
	let pswd = document.getElementById('passwd').value;
	if (pswd) {
		if (pswd.length < 8) {
			error.style.display = '';
			error.innerHTML = 'Password must be atleast of 8 characters long';
			return false;
		} else if (!pswd.match(/[a-z]/)) {
			error.style.display = '';
			error.innerHTML = 'Password must contain atleast one lowercase character';
			return false;
		} else if (!pswd.match(/[A-Z]/)) {
			error.style.display = '';
			error.innerHTML = 'Password must contain atleast one uppercase character';
			return false;
		} else if (!pswd.match(/[0-9]/)) {
			error.style.display = '';
			error.innerHTML = 'Password must contain atleast one digit';
			return false;
		} else if (!pswd.match(/[!@#$%^&*]/)) {
			error.style.display = '';
			error.innerHTML =
				'Password must contain atleast one special character (e.g. !@#$%^&*)';
			return false;
		} else {
			return true;
		}
	}
};

/**
 * validateCPassword - checks if the confirm password matches the password
 * returns true if passwords match and false otherwise
 *
 * @return {true, false}
 */
let validateCPassword = () => {
	let pswd = document.getElementById('passwd').value;
	let cpswd = document.getElementById('cpasswd').value;

	if (cpswd !== pswd) {
		error.style.display = '';
		error.innerHTML = 'Passwords must match';
		return false;
	}
	return true;
};

/*-------------------
  Email validation
-------------------*/
/**
 * validateEmail - checks if the provided email is a valid email
 * returns true if the email is valid and false otherwise
 *
 * @return {*}
 */
let validateEmail = () => {
	let email = document.getElementById('email').value;

	if (!email.match(/[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/)) {
		error.style.display = '';
		error.innerHTML = 'Please put a valid email';
		return false;
	}
	return true;
};

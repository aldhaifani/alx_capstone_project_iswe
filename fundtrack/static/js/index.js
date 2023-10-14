/*
    Global JS script
*/

/*==================
    Form Validation 
==================*/
const form = document.getElementById('form');
const error = document.getElementById('error_msg');
const params = new URLSearchParams(window.location.search);

form.addEventListener('submit', (e) => {
  if (!validateEmail() || !validatePassword() || !validateCPassword()) {
    e.preventDefault();
  }
});

/* Password validation */
let validatePassword = () => {
  const pswd = document.getElementById('passwd').value;
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

let validateCPassword = () => {
  const pswd = document.getElementById('passwd').value;
  const cpswd = document.getElementById('cpasswd').value;

  if (cpswd !== pswd) {
    error.style.display = '';
    error.innerHTML = 'Passwords must match';
    return false;
  }
  return true;
};

/* Email validation */
let validateEmail = () => {
  const email = document.getElementById('email').value;

  if (!email.match(/[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/)) {
    error.style.display = '';
    error.innerHTML = 'Please put a valid email';
    return false;
  }
  return true;
};

/* Get query string parameter value 
let query_string_param = function (key) {
  const params = new Proxy(new URLSearchParams(window.location.search), {
    get: (searchParams, prop) => searchParams.get(prop),
  });
  // Get the value of "some_key" in eg "https://example.com/?some_key=some_value"
  return params[key];
}; */

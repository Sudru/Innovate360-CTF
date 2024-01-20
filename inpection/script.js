// script.js
var a = 'aS0zNjB7ZjRrM19mbDQ5fQ';
var flag2 = "0x61 0x6c 0x77 0x61 0x79 0x73 0x5f 0x72 0x65 0x61 0x64 0x5f 0x74 0x68 0x65"
function validateLogin() {
  var username = document.getElementById('username').value;
  var password = document.getElementById('password').value;
  var errorMessage = document.getElementById('error-message');

  // Simple client-side validation to check for certain characters
  var forbiddenChars = /['";]|union|select|from/i;

  if (forbiddenChars.test(username) || forbiddenChars.test(password)) {
    // Decode and display fake flag text for invalid characters
    errorMessage.textContent =  atob(a);
  } else {
    // Clear previous error messages
    errorMessage.textContent = '';

    // Check for a specific username and password
    if (username === 'admin' && password === 'password') {
      // Display success message for admin login
      alert('Login Successful !!\n'+atob(a));
    } else {
        // Display error message for invalid credentials
        alert('Invalid username or password');
      }
    }
  }






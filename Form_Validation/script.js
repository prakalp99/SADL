function validateForm(){
    let isValid = true;
    document.getElementById('emailError').textContent = '';
    document.getElementById('phoneError').textContent = '';
    document.getElementById('passwordError').textContent = '';

    const emailInput = document.getElementById('email').value.trim();
    const phoneInput = document.getElementById('phone').value.trim();
    const passwordInput = document.getElementById('password').value;

    // Email Validation

    const emailPattern = new RegExp(
    "^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,6}$"
    );

    if(!emailInput || !emailPattern.test(emailInput)){
        document.getElementById('emailError').textContent= 'Please enter a valid email address.';
        isValid = false;

    }

    // Phone Validation

    const phonePattern = new RegExp(
    "^\\d{10}$"
    );

    if(!phoneInput || !phonePattern.test(phoneInput)){
        document.getElementById('phoneError').textContent = 'Phone number must be exactly 10 digits';
        isValid = false;


    }

    // Password Validation

    const passwordPattern = new RegExp(
        "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[!@#$%^&*()_+])[A-Za-z\\d!@#$%^&*()_+]{8,}$"

    );
    
    if(!passwordInput){
        document.getElementById('passwordError').textContent = 'Password cannot be empty';
        isValid = false;

    }
    else if(!passwordPattern.test(passwordInput)){
        document.getElementById('passwordError').textContent='Password must be at least 8 characters long and include uppercase, lowercase, speacial characters, and digit';
        isValid = false;

    }

    if(isValid){
        alert("Form Submitted Successfully!");
    }
    return isValid;

}
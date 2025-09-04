/*document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default form submission

        const formData = new FormData(form);

        fetch('/submit_form', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.message === 'Success') {
                alert('Thank you for your submission!');
            } else {
                alert('There was an error submitting the form. Please try again.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('There was an error submitting the form. Please try again.');
        });
    });
});
*/
/*
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default form submission

        const formData = new FormData(form);

        fetch('/submit_form', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            console.log('Response Data:', data);  // Debugging step to see the full response

            if (data.message === 'Success') {
                alert('Thank you for your submission!');
                form.reset();
            } else {
                // If there's an error, ensure the error message is displayed
                alert(data.message || 'There was an error submitting the form. Please try again.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('There was an error submitting the form. Please try again.');
        });
    });
});
*/
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('#contactform'); // Ensure this ID matches
    const submitButton = document.querySelector('#submit'); // Ensure this ID matches

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default form submission

        const formData = new FormData(form);

        fetch('/submit_form', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            console.log('Response Data:', data); // For debugging

            if (data.message === 'Success') {
                alert('Thank you for your submission!');
                form.reset(); // Clear the form fields
                submitButton.disabled = false; // Ensure button is re-enabled
                submitButton.classList.remove('disabled'); // Remove 'disabled' class if it was added
            } else {
                alert(data.message || 'There was an error submitting the form.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('There was an error submitting the form.');
        });
    });
});

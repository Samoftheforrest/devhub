(function() {
    // https://dashboard.emailjs.com/admin/account
    emailjs.init('a8B3AGA56UuueD0HR');
})();

window.onload = function() {
    document.getElementById('contact-form').addEventListener('submit', function(event) {
        event.preventDefault();
        // generate a five digit number for the contact_number variable
        this.contact_number.value = Math.random() * 100000 | 0;
        // these IDs from the previous steps
        emailjs.sendForm('service_sn159ye', 'contact_form', this)
            .then(function() {
                console.log('SUCCESS!');
                // reset form
                let email = document.getElementById('email');
                let subject = document.getElementById('subject');
                let message = document.getElementById('message');
                email.textContent == '';
                subject.textContent == '';
                message.textContent == '';
            }, function(error) {
                console.log('FAILED...', error);
            });
    });
}
(() => emailjs.init('a8B3AGA56UuueD0HR'))();

const formElementsList = ['email', 'subject', 'message'];

window.onload = function() {
    document.getElementById('contact-form').addEventListener('submit', function(event) {
        event.preventDefault();
        if (!this.email.value || !this.subject.value || !this.message.value) return;
        // generate a five digit number for the contact_number variable
        this.contact_number.value = Math.random() * 100000 | 0;
        // these IDs from the previous steps
        emailjs.sendForm('service_sn159ye', 'contact_form', this)
            .then(function() {
                console.log('SUCCESS!');
            }, function(error) {
                console.log('FAILED...', error);
            });
    });
};
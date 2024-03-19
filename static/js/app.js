// // This will hide the message after 5 seconds. You can change the time by changing the `5000` to any other value in milliseconds.

message_timeout = document.getElementById('message-timer');

if (message_timeout) {
    setTimeout(function() {
        message_timeout.style.display = 'none';
    }, 5000);
}
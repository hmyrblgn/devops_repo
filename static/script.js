document.getElementById('notificationForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const userId = document.getElementById('userId').value;
    const message = document.getElementById('message').value;

    fetch('/notifications', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ userId, message }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = data.message;
        document.getElementById('notificationForm').reset();
    })
    .catch(error => console.error('Error:', error));
});

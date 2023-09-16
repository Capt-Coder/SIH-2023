function updateDate() {
    const dateElement = document.getElementById('date');
    const now = new Date();

    const day = now.getDate();
    const month = now.toLocaleString('default', { month: 'long' });
    const year = now.getFullYear();

    const formattedDate = `${day} ${month}, ${year}`;

    dateElement.textContent = formattedDate;
}
updateDate();
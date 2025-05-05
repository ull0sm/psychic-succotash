document.addEventListener('DOMContentLoaded', () => {
    const subject = sessionStorage.getItem('selectedQuiz') || 'DBMS'; // Default to DBMS
    fetchLeaderboard(subject);
});

function fetchLeaderboard(subject) {
    fetch(`/leaderboard/${subject}`)
        .then(response => response.json())
        .then(data => {
            const leaderboardContainer = document.getElementById('leaderboard-data');
            leaderboardContainer.innerHTML = '';
            data.forEach((entry, index) => {
                const row = `
                    <tr>
                        <td>${index + 1}</td>
                        <td>${entry.name}</td>
                        <td>${entry.score}</td>
                    </tr>
                `;
                leaderboardContainer.innerHTML += row;
            });
        })
        .catch(error => console.error('Error fetching leaderboard data:', error));
}
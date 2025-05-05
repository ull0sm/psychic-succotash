// Fetch student data for the teacher dashboard
function fetchStudentData() {
    fetch('/teacher/students')
        .then(response => response.json())
        .then(data => {
            const studentDataContainer = document.getElementById('student-data');
            studentDataContainer.innerHTML = '';
            data.forEach(student => {
                const row = `
                    <tr>
                        <td>${student.name}</td>
                        <td>${student.subject}</td>
                        <td>${student.score}</td>
                    </tr>
                `;
                studentDataContainer.innerHTML += row;
            });
        })
        .catch(error => console.error('Error fetching student data:', error));
}
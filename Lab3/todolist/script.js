function addTask() {
    const taskInput = document.getElementById('new-task');
    const tasksList = document.getElementById('tasks-list');
    const taskText = taskInput.value.trim();

    if (taskText) {
        const listItem = document.createElement('li');
        listItem.innerHTML = `
            <input type="checkbox" onclick="toggleDone(this)">
            <span>${taskText}</span>
            <button class="delete-btn" onclick="deleteTask(this)">Delete</button>
        `;
        tasksList.appendChild(listItem);
        taskInput.value = '';
    }
}

function toggleDone(checkbox) {
    if (checkbox.checked) {
        checkbox.parentElement.classList.add('done');
    } else {
        checkbox.parentElement.classList.remove('done');
    }
}

function deleteTask(button) {
    button.parentElement.remove();
}


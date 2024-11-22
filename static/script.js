
// Fetch the to-do items from the server and populate the list
fetch('/show')
    .then(response => response.json())
    .then(toDos => {
        const todoListElement = document.getElementById('todo-list');
        todoListElement.innerHTML = ''; // Clear current list

        for (let name in toDos) {
            let listItem = document.createElement('li');
            listItem.className = 'todo-item';
            listItem.textContent = name;
            listItem.dataset.state = 'name'; // Initial state is name

            listItem.onclick = () => {
                if (listItem.dataset.state === 'name') {
                    listItem.textContent = toDos[name];
                    listItem.dataset.state = 'desc';
                } else {
                    listItem.textContent = name;
                    listItem.dataset.state = 'name';
                }
            };

            todoListElement.appendChild(listItem);
        }
    })
    .catch(error => console.error('Error fetching to-dos:', error));
const tg = window.Telegram.WebApp;

const departments = [
    {
        name: "Sales",
        employees: ["Alice", "Bob", "Charlie"]
    },
    {
        name: "Engineering",
        employees: ["Dave", "Eve", "Frank"]
    },
    {
        name: "HR",
        employees: ["Grace", "Heidi", "Ivan"]
    }
];

function createMenu(data) {
    const menu = document.getElementById('menu');

    data.forEach(department => {
        const departmentItem = document.createElement('li');
        const triangle = document.createElement('span');
        triangle.className = 'triangle';
        triangle.textContent = '\u25B6'; // Unicode for a right-pointing triangle

        const departmentName = document.createElement('span');
        departmentName.textContent = department.name;

        const employeeList = document.createElement('ul');
        employeeList.className = 'hidden';
        department.employees.forEach(employee => {
            const employeeItem = document.createElement('li');
            employeeItem.textContent = employee;

            // Send data on employee click
            employeeItem.addEventListener('click', (event) => {
                event.stopPropagation();
                tg.sendData(JSON.stringify({ department: department.name, employee }));
            });

            employeeList.appendChild(employeeItem);
        });

        departmentItem.appendChild(triangle);
        departmentItem.appendChild(departmentName);
        departmentItem.appendChild(employeeList);
        menu.appendChild(departmentItem);

        // Toggle employee list on click
        departmentItem.addEventListener('click', () => {
            const isHidden = employeeList.classList.contains('hidden');
            employeeList.classList.toggle('hidden', !isHidden);
            triangle.classList.toggle('expanded', isHidden);
        });
    });
}

createMenu(departments);

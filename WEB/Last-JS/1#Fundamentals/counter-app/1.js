let countEl = document.getElementById("count-el");
let saveEl = document.getElementById("save-el");

let count = 0;

function increment() {
    count += 1;
    countEl.textContent = count;
}

function decrement() {
    count -= 1;
    countEl.textContent = count;
}

function save() {
    let el = `${count} - `;
    saveEl.textContent += el;
    count = 0;
    countEl.textContent = count;
}
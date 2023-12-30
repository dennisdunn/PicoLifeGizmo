const CELLS_W = 16;
const CELLS_H = 7;

function toRowMajor(cell) {
    return cell.y * CELLS_W + cell.x;
}

function fromRowMajor(idx) {
    return {
        x: idx % CELLS_W,
        y: Math.floor(idx / CELLS_W)
    }
}

function createEditor() {
    const cells = document.querySelector('.editor');
    for (let y = 0; y < CELLS_H; y++) {
        const row = document.createElement('div');
        row.className = 'row';
        for (let x = 0; x < CELLS_W; x++) {
            const button = document.createElement('input');
            button.type = 'checkbox';
            button.dataset.idx = toRowMajor({ x, y })
            row.appendChild(button);
        }
        cells.appendChild(row);
    }
}

function createNavbar() {
    const nav = document.querySelector('nav .patterns');
    for (let key in patterns) {
        const button = document.createElement('a');
        button.onclick = ()=>loadEditor(key);
        button.innerText = key;
        nav.appendChild(button);
    }
}

function clearEditor() {
    const buttons = document.querySelectorAll('.editor input');
    for (let button of buttons) {
        button.checked = false;
    }
}

function uploadEditor() {
    const cells = readEditor();
    console.log(cells);
}

function readEditor() {
    const cells = [];
    const buttons = document.querySelectorAll('.editor input');
    for (let button of buttons) {
        if (button.checked) {
            cells.push(fromRowMajor(JSON.parse(button.dataset.idx)));
        }
    }
    return cells;
}

function setEditor(cells) {
    clearEditor();
    for (let cell of cells) {
        const idx = toRowMajor(cell);
        const button = document.querySelector(`.editor input[data-idx="${idx}"]`);
        button.checked = true;
    }
}

function loadEditor(name) {
    const cells = patterns[name];
    setEditor(cells);
}

const patterns = {
    "Blinkers": [
        { "x": 9, "y": 1 },
        { "x": 10, "y": 1 },
        { "x": 11, "y": 1 },
        { "x": 1, "y": 2 },
        { "x": 6, "y": 2 },
        { "x": 1, "y": 3 },
        { "x": 6, "y": 3 },
        { "x": 1, "y": 4 },
        { "x": 6, "y": 4 },
        { "x": 11, "y": 5 },
        { "x": 12, "y": 5 },
        { "x": 13, "y": 5 }
    ],
    "Blocks": [
        { "x": 1, "y": 1 },
        { "x": 2, "y": 1 },
        { "x": 1, "y": 2 },
        { "x": 2, "y": 2 },
        { "x": 5, "y": 3 },
        { "x": 6, "y": 3 },
        { "x": 10, "y": 3 },
        { "x": 11, "y": 3 },
        { "x": 5, "y": 4 },
        { "x": 6, "y": 4 },
        { "x": 10, "y": 4 },
        { "x": 11, "y": 4 },
        { "x": 14, "y": 5 },
        { "x": 15, "y": 5 },
        { "x": 14, "y": 6 },
        { "x": 15, "y": 6 }
    ],
    "Toad": [
        { "x": 5, "y": 2 },
        { "x": 6, "y": 2 },
        { "x": 7, "y": 2 },
        { "x": 6, "y": 3 },
        { "x": 7, "y": 3 },
        { "x": 8, "y": 3 }
    ],
    "Beacon": [
        { "x": 5, "y": 2 },
        { "x": 6, "y": 2 },
        { "x": 5, "y": 3 },
        { "x": 8, "y": 4 },
        { "x": 7, "y": 5 },
        { "x": 8, "y": 5 }
    ],
    "Glider": [
        { "x": 2, "y": 0 },
        { "x": 3, "y": 1 },
        { "x": 1, "y": 2 },
        { "x": 2, "y": 2 },
        { "x": 3, "y": 2 }
    ]
}
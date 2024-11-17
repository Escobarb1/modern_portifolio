function Player(name, marker) {
    this.name = name;
    this.marker = marker;
    this.sayName = function() {
        console.log(this.name);
    };
  }

const player1 = new Player('steve', 'X');
const player2 = new Player('also steve', '0');
player1.sayName(); // 'steve'
player2.sayName();

function Book()
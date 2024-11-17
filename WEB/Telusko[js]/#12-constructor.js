function Alien(name, tech){
    this.name = name;
    this.tech = tech;

    this.work = function(){
        console.log("Solving bugs from 12 hrs");
    }

    return 7;
}

let alien1 = new Alien('Ernest', 'JS');
let alien2 = new Alien('Goodluck', 'Java');

alien1.tech = 'Blockchain';

console.log(alien1);
console.log(alien2);


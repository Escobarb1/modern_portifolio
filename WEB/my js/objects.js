class car {
    constructor(make, model, year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }   

    print() {
        console.log(`${this.make} ${this.model} (${this.year})`);
    }
}

let myCar = new car('BMW', '7451i', 2010);
myCar.print();


class SportsCar extends car{
    revEngine() {
        console.log('Virrow goes the ' + this.model);
    }
}

let mySportsCar = new SportsCar('dodge', 'viper', 2011);
mySportsCar.print();
mySportsCar.revEngine();

// myCar.revEngine();

class GameCar extends car{

}

let myGameCar = new GameCar('venza', 'scalet', 2015);
myGameCar.print();
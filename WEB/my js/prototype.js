let originalCar = {
    make: 'bow',
    model: '7451i',
    year: 2010
};

let newCar = Object.create(originalCar);
console.log(newCar.make);

console.log(Object.getPrototypeOf(newCar));

let myPrototype = Object.getPrototypeOf(newCar);
console.log(myPrototype.make);

originalCar.doors = 4;
console.log(newCar.doors);

console.log(originalCar.hasOwnProperty('doors'));
console.log(newCar.hasOwnProperty('doors'));

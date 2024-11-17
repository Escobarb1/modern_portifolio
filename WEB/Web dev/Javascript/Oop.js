//Functional programming

// var shoes = 100;
// var stateTax = 1.2;

// function totalPrice(shoes, stateTax) {
//     return shoes * stateTax;
// }
// var toPay = totalPrice(shoes, stateTax);
// console.log(toPay);



// OOP

// var purchase1 = {
//     shoes : 100,
//     stateTax : 1.2,
//     totalPrice : function() {
//         var calculation = purchase1.shoes * purchase1.stateTax;
//         console.log('Total price:', calculation);
//     }
// }

// purchase1.totalPrice();


// var purchase2 = {
//     shoes : 50,
//     stateTax : 1.2,
//     totalPrice : function() {
//         var calculation = purchase2.shoes * purchase2.stateTax;
//         console.log('Total price:', calculation);
//     }
// }
// purchase2.totalPrice()

// OOP This keyword

// var purchase1 = {
//     shoes : 100,
//     stateTax : 1.2,
//     totalPrice : function() {
//         var calculation = this.shoes * this.stateTax;
//         console.log('Total price:', calculation);
//     }
// }

// purchase1.totalPrice();


// var purchase2 = {
//     shoes : 50,
//     stateTax : 1.2,
//     totalPrice : function() {
//         var calculation = this.shoes * this.stateTax;
//         console.log('Total price:', calculation);
//     }
// }
// purchase2.totalPrice()



// const bicycle = {
//     bell: function() {
//         return "Ring, ring! Watch out, please!"
//     }
// }
// const door = {
//     bell: function() {
//         return "Ring, ring! Come here, please!"
//     }
// }
// bicycle.bell(); // "Get away, please"



class Bird {
    useWings() {
        console.log("Flying!")
    }
}
class Eagle extends Bird {
    useWings() {
        super.useWings()
        console.log("Barely flapping!")
    }
}
class Penguin extends Bird {
    useWings() {
        console.log("Diving!")
    }
}
var baldEagle = new Eagle();
var kingPenguin = new Penguin();
baldEagle.useWings(); // "Flying! Barely flapping!"
kingPenguin.useWings(); // "Diving!"

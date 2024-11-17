// const colors = ['red','orange','yellow']
// for (var color of colors) {
//     console.log(color);
// }


// // Object.keys()
// const car2 = {
//     speed : 200,
//     color : 'red'
// }
// console.log(Object.keys(car2));



// // Object.values
// const car3 = {
//     speed: 300,
//     color: "yellow"
// }
// console.log(Object.values(car3)); // [300, 'yellow']


// // Object.entries
// const car4 = {
//     speed: 400,
//     color: 'magenta'
// }
// console.log(Object.entries(car4));




// var clothingItem = {
//     price: 50,
//     color: 'beige',
//     material: 'cotton',
//     season: 'autumn'
// }

// for( const key of Object.keys(clothingItem) ) {
//     console.log(key, ":", clothingItem[key])
// }





// var family = {
//     stranger : 'Peace',
//     Evans : 'Kelechi',
//     Escobar : 'Chinonso',
//     Ezeh : 'Goodluck'    
// }
// for(const key of Object.keys(family)) {
//     console.log(key, ':', family[key]);
// }



// function testBracketsDynamicAccess() {
//     var dynamicKey;
//     if(Math.random() > 0.5) {
//       dynamicKey = "speed";
//      }else{
//        dynamicKey = "color";
//      }
  
//       var drone = {
//         speed: 15,
//         color: "orange"
//       }
  
//       console.log(drone[dynamicKey]);
//   }
//   testBracketsDynamicAccess();


const car = {
    engine : true
}
const sportsCar = Object.create(car);
sportsCar.speed = 'fast';
console.log("The sportcar object: ", sportsCar);                            

for(prop in sportsCar) {
    console.log(prop);
}

for(prop of Object.keys(sportsCar)) {

    console.log(prop + ": " + sportsCar[prop]);
}
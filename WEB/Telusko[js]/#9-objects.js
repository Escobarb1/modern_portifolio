// // // object literals

// let alien = {
//     name: "Ernest",
//     tech: "JS",
//     'work experience': 4
// }

// // console.log(alien.name);
// console.log(alien['work experience']);




// let alien = {
//     name : 'Ernest',
//     tech : 'JS',
//     laptop : {
//         cpu : "i7",
//         ram : 4,
//         brand1: 'Asus'
//     }
// }


// console.log(alien?.laptop?.brand?.length);

// delete alien.laptop
// console.log(alien);






let alien = {
    name : 'Ernest',
    tech : 'JS',
    laptop : {
        cpu : "i7",
        ram : 4,
        brand1: 'Asus'
    }
}

for(let key in alien.laptop) {
    console.log(key, alien.laptop[key]);
}



// For loop


// for(var i=0; i<101; i++){
//     console.log(i);
// }

// for(var i = 1   ; i <= 3; i++){
//     console.log(i);
// }
// console.log('Go');



// while loop

// var counter = 1;
// while(counter <= 10){
//     console.log(counter);
//     counter++;
// }
// console.log("Happy coding");    


// Nested loops

// for(var i = 2024; i < 2026; i++){
//     console.log(i);
//     for(var j = 6; j < 9; j++){
//         console.log(".............", j);
//     }
// }


// for(var i = 0; i < 11; i++){
//     for(var j = 0; j < 11; j++){
//         console.log(i + ' x ' + j + ' = ' + i * j);
//     }
// }





for(var i = 1; i < 11; i++){
    if(i == 1){
        console.log("Gold medal");
    } else if(i == 2){
        console.log("Silver medal");
    } else if(i == 3){
        console.log("Bronze medal")
    } else{
        console.log(i);
    }
}



for(var i = 1; i < 11; i++){
    switch(i){
        case 1:
            console.log('Gold medal');
            break;
        case 2:
            console.log('Silver medal');
            break;
        case 3:
            console.log('Bronze medal');
            break;
        default:
            console.log(i);
    }
}



for (i = 0; i < 2; i++) {
    for (var j = 0; j < 3; j++) {
        console.log("Hello");
    }
}

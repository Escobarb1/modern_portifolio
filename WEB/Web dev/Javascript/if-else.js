// if else

// var result = 5;
// if(result > 40){
//     console.log("You passed the test");
// } else{
//     console.log("You have not passed the test");
// }



// switch statement 

var place = 'first';
switch(place) {
    case 'first':
        console.log('Gold');
        break;
    case 'second':
        console.log('Silver');
        break;
    case 'third':
        console.log('Bronze');
        break;
    default:
        console.log('No medal');
}






var age = 100;
if(age >= 65){
    console.log("You get your income from your pension");
} else if(age < 65 && age >= 18){
    console.log("Each month you get a salary");
} else if(age < 18){
    console.log("You get an allowance");
} else{
    console.log("The value of the age variable is not numerical");
}




var day = 'Sunday';
switch(day) {
   case 'Monday':
       console.log('Read a book');
       break;
   case 'Tuesday':
       console.log('Watch a movie');
       break;
   case 'Wednesday':
       console.log('Read a book');
       break;
   case 'Thursday':
       console.log('Play basketball');
       break;
   case 'Friday':
       console.log('Socialize');
       break;
   case 'Saturday':
       console.log('Chill');
       break;
   case 'Sunday':
       console.log('Have barbecue');
       break;
   default:
       //this block will run if no condition matches
       console.log('There is no such day');
}
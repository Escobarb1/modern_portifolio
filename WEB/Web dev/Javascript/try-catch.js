// console.log(a + b);
// console.log("This line is never reached");

//throw new ReferenceError();




// try{
    //     console.log(a + b);
    // } catch(err){
        //     // console.log(err)
        //     console.log("There was an error");
        //     console.log("The error was saved in the error log");
        // }   
        // console.log("My program does not stop");
        
// try{            
//     throw new ReferenceError();
//     } catch(err){
//         // console.log(err)
//         console.log("There was a ReferenceError");
//     }
// console.log("My program does not stop");


// try{
// console.log(username);
// } catch(err) {
//     // console.log(err);
//     console.log("detected an error");
// }




// function addTwoNums(a, b){
//     try{
//         if(typeof(a) != 'number'){
//             throw new ReferenceError('the first argument is not a number');
//         } else if(typeof(b) != 'number'){
//             throw new ReferenceError('the second argument is not a number');
//         } else{
//             console.log(a + b);
//         }
//     }catch(err) {
//         console.log("Error!", err);    
//     }
// }
// addTwoNums(5, "5");
// console.log("It still works");



// function addTwoNums(a,b) {
//     try {
//         if(typeof(a) != 'number') {
//             throw new ReferenceError('the first argument is not a number')
//         } else if (typeof(b) != 'number') {
//             throw new ReferenceError('the second argument is not a number')
//         } else {
//             console.log(a + b)
//         }
//     } catch(err) {
//         console.log("Error!", err)
//     }
// }
// addTwoNums(5, "5")
// console.log("It still works")





// function letterFinder(word, match) {
//     var conditional = typeof(word) == 'string' && word.length >= 2;
//     var condition2 = typeof(match) == 'string' && match.length === 1;
//     if(conditional == true && condition2 == true){

//         for(var i = 0; i < word.length; i++) {
//             if(word[i] == match) {
//                 //if the current character at position i in the word is equal to the match
//                 console.log('Found the', match, 'at', i)
//             } else {
//                 console.log('---No match found at', i)
//             }
//         } 
//     } else{
//         console.log("Please pass correct arguments to the function.");
//     }
// }
// letterFinder("car", "c");




// function letterFinder(word, match) {
//     var condition1 = typeof(word) == 'string' && word.length >= 2; //if the word is a string and the length is greater than or equal to 2
//     var condition2 = typeof(match) == 'string' && match.length == 1; //if the match is a string and the length is equal to 1
//     if(condition1 && condition2) { //if both condition matches
//         for(var i = 0; i < word.length; i++) {
//             if(word[i] == match) {
//                 //check if the character at this i position in the word is equal to the match
//                 console.log('Found the', match, 'at', i)
//             } else {
//                 console.log('---No match found at', i)
//             }
//         }
//     } else {
//         //if the requirements don't match
//         console.log("Please pass correct arguments to the function")
//     }
// }
// letterFinder([],[])
// letterFinder("cat","c")








var result = null;
console.log(result);


try {
    console.log('Hello');
  } catch(err) {
    console.log('Goodbye');
  }
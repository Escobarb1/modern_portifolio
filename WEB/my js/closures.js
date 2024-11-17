function sayHello(name) {
    return function() {
        console.log('howdy ' + name);
    }
}

let bob = sayHello('bob');
let conrad = sayHello('Goodluck');
let grant = sayHello('grant');

grant();
conrad();
bob();
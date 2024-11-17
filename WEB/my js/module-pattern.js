var counter = (function() {

    //private stuff
    let count = 0;

    function print(message){
        console.log(message + '----' + count);
    }

    //return an object
    return{
        value: count,
        get: function() { return count; },

        set: function(value) { count = value; },

        increament: function() {
            count += 1;
            print('After increament: ');
        },

        reset: function() {
            print('Before reset: ');
            count = 0;
            print('After reset: ');
        }
    }

})();

// console.log(counter.count);

counter.increament();
counter.increament();
counter.increament();


// console.log(counter.value);

counter.set(7);
console.log(counter.get());

counter.reset();
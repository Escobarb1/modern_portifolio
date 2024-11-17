// let halley = {
//     _name : 'Halley', 
//     _behavior : 0,

//     get name() {
//         return this._name;
//     },

//     get behavior() {
//         return this._behavior;
//     },

//     incrementBehavior() {
//         this._behavior++;
//     }
// }




//////////////////////////// / class


// class Dog {
//     constructor(name) {
//       this.name = name;
//       this.behavior = 0;
//     } 
//   }
  
//   const halley = new Dog('Halley'); // Create new Dog instance
//   console.log(halley.name); // Log the name value saved to halley
//   // Output: 'Halley'





// class Surgeon {
// constructor(name, department) {
//     this.name = name;
//     this.department = department;
// }
// }

// const surgeonRomero = new Surgeon('Francisco Romero', 'Cardiovascular');
// const surgeonJackson = new Surgeon('Ruth Jackson', 'Orthopedics');
// console.log(surgeonRomero.department);








/////////////// method

class Dog {
    constructor(name) {
      this._name = name;
      this._behavior = 0;
    }
      
    get name() {
      return this._name;
    }
    
    get behavior() {
      return this._behavior;
    }
    
    incrementBehavior() {
      this._behavior++;
    }
  }










  class Surgeon {
    constructor(name, department) {
      this._name = name;
      this._department = department;
      this._remainingVacationDays = 20;
    }
    
    get name() {
      return this._name;
    }
    
    get department() {
      return this._department;
    }
    
    get remainingVacationDays() {
      return this._remainingVacationDays;
    }
    
    takeVacationDays(daysOff) {
      this._remainingVacationDays -= daysOff;
    }
  }
  
  const surgeonRomero = new Surgeon('Francisco Romero', 'Cardiovascular');
  const surgeonJackson = new Surgeon('Ruth Jackson', 'Orthopedics');
  
  console.log(surgeonRomero.name);
  surgeonRomero.takeVacationDays(3);
  console.log(surgeonRomero.remainingVacationDays);
  








  class Surgeon {
    constructor(name, department) {
      this._name = name;
      this._department = department;
      this._remainingVacationDays = 20;
    }
    get name() {
      return this._name;
    }
  
    get department() {
      return this._department;
    }
  
    get remainingVacationDays() {
      return this._remainingVacationDays; 
    }
  
    takeVacationDays(daysOff) {
      this._remainingVacationDays -= daysOff;
    }
  }
  
  const surgeonRomero = new Surgeon('Francisco Romero', 'Cardiovascular');
  const surgeonJackson = new Surgeon('Ruth Jackson', 'Orthopedics');
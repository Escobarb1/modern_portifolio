// class Dog {
//     constructor(name) {
//       this.name = name;
//       this.behavior = 0;
//     } 
//   }
  
//   const halley = new Dog('Halley'); // Create new Dog instance
//   console.log(halley.name); // Log the name value saved to halley
//   // Output: 'Halley'
//   const ernest = new Dog('Ernest');
//   console.log(ernest.name);





// //   CLASSES
// //   Methods
  



//   class Surgeon {
//     constructor(name, department) {
//       this._name = name;
//       this._department = department;
//       this._remainingVacationDays = 20;
//     }
//     get name() {
//       return this._name;
//     }
  
//     get department() {
//       return this._department;
//     }
  
//     get remainingVacationDays() {
//       return this._remainingVacationDays; 
//     }
  
//     takeVacationDays(daysOff) {
//       this._remainingVacationDays -= daysOff;
//     }
//   }
  
//   const surgeonRomero = new Surgeon('Francisco Romero', 'Cardiovascular');
//   const surgeonJackson = new Surgeon('Ruth Jackson', 'Orthopedics');
//   console.log(surgeonJackson.name + surgeonJackson.remainingVacationDays);









// //   Method Calls


//   class Surgeon {
//     constructor(name, department) {
//       this._name = name;
//       this._department = department;
//       this._remainingVacationDays = 20;
//     }
    
//     get name() {
//       return this._name;
//     }
    
//     get department() {
//       return this._department;
//     }
    
//     get remainingVacationDays() {
//       return this._remainingVacationDays;
//     }
    
//     takeVacationDays(daysOff) {
//       this._remainingVacationDays -= daysOff;
//     }
//   }
  
//   const surgeonRomero = new Surgeon('Francisco Romero', 'Cardiovascular');
//   const surgeonJackson = new Surgeon('Ruth Jackson', 'Orthopedics');
  
//   console.log(surgeonRomero.name);
//   surgeonRomero.takeVacationDays(3);
//   console.log(surgeonRomero.remainingVacationDays);
  








// Inheritance

//   class HospitalEmployee {
//     constructor(name) {
//       this._name = name;
//       this._remainingVacationDays = 20;
//     }
    
//     get name() {
//       return this._name;
//     }
    
//     get remainingVacationDays() {
//       return this._remainingVacationDays;
//     }
    
//     takeVacationDays(daysOff) {
//       this._remainingVacationDays -= daysOff;
//     }
//   }
  
  
//   class Nurse extends HospitalEmployee {
//     constructor(name, certifications) {
//       super(name);
//       this._certifications = certifications;
//     }
//   }
  
//   const nurseOlynyk = new Nurse('Olynyk', ['Trauma', 'Pediatrics']);
//   console.log(nurseOlynyk.name);
















  class HospitalEmployee {
    constructor(name) {
      this._name = name;
      this._remainingVacationDays = 20;
    }
    
    get name() {
      return this._name;
    }
    
    get remainingVacationDays() {
      return this._remainingVacationDays;
    }
    
    takeVacationDays(daysOff) {
      this._remainingVacationDays -= daysOff;
    }
  }
  
  class Nurse extends HospitalEmployee {
   constructor(name, certifications) {
     super(name);
     this._certifications = certifications;
   } 
  }
  
  const nurseOlynyk = new Nurse('Olynyk', ['Trauma','Pediatrics']);
  console.log(nurseOlynyk.takeVacationDays(5));
  console.log(nurseOlynyk.remainingVacationDays)
  
  






  class HospitalEmployee {
    constructor(name) {
      this._name = name;
      this._remainingVacationDays = 20;
    }
    
    get name() {
      return this._name;
    }
    
    get remainingVacationDays() {
      return this._remainingVacationDays;
    }
    
    takeVacationDays(daysOff) {
      this._remainingVacationDays -= daysOff;
    }
  }
  
  class Nurse extends HospitalEmployee {
    constructor(name, certifications) {
      super(name);
      this._certifications = certifications;
    } 
    
    get certifications() {
      return this._certifications;
    }
    
    addCertification(newCertification) {
      this._certifications.push(newCertification);
    }
  }
  
  const nurseOlynyk = new Nurse('Olynyk', ['Trauma','Pediatrics']);
  nurseOlynyk.takeVacationDays(5);
  console.log(nurseOlynyk.remainingVacationDays);
  nurseOlynyk.addCertification('Genetics');
  console.log(nurseOlynyk.certifications);


  
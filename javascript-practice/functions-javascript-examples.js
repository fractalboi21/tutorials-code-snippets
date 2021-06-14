//function declarations
function funcName(a,b) {
  return a*b;
}

//function expressions
const x = function(a,b) {return a*b}

//function invoction
The Global Object
let x = myFunction();            // x will be the window object

function myFunction() {
  return this;
}


//Invoking a Function as a Method
 const myObject = {
  firstName:"John",
  lastName: "Doe",
  fullName: function () {
    return this.firstName + " " + this.lastName;
  }
}
myObject.fullName();         // Will return "John Doe" 

//Invoking a Function with a Function Constructor
// This is a function constructor:
function myFunction(arg1, arg2) {
  this.firstName = arg1;
  this.lastName  = arg2;
}

// This creates a new object
const myObj = new myFunction("John", "Doe");

// This will return "John"
myObj.firstName;

//The JavaScript call() Method
const person = {
  fullName: function() {
    return this.firstName + " " + this.lastName;
  }
}
const person1 = {
  firstName:"John",
  lastName: "Doe"
}
const person2 = {
  firstName:"Mary",
  lastName: "Doe"
}

// This will return "John Doe":
person.fullName.call(person1);

//The call() Method with Arguments
const person = {
  fullName: function(city, country) {
    return this.firstName + " " + this.lastName + "," + city + "," + country;
  }
}

const person1 = {
  firstName:"John",
  lastName: "Doe"
}

person.fullName.call(person1, "Oslo", "Norway");



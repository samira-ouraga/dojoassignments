// function onlyPrintNumbers(arr){
//     var newArr = [];
//         for (var i=0; i<=arr.length; i++){
//             if (typeof arr[i] === "number" ){
//                 newArr.push(arr[i]);
//                 console.log(newArr);
            
//             }
//         }
        
// }
// onlyPrintNumbers([23, "my", 3, "name", 8, 56]);

var dojo = {};                                 // creates an empty object
dojo = {
  name: 'Coding Dojo',                         // property can store a string
  number_of_students: 25,                      // property can store a number
  instructors: ['Andrew', 'Michael', 'Jay'],   // property can store arrays
  location: {                                  // property can even store another object!
    city: 'San Jose',
    state: 'CA',
    zipcode: 95112
  }
}                                              // access object properties with dot (.) notation
console.log(dojo.name, dojo.number_of_students, dojo.instructors, dojo.location);
console.log(dojo["name"]);                     // or bracket [] notation (note: specify key in quotes)
dojo.snacks = ['Fig Bars', 'Bagels', 'Popcorn', 'Apples']; //to add new key:value to object
console.log(dojo.snacks);

dojo.number_of_students = 40;         // to update values
dojo.location.city = "Bellevue";
dojo.location.state = "Washington";
dojo.location.zipcode = "unknown";

console.log(dojo.location.city);
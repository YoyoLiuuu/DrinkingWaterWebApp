



// Check today is which date of the week  0-6 for sunday to saturday
const today = new Date();
let str = "d"+ today.getDay().toString();
let d = document.getElementById(str);


// console.log(data)
// Obtain today water level
var data= JSON.parse('{{ tracking | safe }}')
console.log(data)
// d.innerHTML = "HELLO";
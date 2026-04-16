function sum(a,b){
    return a+b;
}
let ans =sum(2,3);
console.log(ans);

function nSum(n){
    let ans=n;
    for (let i=0; i<n; i++){
   ans =ans+i;
    }
    return ans;
}
 let res =nSum(5);
 console.log(res);
 
function greet (name){
    return "hello,"+name ;
}

let message =greet("firoz");
console.log(message);
 

let users =[
    {
        name : "firoz",
        age : 28,
        cities: ["ongole","hyderabad","bangalore", {
            villages: ["maddiralapadu","kondapuram"]
        }],
        player : true,


    }
]
console.log(users[0].cities[3].villages[1]);

function factorial(n){
    if (n==0 || n==1){
        return 1;
    }
    else{
        return n*factorial(n-1);
    }
}
let fact = factorial(5);
console.log(fact);


console.log("Start");

setTimeout(() => {
  console.log("Async task done");
}, 2000);

console.log("End");

let fs = require("fs");
let readmew = fs.readFileSync("grid.html","utf8");
console.log(readmew);
console.log("after the readfile ");


// let read1=fs.readFile("grid.html","utf8");
// console.log(read1);
// let read2 =fs.readFile("firoz.html","utf8");
// console.log(read2);

// let read3 =fs.readFile("grid.html","utf8");
// console.log("readding after ");
 

let read1 =fs.readFile("grid.html","utf8",(err, data)=>{
    if (err) console.log("first");
    console.log("1");

});
let read2 =fs.readFile("firoz.html","utf8",(err, data)=>{
    if (err) console.log("second");
    console.log("2");  

});
let read3 =fs.readFile("grid.html","utf8",(err, data)=>{
    if (err) console.log("third");
    console.log("3");  

});


console.log ("first hi");

setTimeout(() => {
    console.log("second hi");
}, 15000);

console.log("third hi");
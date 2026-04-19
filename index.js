// function sum(a,b){
//     return a+b;
// }
// let ans =sum(2,3);
// console.log(ans);

// function nSum(n){
//     let ans=n;
//     for (let i=0; i<n; i++){
//    ans =ans+i;
//     }
//     return ans;
// }
//  let res =nSum(5);
//  console.log(res);
 
// function greet (name){
//     return "hello,"+name ;
// }

// let message =greet("firoz");
// console.log(message);
 

// let users =[
//     {
//         name : "firoz",
//         age : 28,
//         cities: ["ongole","hyderabad","bangalore", {
//             villages: ["maddiralapadu","kondapuram"]
//         }],
//         player : true,


//     }
// ]
// console.log(users[0].cities[3].villages[1]);

// function factorial(n){
//     if (n==0 || n==1){
//         return 1;
//     }
//     else{
//         return n*factorial(n-1);
//     }
// }
// let fact = factorial(5);
// console.log(fact);


// console.log("Start");

// setTimeout(() => {
//   console.log("Async task done");
// }, 2000);

// console.log("End");

// let fs = require("fs");
// let readmew = fs.readFileSync("grid.html","utf8");
// console.log(readmew);
// console.log("after the readfile ");


// // let read1=fs.readFile("grid.html","utf8");
// // console.log(read1);
// // let read2 =fs.readFile("firoz.html","utf8");
// // console.log(read2);

// // let read3 =fs.readFile("grid.html","utf8");
// // console.log("readding after ");
 

// let read1 =fs.readFile("grid.html","utf8",(err, data)=>{
//     if (err) console.log("first");
//     console.log("1");

// });
// let read2 =fs.readFile("firoz.html","utf8",(err, data)=>{
//     if (err) console.log("second");
//     console.log("2");  

// });
// let read3 =fs.readFile("grid.html","utf8",(err, data)=>{
//     if (err) console.log("third");
//     console.log("3");  

// });


// console.log ("first hi");

// setTimeout(() => {
//     console.log("second hi");
// }, 15000);

// console.log("third hi");


// console.log("A");

// setTimeout(() => {
//   console.log("B");
// }, 0);

// console.log("C");


// function callbackNew(){
//     console.log("callback function executed");
// };

// setTimeout((callbackNew), 2000);
// console.log("after the setTimeout");


// function fetchData(callback) {
//   setTimeout(() => {
//     return "Data";
//   }, 1000);
// }

// let result = fetchData();
// console.log(result);

 
// function dotask(cb){
//   console.log("Task started");
//    cb();
// }

// function callback(){
//   setTimeout(()=> {
//     console.log("Task completed")
//   },2000);

// }
// dotask(callback);

// function doTask(cb){
//   console.log ("task started");
//   setTimeout(()=>{
//     console.log("Task done");
//   }, 2000);
//   cb();
// }

// function callBack(){
//   console.log ("call back executed ");
// }
// doTask(callBack);

// function anotherTask(callBack){
//   setTimeout ( () => {
//     console.log ("first task");
//   }, 2000);
//   callBack();
// }

// function callBack (){
//   setTimeout( () =>{
//     console.log("second task");
//   }, 2000);
// }
// anotherTask(callBack);



// function task1(callBack){
//   setTimeout ( () => {
//     console.log (" task1 done ");
//   }, 2000);
//   callBack();
// }

// function callBack (){
//   setTimeout( () =>{
//     console.log("task2  done");
//   }, 1000);
// };
// task1(callBack);

// function doTask(cb) {
//   console.log("Task started");

//   setTimeout(() => {
//     console.log("Task done");
//     cb(); // ✅ call AFTER async work
//   }, 2000);
// }

// function callBack() {
//   console.log("Callback executed");
// }

// doTask(callBack);

// function firstTask(cb) {
//   setTimeout(() => {
//     console.log("First done");
//     cb(); // run second only after first
//   }, 2000);
// }

// function secondTask() {
//   setTimeout(() => {
//     console.log("Second done");
//   }, 1000);
// }

// firstTask(secondTask);

/* constructor */

// class animal {
//   constructor(name1, breed){
//     this.name1= name1 ;
//     this.breed=breed;
//   }
// }
// class dog extends animal{
//   constructor(name1 , breed){
//     super (name1, breed);
//   }
// bark(){
//   console.log("this dog "+this.name1+" and breed "+this.breed);
// }

// }
// let ani = new dog("tommy ", "german "); 
// ani.bark();

// const date = new Date();
// console.log(date.getDay());

// const map = new Map()
// map.set('name', 'firoz');
// map.set('age',  28);
// console.log (map.get('name'));

let p = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Task completed");
    console.log("before");
  }, 2000);
});
 p.then((result) => {
  console.log("dwc" +result);
 });
 console.log(p);

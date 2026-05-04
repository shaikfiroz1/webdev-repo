// function fetchUser(userId){
//     return new Promise( (resolve , reject) => {

//       setTimeout(() => {
//         if (userId>0) {
//             resolve ( {
//                 id: userId, 
//                 name : "firoz",
//                 city : "Berlin"
//             })
//         }else {
//             reject(new Error("invalid id"));
//        }
//         }, 2000);

//     });
// }
// let p=fetchUser(0); 
// p.then (result => console.log(result))
// .catch( error => console.log (error))
// .finally(() => {
//     console.log("finally is called here" 
//   })

//creating a simple promise 

// const myPromise = new Promise( (resolve,reject) =>{
//     resolve("hello wolrd")
// }  );

// myPromise.then ( result =>  {console.log(result)});    

// const p = new Promise ( (resolve, reject) =>{
//     reject ("something is fishy")
// } )
// p.then(result=>{console.log(result)}).catch(error => {console.log(error)});


// Promise.resolve(55).then (result => {console.log('resolved log :', result)});

// function delay (){
   
//     return new Promise ( ( resolve , reject ) => {
//         setTimeout ( ()=>{
//         resolve ("things getting delayed by 5 mins")
//     },5000)
// });
// }

// let p = delay ();
// p.then (result =>{
//     console.log(result)
// })

const num= Promise.resolve(5);

num.then( num =>  num * 2).then( (num => num +10) ).then ( result => console.log('final value :', result));

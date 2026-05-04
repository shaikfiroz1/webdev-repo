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

const myPromise = new Promise( (resolve,reject) =>{
    resolve("hello wolrd")
}  );

myPromise.then ( result =>  {console.log(result)});    
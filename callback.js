// function placeorder (item , callback){
//     setTimeout( () => {
//      callback(`item is deliverd : ${item}`)
    
//     }, 1000);
// }
// placeorder("biryani", (msg)=> console.log(msg));

// function fetchData(userid , callback){
//     setTimeout ( () => {
//         if (userid ===0 ){
//             callback(new Error ("invalid userid"), null);
            
//         }else {
//             callback(null , {
//                 id: userid,
//                 name : "firoz"
//             })
//         }
//     }, 500)
// }

// fetchData(1 , (err, data) =>{
//     if (err){
//         console.error("error :", err.message);
        
//     }else {
//         console.error("Data : " , data);
//     }
// })

function step1(cb) { setTimeout(() => { console.log("Step 1 done"); cb() }, 500) }
function step2(cb) { setTimeout(() => { console.log("Step 2 done"); cb() }, 500) }
function step3(cb) { setTimeout(() => { console.log("Step 3 done"); cb() }, 500) }

step1(() => {
  step2(() => {
    step3(() => {
      console.log("All 3 steps done! ")
    })
  })
}) 
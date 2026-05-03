function placeorder (item , callback){
    setTimeout( () => {
     callback(`item is deliverd : ${item}`)
    
    }, 1000);
}
placeorder("biryani", (msg)=> console.log(msg));
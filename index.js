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
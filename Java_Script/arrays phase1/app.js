// let arr=[1,2,3,true,[1000,[2000,3000,4000],30000],undefined,"string"];

// console.log(arr[4][1][1]);
// console.log(arr);


// let num=[1,2,3,4,5,6,7,8,9];
// console.log(num);

// let isMale=true;
// console.log(isMale);


// let janwar={
//     type:"dog",
//     legs:4,
//     color:"brown",
//     isNonVegetarian:true  
// }
// console.log(janwar);
// console.log(janwar['color']);
// console.log(janwar.type);



let obj={
    naam:"Rohit",
    age:24,
    isMale:true,
    isSingle:true,
    wannaMingle:true
}
for (let x in obj){
    console.log(x);
    console.log(obj[x]);
}
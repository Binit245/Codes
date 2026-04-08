
//  how it is called

// 1.direct calling --> window object

// function samarth() {
//     console.log(this);
// }
// samarth()  

// 2. object calling --> object itself or obj inside which that method is available

// let obj = {
//     a: 30,
//     fn: function() {
//         console.log(this);
//     }   
// }
// obj.fn()  // obj

//--------------------------------------------------


// let obj = {
//     a: 10,
//     fn: function(){
//         console.log(this , "1");  // obj
//         function sam(){
//             console.log(this , "2");  
//         }
//         sam();   // window
//     } 
// }
// obj.fn()


//--------------------------------------------------

// let obj = {
//     a: 10,
//     fn: function(){
//         console.log(this , "1");  // window
//         function sam(){
//             console.log(this , "2");  
//         }
//         sam();   // window
//     } 
// }
// let fun = obj.fn;
// fun(); \



//--------------------------------------------------


//3. constructor calling --> newly created object

// function sam(){
//     this.company = "pata nhi";
//     this.package= "bahut sara";
    
// }
// let o1 = new sam();
// let o2 = new sam();
// console.log(o1);
// console.log(o2);

//--------------------------------------------------

// 4.indirect calling --> call , apply , bind  or change the refrence of this keyword

// let obj = {
//     a:10,
//     fn: function(x,y){ console.log(this.a,x,y); }
// }
// let obj2 = {
//     a:50
// }
// //obj.fn(10,20)
// obj.fn.call(obj2,200,300)
// obj.fn.apply(obj2,[500,600])
// let newFn= obj.fn.bind(obj2,200,300)    // copy banata hai
// newFn()




//--------------------------------------------------

//5. Arrow function --> lexically binded this

// function sqr(n){
//     console.log(n*n);
// }
// // way-1
// let sqr = (n) => {
//     console.log(n*n);
// }

// way-2
// let sqr2 = (n)=> n*n
// console.log(sqr2(6));

// way-3
// let sqr3 = n => n*n

// console.log(sqr3(6));


let obj = {
    a: 10,
    fn: ()=>{
        console.log(this,"1");
        let fun = ()=>{
            console.log(this,"2");
        }
        fun();
    }
}
let baba = obj.fn;
baba();


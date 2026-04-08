
// function sam(){


// }

// let a = sam()
// console.log(a);



// ------------------------------------------------------// ------------------------------------------------------

// function sam (){


// }

// let a = sam()
// let b = new sam()
// console.log(a);
// console.log(b);

// ------------------------------------------------------// ------------------------------------------------------

function sam(a,b,c,d){
    this.name = a;
    this.age = b;
    this.pasandeedaRang = c;
    this.KyaShikhtaHai = d;
    this.party= function(){
        console.log("party time");
    }
}
let a = new sam("binit",22,"Blue",true)
let b = new sam("rahul",23,"Black",false)
let c = new sam("sachin",24,"Red",true)

console.log(a);
console.log(b);
console.log(c);
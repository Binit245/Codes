

// function sam(){
//     console.log(sam);
// }
//---------------------------------------------------

// function sam(){
//     console.log(new sam());
// }

//---------------------------------------------------

// async function sam(){
//     return new Promise((resolve, reject) => {resolve("hello world")});
// }

// console.log( sam() );




async function sam1(){
    console.log(10);
    console.log(20);
    let resp = await fetch('https://jsonplaceholder.typicode.com/todos')
    let data = await resp.json();
    console.log(data);
    console.log(30);

}

sam1()


function step1(){
    console.log("please wait selecting image...");
    return new Promise(function(resolve, reject){
        setTimeout(function(){
            resolve('selected image')
        }, 4000);
    })
}

function step2(){
    console.log("please wait captioning ${image}...");
    return new Promise(function(resolve, reject){
        setTimeout(function(){
            resolve('Filtered image')
        }, 2000);
    })
}

function step3(filteredImage){
    console.log("please wait uploading ${caption}...");  
    return new Promise(function(resolve, reject){
        setTimeout(function(){
            resolve('captioned image')
        }, 3000);
    })
}

function step4(caption){
    console.log("please wait applying caption ${caption}...");
    return new Promise(function(resolve, reject){
        setTimeout(function(){
            resolve('image uploaded')
        }, 2000);
    })
}

step1()
.then(function(data){
    console.log(data);
    return step2(data)
    })
    .then(function(data){
        console.log(data);
        return step3(data)
    })
    .then(function(data){
        console.log(data);
        return step4(data)
    })
    .then(function(data){
        console.log(data);
    })













// function step1(){
//     console.log("please wait selecting image..."); 
//     return new Promise(function(resolve, reject){
//         setTimeout(function(){
//             resolve('selected image')
//             // reject('chl chl bsdk')
//         }, 4000);
//     });
        
// }

// let p1 = step1()
// p1
// .then(function(data){
    // console.log(data);})
// .catch(function(err){
    // console.log(err);})
// .finally(function(){
//     console.log("operation completed");
// });
// console.log(p1);
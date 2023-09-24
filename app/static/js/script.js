function puredigit(value){ 
    return value.replace(/[\D]/g, '');
 }
 function pureletters(value){
    return value.replace(/[^a-zA-Z]/g, ''); 
 }
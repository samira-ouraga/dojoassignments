function printDigits(startAmount, lastAmount){
    for (var i=startAmount; i<lastAmount ; i++){
        if (i==startAmount){
            continue;
        }
        console.log(i);
    }
}

console.log(printDigits(4,8));
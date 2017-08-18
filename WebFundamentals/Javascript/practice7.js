function gaming(quarters){
    while(quarters >0){  //as long as you more than 1  quarter, knowing that quaretr =25 cents
        var winning = Math.floor(Math.random()*100); // winning will be a random number from 0 to 100
        if (winning >1){      // if result is 1 then you have one
            var yourMoney = Math.floor((Math.random()*50) + 50); // money won is number from 0 to 50
            return yourMoney + quarters;        //  add money won to quarters remaining
        }
    }

    return 0;
}
console.log(gaming(564));
let num = 0
while (num < 101) {
    if (num % 3 === 0 && num % 5 === 0) {
        console.log("fizzbuzz");
        num++
    }
    else if (num % 3 === 0) {
        console.log("fizz")
        num++
    }
    else if (num % 5 === 0) {
        console.log("buzz")
        num++
    }
    else {
        console.log(num)
        num++
    }
}
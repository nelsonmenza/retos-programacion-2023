const leetDict = {
    a: '4',
    b: '13',
    c: '<',
    d: '|)',
    e: '3',
    f: '|=',
    g: '9',
    h: '#',
    i: '1',
    j: '_|',
    k: '|<',
    l: '|',
    m: '|\/|',
    n: '|\|',
    o: '0',
    p: '|2',
    q: '(_,)',
    r: '|2',
    s: '5',
    t: '7',
    u: '|_|',
    v: '\/',
    w: '\/\/',
    x: '><',
    y: '`/',
    z: '2',
}

function translateToLeet(leetDict, word) {
    let newWord = ""
    word=word.toLowerCase()

    for (let num in word) {
      if (word[num] in leetDict){
        newWord+=leetDict[word[num]]
      }
      else{
        newWord+=word[num]
      }
    }
    return newWord
}


console.log(translateToLeet(leetDict, 'hello'))
console.log(translateToLeet(leetDict, 'NelsonMenza'))
console.log(translateToLeet(leetDict, 'Pruebas'))
console.log(translateToLeet(leetDict, 'TESTING'))
console.log(translateToLeet(leetDict, 'ESTA ES La ultima Prueba.'))

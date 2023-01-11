
let input = document.querySelector("#input")
let output = document.querySelector("#output")
let operationDouble = document.querySelector("#operation-double")
let operationTriple = document.querySelector("#operation-triple")

operationDouble.addEventListener("click", () => {
    output.value = run("double", input.value)
})
operationTriple.addEventListener("click", () => {
    output.value = run("triple", input.value)
})


let operationQuack = document.querySelector("#operation-quack")
let operationChicken = document.querySelector("#operation-chicken")

operationChicken.addEventListener("click", () => {
    output.value = run("chicken", input.value)
})

operationQuack.addEventListener("click", () => {
    output.value = run("quack", input.value)
})

function chicken (x) {
    return "CHICKEN!!!"
}

function quack(x) {
    return "QUACK!!!"
}
function double(x) {
    if (typeof x === "string") {
        return "(" + x + x + ")"
    }
    console.log (x*2)
    return x * 2
}

function triple(x) {
    if (typeof x === "string"){
        return "(" + x + x + x + ")"
    }
    console.log (x*3)
    return x * 3
}

export function run(operation, x) {
    console.log(operation)
    console.log(x)
        if (operation === "double") {
            return double(x)
            
        }
        if (operation === "triple"){
            return triple (x)
        }

        if (operation === "quack") {
            return quack (x)
        }
        if (operation === "chicken") {
            return chicken (x)
        }
}


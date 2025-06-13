var car = {
    color: "green" ,
    mileage: 1500 ,
    maxspeed: 120
}

var laptop = {
    color: "Silver" ,
    processor: "Intel I-Five" ,
    gpu: "NVIDIA RTX Thirty-Sixty"
}

var smartphone = {
    screen: "Made of Gorilla Glass" ,
    camera: 3 ,
    model: "Samsung Galaxy+"
    
}

console.log(car.color)
console.log(car.mileage)
console.log(car.maxspeed)
car.color = "blue"

console.log(car)

console.log(laptop.color)
console.log(laptop.processor)
console.log(laptop.gpu)
laptop.gpu = "Ryzen 9060XT"
console.log(laptop)

console.log(smartphone.screen)
console.log(smartphone.camera)
console.log(smartphone.model)
smartphone.camera = 5
console.log(smartphone)

let btn = document.getElementById('button');

let text = document.getElementById('textfield');

let name = document.getElementById('boxname')

let color = document.getElementById('color')

let rainbow = ['red','orange','yellow','green','blue','purple','violet'];

function change() {
  let pigpicture = document.createElement("img");
  pigpicture.src="PigTrotting.jpeg"

  let puppypicture = document.createElement("img");  
  puppypicture.src="CuteAdorablePuppy.jpeg"

  let elephant = document.createElement("img");
  elephant.src="HappyElephant.jpeg"

  let response = "pigs"

  if (name.value !== ""){ 
    text.innerText = ("Hello, " + name.value + ", you have gone through the pigsifying machine. You are now a pig.")

    /* text.innerText = (name.value) */
    console.log("Secret message for " + name.value)
    text.appendChild(pigpicture)
  }

  if (name.value.length === 0){
    text.innerText = "Type in your name!"
  }

if (name.value.toLowerCase() === "me"){
    text.innerText = "Hello, you are an octopus."
   text.appendChild(elephant)
  }


  if (name.value.toLowerCase() === "tanya"){
    text.innerText = "Tanya, you now have the ability to turn into your favorite animal, the elephant!"
   text.appendChild(elephant)
  }

  if (name.value.toLowerCase() === "dad"){
    text.innerText = "Dad, you now have the ability to turn into a dog and get petted on your fluffy head all the time."
   text.appendChild(puppypicture)
  }  
    name.value = ""

}

function hues() {
   document.body.style.background = rainbow[Math.floor(7*Math.random())]
}

btn.addEventListener('click', change);

color.addEventListener('click', hues); 

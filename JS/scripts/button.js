const button= document.querySelector("button");
const heading = document.querySelector("h1");

button.onclick = () => {
    const name = prompt("whats your name?");
    alert(`Hello ${name}, nice to see you!`);
    heading.textContent = `Welcome ${name}`;
    heading.style.color = "red";
}


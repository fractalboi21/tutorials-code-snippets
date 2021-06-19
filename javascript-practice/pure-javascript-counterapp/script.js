function incrementButton() {
    let element = document.getElementById('incrementText');
    let value = element.innerHTML;
    ++value;
    document.getElementById('incrementText').innerText = value;
}
function decrementButton() {
    let element = document.getElementById('incrementText');
    let value = element.innerHTML;
    --value;
    document.getElementById('incrementText').innerHTML = value;
}
function resetVal() {
    let element = document.getElementById('incrementText');
    let value = element.innerHTML;
    value = 0;
    document.getElementById('incrementText').innerHTML = value;
}

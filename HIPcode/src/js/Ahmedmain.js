
let btnGet = document.querySelector('#btn-get');
let inputGet = document.querySelector('#input-get');

btnGet.addEventListener('click', () =>
{
  alert("Your new water goal is " + inputGet.value + " cups");
});

const toggle = document.querySelector('.toggle input')

toggle.addEventListener('click', () => {
    const onOff = toggle.parentNode.querySelector('.onoff')
    onOff.textContent = toggle.checked ? 'ON' : 'OFF'
    
})

let notifybtnGet = document.querySelector('#notifybtn-get');
let notifyinputGet = document.querySelector('#notifyinput-get');

notifybtnGet.addEventListener('click', () =>
{
  alert("You will be notified every " + notifyinputGet.value + " hour(s)");
  
});

let wakeupInput = document.querySelector('wakeupinput-get');
let bedtimeInput = document.querySelector('bedtimeinput-get');
let sleepButton = document.querySelector('sleepbtn-get');

sleepButton.addEventListener('click', () =>
{
  alert("Your new wake up time is " + wakeupInput + " and your new bedtime is " + bedtimeInput);
})
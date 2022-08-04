
let btnGet = document.querySelector('#btn-get');
let inputGet = document.querySelector('#input-get');

btnGet.addEventListener('click', () =>
{
  if(inputGet.value > 0)
  {
    alert("Your new water goal is " + inputGet.value + " cups");
  }
  else
  {
    alert("Invalid Value");
  }
})

const toggle = document.querySelector('.toggle input')

toggle.addEventListener('click', () => {
    const onOff = toggle.parentNode.querySelector('.onoff')
    onOff.textContent = toggle.checked ? 'ON' : 'OFF'
    
})

let notifybtnGet = document.querySelector('#notifybtn-get');
let notifyinputGet = document.querySelector('#notifyinput-get');

notifybtnGet.addEventListener('click', () =>
{
  if(notifyinputGet.value > 0)
  {
    alert("You will be notified every " + notifyinputGet.value + " hour(s)");
  }
  else
  {
    alert("Invalid Value");
  }
})

let wakeuptime = document.getElementById("wakeupinput-get");
let sleepingtime = document.getElementById("bedtime-get");


function processData(wakeuptime,sleepingtime)
{
 var awake = wakeuptime.value;
 var asleep = sleepingtime.value;
 alert("Your new wake up time is " + awake + " and your new sleeping time is " + asleep);
}
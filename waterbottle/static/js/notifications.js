
let btnGet = document.querySelector('#btn-get');
let inputGet = document.querySelector('#input-get');

btnGet.addEventListener('click', () => {
  if (inputGet.value > 0) {
    alert("Your new water goal is " + inputGet.value + " cups");
  }
  else {
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
let minuteInput = document.querySelector('#minuteinput-get');

notifybtnGet.addEventListener('click', function (event) {
  if (notifyinputGet.value >= 0 &&  minuteInput.value >= 0) {
    event.preventDefault();
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    function get_fb(){
      $.ajaxSetup({
        headers: { "X-CSRFToken": csrftoken }
      });
      $.ajax({
        type: "POST",
        url:'/send/',
        data: {},
        success: function (data) {
          console.log("success")
        }
      });
    }
    setInterval(get_fb, 1000*60*60*notifyinputGet.value + 1000*60*minuteInput.value);
    alert("You will be notified every " + notifyinputGet.value + " hour(s)" + minuteInput.value + " minute(s) ");

  }
  else {
    alert("Invalid Value");
  }
})




let wakeuptime = document.getElementById("wakeupinput-get");
let sleepingtime = document.getElementById("bedtimeinput-get");
let saveTimeBtn = document.getElementById("sleepbtn-get");
saveTimeBtn.addEventListener('click', () => {
  alert("Your new wake up time is " + wakeuptime.value + " and your new sleeping time is " + sleepingtime.value);
})


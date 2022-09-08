
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


let wakeuptime = document.getElementById("wakeupinput-get");
let sleepingtime = document.getElementById("bedtimeinput-get");
let saveTimeBtn = document.getElementById("sleepbtn-get");
saveTimeBtn.addEventListener('click', () => {
  alert("Your new wake up time is " + wakeuptime.value + " and your new sleeping time is " + sleepingtime.value);
})



const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
function get_fb(){
  var fcm_token = localStorage.getItem('fcm_token')
  $.ajaxSetup({
    headers: { "X-CSRFToken": csrftoken }
  });
  $.ajax({
    type: "POST",
    url:'/send/',
    data: JSON.stringify({"token": fcm_token}),
    success: function (data) {
      console.log("success")
    }
  });
}
const toggle = document.querySelector('.toggle input')

toggle.addEventListener('click', () => {
  const onOff = toggle.parentNode.querySelector('.onoff')
  onOff.textContent = toggle.checked ? 'ON' : 'OFF'
  if (onOff.textContent == 'ON') {
    if (inputGet.value && wakeuptime.value && sleepingtime.value) {
      let sleepHour = sleepingtime.value.split(':')[0]
      let wakeupHour = wakeuptime.value.split(':')[0]
      if ( sleepHour < wakeupHour  ) {
        var dividedHour = (12 + parseInt(sleepHour) - parseInt(wakeupHour)) + 12;
      } else {
        var dividedHour = parseInt(sleepHour) - parseInt(wakeupHour)
      }
      let dividedMinute = sleepingtime.value.split(':')[1] - wakeuptime.value.split(':')[1]
      let averageTime = Math.floor((dividedHour*60 + dividedMinute)/inputGet.value)
      setInterval(get_fb, 1000*60*averageTime);
      // console.log((dividedHour*60 + dividedMinute)/inputGet.value);
      alert("You will be notifed every "+ Math.floor(averageTime/60) + " hour(s) and " + (averageTime%60)+ " minute(s)");
      var div = document.getElementById('notify');
      div.remove();
    }
    else {
      alert("Make sure you have entered your water goal, wake up time, and bed time");
      toggle.checked = false;
      onOff.textContent = 'OFF';
      
    }
  }

})

let notifybtnGet = document.querySelector('#notifybtn-get');
let notifyinputGet = document.querySelector('#notifyinput-get');
let minuteInput = document.querySelector('#minuteinput-get');

notifybtnGet.addEventListener('click', function (event) {
  if (notifyinputGet.value >= 0 &&  minuteInput.value >= 0) {
    event.preventDefault();
    setInterval(get_fb, 1000*60*60*notifyinputGet.value + 1000*60*minuteInput.value);
    alert("You will be notified every " + notifyinputGet.value + " hour(s) " + minuteInput.value + " minute(s) ");

  }
  else {
    alert("Invalid Value");
  }
})





var firebaseConfig = {
    apiKey: "AIzaSyB-fiT1Ju7Gf4dPdS9BbscZLnjvwycvtt4",
    authDomain: "drink-water-database.firebaseapp.com",
    databaseURL: "https://drink-water-database-default-rtdb.firebaseio.com",
    projectId: "drink-water-database",
    storageBucket: "drink-water-database.appspot.com",
    messagingSenderId: "498708914059",
    appId: "1:498708914059:web:32adf2844b31d65218598e",
    measurementId: "G-TVZERVCL6F"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  firebase.analytics();
  const messaging = firebase.messaging();
  messaging.getToken({ vapidKey: 'BPcTEKzpK4xmNDhcAuyICrML7vtsaewlKkjB15phBH5Ti_T5gsAuUuQwf2EHQj5I5CyqrH6fN3MwQ7AFDJv6Gz8' })
    .then((currentToken) => {
      if (currentToken) {
        localStorage.setItem('fcm_token', currentToken)
        document.cookie = "fcm_token=" + currentToken
        console.log("TOKEN: " + currentToken)
        console.log("ALL COOKIES: " + document.cookie.split(';'))
      } else {
        console.log('No registration token available. Request permission to generate one.');
      }
    }).catch((err) => {
      console.log('An error occurred while retrieving token. ', err);
    });

  messaging.requestPermission().then(function () {
    console.log("Notification permission granted.");
    return messaging.getToken()
  }).catch(function (error) {
    console.log("Unable to get permission to notify.", error)
  })

  messaging.onMessage((payload) => {
    console.log("Message received ", payload)
    const notificationOptions = {
      body: payload.notification.body,
      icon: payload.notification.icon
    }
    if (Notification.permission == "granted") {
      var notification = new Notification(payload.notification.title, notificationOptions)
      notification.onClick = function (ev) {
        ev.preventDefault();
        window.open(payload.notification.click_action, '_blank');
        notification.close();
      }
    }
  });

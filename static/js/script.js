//Functions and variables ---------------------------------

function printValues(obj) {
  for (var key in obj) {
      if (typeof obj[key] === "object") {
          console.log('key: ' + key );
          printValues(obj[key]);   
      } else {
          console.log('key: ' + key );
          console.log('val: ' + obj[key]);    
      }
  }
}


//Event listeners -----------------------------------------



//Initialize mobile menu
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {
      'edge': 'right',
    });
  });

//Initialize modals
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, {'dismissible': true, 'opacity': 0.65});
  });

 
//Initialize dropdown for login / signup etc Desktop/Tablet
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.dropdown-trigger');
  var instances = M.Dropdown.init(elems, {
    'coverTrigger': false,
    'inDuration': 500,
    'outDuration': 300,
  });
});

 //Initialize dropdown for login / signup etc Mobile
 document.addEventListener('DOMContentLoaded', function() {
  var elems2 = document.querySelectorAll('.dropdown-trigger2');
  var instances = M.Dropdown.init(elems2, {
    'coverTrigger': false,
    'inDuration': 500,
    'outDuration': 300,
  });
});


// Initialize tooltips
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.tooltipped');
  var instances = M.Tooltip.init(elems, {
    'margin': 0,
    'inDuration': 1500,
    'outDuration': 0,
    'outDelay': 0,
  });
});


 /* jQuery ---------------------*/

 //Fade effect on messages
 $(".msg").ready(function(){
  $(".msg").fadeOut(10000);
});
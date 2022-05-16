//Functions and variables ---------------------------------

function printValues(obj) {
  for (var key in obj) {
      if (typeof obj[key] === "object") {
          console.log('key: ' + key )
          printValues(obj[key]);   
      } else {
          console.log('key: ' + key )
          console.log('val: ' + obj[key]);    
      }
  }
}


//Event listeners -----------------------------------------



//Initialize mobile menu
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {});
  });

//Initialize modals
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, {'dismissible': true, 'opacity': 0.65});
  });

 //Initialize dropdown for login / signup etc
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.dropdown-trigger');
  var instances = M.Dropdown.init(elems, {});
});


//Auto fill hidden form for submitting order to database...
document.addEventListener('DOMContentLoaded', function autoFillOrderForm() {
  document.getElementById('id_order_id').setAttribute('value', order_id );
  document.getElementById('id_user_id').setAttribute('value', user_id );
  document.getElementById('id_grand_total').setAttribute('value', grand_total );
  console.log("updating form fields");
});

/*
 document.addEventListener('DOMContentLoaded' && 'submit', function openModal() {
    var instance = M.Modal.getInstance($('#add-to-basket'));
    instance.open();
});
*/

//Paypal API integration ------------------------------------
const payPalButtons = paypal.Buttons({

  style: {
    color: "gold",
    shape: "rect",
    layout: "vertical"
  },
// Set up the transaction
createOrder: function(data, actions) {
  const createOrderPayload = {
      purchase_units: [{
      reference_id: order_id,
      amount: {
         
          value: grand_total
      },
    }]
  }
  console.log('The order payload is: ' + JSON.stringify(createOrderPayload, null, 4));
  return actions.order.create(createOrderPayload);
},

//On Initializastion 
onInit: (data, actions) => {
  let grand_total = document.getElementById('grand-total').textContent;
  let user_id = document.getElementById('user_id').textContent;
  let order_id = document.getElementById('order_id').textContent;
  
  if (grand_total == 0){
    actions.disable();
  }
  else {
    actions.enable();
  }
},

//If order is cancelled
onCancel: (data) => {
  alert('Payment Cancelled');
},
// Finalize the transaction
onApprove: (data, actions) => {
    const captureOrderHandler = (details) => {
        const payerName = details.payer.name.given_name;
        console.log('Transaction completed for: ' + payerName);
        console.log('The details: ' + JSON.stringify(details, null, 4));

        document.getElementById('download-0').removeAttribute('disabled');
        let transaction_date = document.getElementById('transaction_date').textContent;
        let transaction_time = document.getElementById('transaction_time').textContent;
        document.getElementById('id_transaction_date').setAttribute('value', transaction_date );
        document.getElementById('id_transaction_time').setAttribute('value', transaction_time );              
        document.getElementById('order-form').submit();
    };
    return actions.order.capture().then(captureOrderHandler);

  },

  // handle unrecoverable errors
  onError: (err) => {
      console.error('An error prevented the buyer from checking out with PayPal');
      alert('Payment failed');
  }
  });

  //Render the paypal button
  payPalButtons
    .render("#paypal-button-container")
    .catch((err) => {
      console.error('PayPal Buttons failed to render');
    });





    

 
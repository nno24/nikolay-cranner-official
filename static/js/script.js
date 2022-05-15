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



  let grand_total = document.getElementById('grand-total').textContent;
  let user_id = document.getElementById('user_id').textContent;
  let order_id = document.getElementById('order_id').textContent;


paypal.Buttons({

// Set up the transaction
createOrder: function(data, actions) {
    return actions.order.create({
        purchase_units: [{
            reference_id: order_id,
            amount: {
               
                value: grand_total
            }
        }]
    });
},

// Finalize the transaction
onApprove: function(data, actions) {
    return actions.order.capture().then(function(orderData) {
        // Successful capture! For demo purposes:
        console.log('Capture result', orderData, JSON.stringify(orderData, null, 2));
        var transaction = orderData.purchase_units[0].payments.captures[0];
        //alert('Transaction '+ transaction.status + ': ' + transaction.id + '\n\nSee console for all available details');

        // Replace the above to show a success message within this page, e.g.
        //const element = document.getElementById('paypal-button-container');
        //element.innerHTML = '';
        //element.innerHTML = '<h3>Thank you for your payment!</h3>';
        // Or go to another URL:  actions.redirect('thank_you.html');
        
        document.getElementById('download-0').removeAttribute('disabled');
        let transaction_date = document.getElementById('transaction_date').textContent;
        let transaction_time = document.getElementById('transaction_time').textContent;
        document.getElementById('id_transaction_date').setAttribute('value', transaction_date );
        document.getElementById('id_transaction_time').setAttribute('value', transaction_time );              
        document.getElementById('order-form').submit();
    
        

           
        
    });
}


}).render('#paypal-button-container');


/*
 document.addEventListener('DOMContentLoaded' && 'submit', function openModal() {
    var instance = M.Modal.getInstance($('#add-to-basket'));
    instance.open();
});
*/

//Auto fill hidden form for submitting order to database...
document.addEventListener('DOMContentLoaded', function autoFillOrderForm() {
  document.getElementById('id_order_id').setAttribute('value', order_id );
  document.getElementById('id_user_id').setAttribute('value', user_id );
  document.getElementById('id_grand_total').setAttribute('value', grand_total );
  console.log("updating form fields");
});

    

 
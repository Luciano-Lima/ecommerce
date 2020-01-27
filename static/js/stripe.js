$(function() {
    // Get the card detail
    $('#payment-form').submit(function() {
        
        var form = this;
        var card = {
            number: $('#id_number').val(),
            cvc: $('#id_cvv').val(),
            exp_month: $('#id_exp_month').val(),
            exp_year: $('#id_exp_year').val(),
        };
           
        Stripe.createToken(card, function(status, response) {
            if (status === 200) {
                $('#card-error').hide();
                $('#id_stripe_id').val(response.id);

                // Removing the card atributes
                $("#id_number").removeAttr('name');
                $("#id_cvv").removeAttr('name');
                $("#id_exp_month").removeAttr('name');
                $("#id_exp_year").removeAttr('name');
                form.submit();
    
            } else {
                $('#stripe-error-message').text(response.error.message);
                $('#card-error').show();
                $("#validate_card_btn").attr("disabled", false);
            }
        });
        return false;
        });
    })
            
        
$(function() {
    // Get the card detail
    $('#payment').submit(function() {
        var form = this;
        var card = {
            number: $('#id_credit_card_number').val(),
            expMonth: $('#id_expiry_month').val(),
            expYear: $('#id_expiry_year').val(),
            cvc: $('#id_cvv').val(),
        };
    Stripe.createToken(card, function(status, response) {
        if (status === 200) {
            $('#credit-card-erros').hide();
            $('#id_stripe_id').val(response.id);

            // Preventes the card detail to be sent to our server by removiments the atributes
            $('#id_credit_card_number').removeAtrr('name');
            $('#id_expiry_month').removeAtrr('name');
            $('#id_expiry_year').removeAtrr('name');
            $('#id_cvv').removeAtrr('name');
            
            form.submit();

        } else {
            $('#stripe-error-message').text(response.error.message);
            $('#credit-card-errors').show();
            $('#validate_card_btn').attr('disable', false);
        }
    });
    return false;
    });
})

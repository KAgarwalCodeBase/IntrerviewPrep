public class Driver {
    public static void main(String[] args) {
        PaymentProcessor processor = new PaymentProcessor();

        Payment creditCard = new CreditCardPayment();
        Payment payPal = new PayPalPayment();
        Payment googlePay = new GooglePayPayment();

        processor.processPayment(creditCard);
        processor.processPayment(payPal);
        processor.processPayment(googlePay);
    }
}

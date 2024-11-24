class Driver{
    public static void main(String args[]){
        PaymentProcessor paymentProcessor= new PaymentProcessor();
        paymentProcessor.processPayment("CreditCard");   
        paymentProcessor.processPayment("PayPal");   
        

    }
}
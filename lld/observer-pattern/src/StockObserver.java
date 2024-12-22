public class StockObserver implements Observer{
    private static int observerIDTracker = 0;
    private double ibmPrice;
    private double aapPrice;
    private double googPrice;
    private int observerID;
    private StockGrabber stockGrabber;
    public StockObserver(StockGrabber stockGrabber){
        this.stockGrabber = stockGrabber;
        this.observerID = ++observerIDTracker;
        System.out.println("New Observer " + this.observerID);

        this.stockGrabber.register(this);
    }
    @Override
    public void update(double ibmPrice, double aapPrice, double googPrice) {
        this.ibmPrice = ibmPrice;
        this.aapPrice = aapPrice;
        this.googPrice = googPrice;

        printThePrice();
    }

    private void printThePrice(){
        System.out.println(observerID + "\nIBM: " + ibmPrice + "\nAAPL: " +
                aapPrice + "\nGOOG: " + googPrice + "\n");

    }

}

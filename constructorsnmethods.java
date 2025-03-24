public class Vehicle
{

    //instance variables
    private boolean usedFlag;
    private String model;
    private int numTires;

    public Vehicle(boolean f, String m, int n) {
        usedFlag = f;
        model = m;
        numTires = n;
    }

    //overloaded constructor
    //notice how the tire value is not a parameter, as it is given a default value
    public Vehicle(boolean f, String m) {
        usedFlag = f;
        model = m;
        numTires = 0;
    }

    public void setTire(int newTires) {

        numTires = newTires + 4;
        
    }

    
    //toString() method, converts the object to a string that can be returned
    public String toString() {
        return "Used: " + usedFlag + ", Model: " + model + ", Tires: " + numTires;
    }    

    public static void main(String[] args)
        {
            //since this object doesn't specify the number of tires, it will give it the default value 
            Vehicle arya = new Vehicle(true, "1967 ferrari");
            System.out.println(arya);
       
        }
}

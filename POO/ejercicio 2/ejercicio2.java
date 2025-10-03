abstract class Bus{
    public int asientos;
    public int pasajeros;
    public double pasaje;
    public Bus(int asientos,int pasajeros,double pasaje){
        this.asientos=asientos;
        this.pasajeros=pasajeros;
        this.pasaje=pasaje;
    }
    public void Subirpasajeros(int x){
        if (this.asientos>=this.pasajeros+x) {
            this.pasajeros+=x;
            int libres=this.asientos-this.pasajeros;
            System.out.println("Aun quedan: "+libres);
        }else{
            System.out.println("Esta lleno");
        }
    }
    public double Cobro(){
        return this.pasaje*this.pasajeros;
    }
}

class BusT extends Bus{
    public BusT(int asientos,double pasaje){
        super(asientos, 0 , pasaje);
    }
}

public class ejercicio2 {
public static void main(String[] args) {
    BusT bus1 = new BusT(24, 1.50);
    int a=0; 
    bus1.Subirpasajeros(8);
    System.out.println(bus1.Cobro());
    bus1.Subirpasajeros(10);
    System.out.println(bus1.Cobro());
    bus1.Subirpasajeros(10);
    a++;
}
}

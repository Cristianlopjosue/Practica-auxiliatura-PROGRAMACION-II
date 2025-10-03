class Parada{
    public String admins[];
    public String autos [][];
    public String nombreP;
    public Parada(String admins[],String autos[][],String nombreP){
        this.admins=admins;
        this.autos=autos;
        this.nombreP=nombreP;
    }
    public Parada(){
        this.admins=new String[]{"juan","jose","Luis","pedro","Joselito","julian","Santiago","Ignacio","Victor","Daniel"};
        this.autos=new String[][]{{"Toyota","Tesla"},{"Juan","Luis"},{"109098","90876"}};
        this.nombreP="Parada cota cota";
    }
    public void  Mostrar(){
        System.out.print("Admins:");
        for (int i = 0; i < admins.length; i++) {
            System.out.print(admins[i]+" , ");
        }
        System.out.println();
        for (int i = 0; i < autos.length; i++) {
            for (int j = 0; j < autos[i].length; j++) {
                System.out.print(autos[i][j]+"  ");
            }
            System.out.println();
        }
        System.out.println("Nombre:"+nombreP);
    }
        public void Adicion(String[] x){
            String[] nuevoArray = new String[admins.length +x.length];    
            for (int i = 0; i < admins.length; i++) {
                nuevoArray[i] = admins[i]; 
            }
            for (int i = 0; i < x.length; i++) {
                nuevoArray[admins.length + i] = x[i];
    admins = nuevoArray; 
}
}
}
public class ejercicio7 {
public static void main(String[] args) {
    Parada parada= new Parada();
    parada.Mostrar();
    Parada parada1= new Parada(new String[]{"Juan","Pepe"} , new String[][]{{"Toyota","Suzuki"},{"10909","67345"}},"Felipez");
    parada1.Mostrar();
}
}

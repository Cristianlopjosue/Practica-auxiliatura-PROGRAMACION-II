import java.util.Scanner;
class Fruta{
    private  String nombre;
    private  String tipo;
    private  int nroVitaminas;
    private  String[] v3;
    public Fruta(String nombre, String tipo, int nroVitaminas){
        this.nombre=nombre;
        this.tipo=tipo;
        this.nroVitaminas=nroVitaminas;
        this.v3= new String[nroVitaminas];
    }
    public void Vitaminas(){
        Scanner sc=new Scanner(System.in);
        System.out.println("Ingrese las vitaminas de: "+nombre);
        for (int i = 0; i < this.nroVitaminas; i++) {
            this.v3[i]=sc.nextLine();
        }
    }
    public void Mostrar(){
        System.out.println("La fruta: "+nombre+"\nEs de tipo: "+tipo+"\nNumero de Vitaminas: "+nroVitaminas);
        for (int i = 0; i < nroVitaminas; i++) {
            System.out.print("Vitamina: "+v3[i]+"\n");
        }
    }
}
public class ejercicio13 {
public static void main(String[] args) {
    Fruta fruta1= new Fruta("Mango","Drupa", 2);
    Fruta fruta2= new Fruta("Coco","Tropical", 4);
    Fruta fruta3= new Fruta("Frutilla","Fruto rojo", 3);
    fruta1.Vitaminas();
    fruta2.Vitaminas();
    fruta3.Vitaminas();
    fruta1.Mostrar();
}

}

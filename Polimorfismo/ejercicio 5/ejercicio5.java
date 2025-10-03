class Celular{
    public int nroTel;
    public String Dueno;
    public int Espacio;
    public int ram;
    public int nroApp;
    public Celular(int nroTel,String Dueno,int Espacio,int ram,int nroApp){
        this.nroTel=nroTel;
        this.Dueno=Dueno;
        this.Espacio=Espacio;
        this.ram=ram;
        this.nroApp=nroApp;
    }
    public void Incrementar(){
        this.nroApp+=10;
    }
    public void Bajar(){
        this.Espacio-=10;
    }
    public void Mostrar(){
        System.out.println("nroTel:"+nroTel+"\nEspacio:"+Espacio+"\nDueno:"+Dueno+"\nRam:"+ram+"\nnroApp:"+nroApp);
    }
    }
public class ejercicio5 {
public static void main(String[] args) {
    Celular cel1= new Celular(29329323, "Jose", 250, 8, 6);
    cel1.Mostrar();
    cel1.Bajar();
    cel1.Incrementar();
    cel1.Mostrar();
}
}

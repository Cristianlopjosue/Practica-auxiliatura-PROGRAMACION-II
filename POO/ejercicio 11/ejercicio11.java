class Cliente{
    public String nombre;
    public int mesa;
    public Cliente(String nombre,int mesa){
        this.nombre=nombre;
        this.mesa=mesa;
    }
    public String getNombre(){
        return this.nombre;
    }
    public void setNombre(String otro){
        this.nombre=otro;
    }
    public int getMesa(){
        return this.mesa;
    }
    public void setMesa(int otro){
        this.mesa=otro;
    }
    public void Mostrar(){
        System.out.println("Nombre: "+this.nombre+"\nMesa: "+this.mesa);
    }
}

class Pedido{
    public String Producto;
    public String Estado;
    public Pedido(String Producto,String Estado){
        this.Producto=Producto;
        this.Estado=Estado;
    }
    public String getProductos(){
        return this.Producto;
    }
    public void setProductos(String otro){
        this.Producto=otro;
    }
    public void Mostrar(){
        System.out.println("Producto: "+this.Producto+"\nEstado: "+this.Estado);
    }

}
public class ejercicio11 {
    public static void main(String[] args) {
        Cliente cliente1 = new Cliente("Ana", 5);
        cliente1.Mostrar();
        Pedido pedido1 = new Pedido("Café Latte", "Delicioso");
        pedido1.Mostrar();
    }
}

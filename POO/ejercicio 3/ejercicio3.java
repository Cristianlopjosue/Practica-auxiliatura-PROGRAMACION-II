class Producto{
    public String nombre;
    public int precio;
    public int stock;
    public Producto(String nombre, int precio, int stock){
        this.nombre=nombre;
        this.precio=precio;
        this.stock=stock;
    }
    public void VenderProductos(int x){
        this.stock-=x;
    }
    public void restablecer(int x){
        this.stock+=x;
    }
}

public class ejercicio3 {
public static void main(String[] args) {
    Producto canela = new Producto("Canela", 2, 30);
}
}

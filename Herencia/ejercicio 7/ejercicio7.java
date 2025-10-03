class Persona{
    protected  String nombre;
    protected  String Paterno;
    protected  String Materno;
    protected  int edad;
    public Persona(String nombre, String Paterno, String Materno, int edad){
        this.nombre=nombre;
        this.Paterno=Paterno;
        this.Materno=Materno;
        this.edad=edad;
    }
    public void Mostrar(){
        System.out.println("Nombre: "+nombre+"Paterno: "+Paterno+"Materno"+Materno);
    }
}
class Docente extends Persona{
    private int sueldo;
    private int regProfecional;
    public Docente(String nombre, String Paterno, String Materno, int edad,int sueldo,int regProfecional){
        super(nombre, Paterno, Materno, edad);
        this.sueldo=sueldo;
        this.regProfecional=regProfecional;        
    }
    public void Mostrar(){
        System.out.println("Nombre: "+nombre+"Paterno: "+Paterno+"Materno"+Materno+"Sueldo: "+sueldo+"registro: "+regProfecional);
    }
}
class Estudiante extends Persona{
    private int Ru;
    private int matricula;
    public Estudiante(String nombre, String Paterno, String Materno, int edad,int Ru,int matricula){
        super(nombre, Paterno, Materno, edad);
        this.Ru=Ru;
        this.matricula=matricula;
    }
    public void Mostrar(){
        System.out.println("Nombre: "+nombre+"Paterno: "+Paterno+"Materno"+Materno+"Ru: "+Ru+"Matricula"+matricula);
    }
}

public class ejercicio7 {
public static void main(String[] args) {
    Estudiante estudiante1 = new Estudiante("Jose", "Lopez", "Paco", 19, 10909814, 879685);
    Estudiante estudiante2 = new Estudiante("Ernesto", "Quispe", "Mamani", 23, 38576, 28484095);
    Docente docente1=new Docente("Zenon", "Condori", "Gomez", 34, 5000, 394858);
    estudiante1.Mostrar();
    estudiante2.Mostrar();
    docente1.Mostrar();
}
}

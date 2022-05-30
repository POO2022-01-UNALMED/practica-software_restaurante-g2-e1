package gestorAplicacion.gente;

abstract class Persona {
private int cedula;
private String nombre;
private int telefono;

//constructor

public String informacion() {
	return "cedula: "+cedula+" nombre: "+nombre+" telefono: "+telefono;
}

public Persona(int cedula,String nombre,int telefono) {
	this.cedula=cedula;
	this.nombre=nombre;
	this.telefono=telefono;
}

//metodos get y set

public int getCedula() {
	return cedula;
}

public String getNombre() {
	return nombre;
}

public void setNombre(String nombre) {
	this.nombre=nombre;
}
public int getTelefono() {
	return telefono;
}

public void setTelefono(int telefono) {
	this.telefono=telefono;
}

}

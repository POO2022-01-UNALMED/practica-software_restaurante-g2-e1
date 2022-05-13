package gente;

public class Persona {
private int cedula;
private String nombre;
private int telefono;

public Persona(int cedula,String nombre,int telefono) {
	this.cedula=cedula;
	this.nombre=nombre;
	this.telefono=telefono;
}

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

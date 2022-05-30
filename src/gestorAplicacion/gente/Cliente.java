package gestorAplicacion.gente;

import java.util.ArrayList; 
import java.util.Collections;
import java.io.Serializable;

public class Cliente extends Persona implements Serializable{
	
	//constructor
	public Cliente(int cedula,String nombre,int telefono) {
		super(cedula,nombre,telefono);
	}
	
	public String informacion() {
		return "nombre del cliente: "+this.getNombre()+" \ncedula: "+this.getCedula()+" \ntelefono: "+this.getTelefono();
	}
	
}
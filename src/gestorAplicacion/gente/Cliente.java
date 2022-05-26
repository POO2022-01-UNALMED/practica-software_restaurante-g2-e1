package gestorAplicacion.gente;

import java.util.ArrayList; 
import java.util.Collections;

public class Cliente extends Persona {
	
	//constructor
	public Cliente(int cedula,String nombre,int telefono) {
		super(cedula,nombre,telefono);
	}
	
	public String informacion() {
		return "nombre del cliente: "+this.getNombre()+" \ncedula: "+this.getCedula()+" \ntelefono: "+this.getTelefono();
	}
	
}
package gestorAplicacion.gente;

import java.util.ArrayList; 
import java.util.Collections;
import java.io.Serializable;

public class Cliente extends Persona implements Serializable{
	
	public String perfil() {
		return "El cliente es la razon de ser del restaurante, puesto que es el quien consume los productos que se venden en el";
	}
	
	//constructor
	public Cliente(int cedula,String nombre,int telefono) {
		super(cedula,nombre,telefono);
	}
	
	public String informacion() {
		return "nombre del cliente: "+this.getNombre()+" \ncedula: "+this.getCedula()+" \ntelefono: "+this.getTelefono();
	}
	
}
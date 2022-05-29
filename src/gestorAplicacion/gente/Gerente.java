package gestorAplicacion.gente;

import java.util.ArrayList; 
import java.util.Collections;

public class Gerente extends Persona implements gerente_por_defecto {
	private String contraseña_gerente;
	public static Gerente[] arr=new Gerente[1];
	
	//constructor
	
	public Gerente(int cedula,String nombre,int telefono,String contraseña_gerente) {
		super(cedula,nombre,telefono);
		this.contraseña_gerente=contraseña_gerente;
		arr[0]=null;
		arr[0]=this;
	}
	
	public Gerente() {
		super(CEDULA,NOMBRE,TELEFONO);
		contraseña_gerente=CONTRASEÑA;
		arr[0]=this;
	}
	
	//metodos get y set
	
	public int getConstraseña_gerente() {
		return contraseña_gerente;
	}
	
	public void setContraseña_gerente(int contraseña_gerente) {
		this.contraseña_gerente=contraseña_gerente;
	}
	//metodos

public void comprar_ingredientes() {
	//actualiza el numero de ingredientes y resta de el total de efectivo
	//disponible de lo que cuesta
}

public void contratar_empleado(int cedula,String nombre,int telefono) {
	Empleado b=new Empleado(cedula,nombre,telefono);
}

public void despedir_empleado(Empleado empleado) {
	int in=1; //numero del primer empleado
	
	Empleado.lista_empleados.remove(empleado.getNumero_asignado()-1); //se retira al empleado de la lista de empleados
	
	for (int i=0;i<Empleado.lista_empleados.size();i++) { //se resignan los numero de empleado
		Empleado.lista_empleados.get(i).setNumero_asignado(in);
		in++;
	}
	Empleado.numero_empleados--;
	
	empleado=null;
}

public void despido_inteligente() { //este metodo despide al empleado menos eficiente
	
	despedir_empleado(Empleado.empleado_menos_eficiente());
	
}

public String informacion() {
	return "nombre del Gerente: "+this.getNombre()+" \ncedula: "+this.getCedula()+" \ntelefono: "+this.getTelefono();
}

}
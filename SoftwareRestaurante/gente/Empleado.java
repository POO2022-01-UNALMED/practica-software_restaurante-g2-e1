package gente;

import restaurante.*;
import java.util.ArrayList; 
import java.util.Collections;

public class Empleado extends Persona {
private int numero_ventas;
private Turno turno;
public static ArrayList<Empleado> lista_empleados = new ArrayList<Empleado>();

public Empleado(int cedula,String nombre,int telefono) {
	super(cedula,nombre,telefono);
	Empleado.lista_empleados.add(this);
}

public int getNumero_ventas() {
	return numero_ventas;
}

public void nuevaVenta() {
	numero_ventas++;
}

public Turno getTurno() {
	return turno;
}

public void setTurno(Turno turno) {
	this.turno=turno;
}

public static Empleado empleado_mas_eficiente() {
	ArrayList<Integer> cantventasporempleado = new ArrayList<Integer>(); //arraylist con la cantidad de ventas por empleado
	for (int l=0;l<Empleado.lista_empleados.size();l++) {
		cantventasporempleado.add(lista_empleados.get(l).getNumero_ventas());
	}
	Integer maximo = Collections.max(cantventasporempleado); //maximo numero de ventas por empleado
	for (int j=0;j<cantventasporempleado.size();j++) {
		if(cantventasporempleado.get(j)==maximo) {
			return lista_empleados.get(j);
		}
	}
	return null;	
}

public void crear_nueva_orden() {
	/*metodo por definir, recibe los parametros
	 *  para crear una nueva instancia de orden
	 */
}

}

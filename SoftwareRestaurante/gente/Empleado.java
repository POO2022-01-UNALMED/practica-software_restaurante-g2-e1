package gente;

import restaurante.*;
import java.util.ArrayList; 
import java.util.Collections;

public class Empleado extends Persona {
private int numero_ventas;
private Turno turno;
public static ArrayList<Empleado> lista_empleados = new ArrayList<Empleado>();
public static int numero_empleados;

//constructor

public Empleado(int cedula,String nombre,int telefono) {
	super(cedula,nombre,telefono);
	Empleado.lista_empleados.add(this);
	numero_empleados++;
}

//metodos get y set

public int getNumero_empleados() { 
	return numero_empleados;
}

public int getNumero_ventas() {
	return numero_ventas;
}

public Turno getTurno() {
	return turno;
}

public void setTurno(Turno turno) {
	this.turno=turno;
}

// otros metodos

public void nuevaVenta() {
	numero_ventas++;
}

public static Empleado empleado_mas_eficiente() { //este metodo compara la cantidad de ventas de los empleados y devuelve el que MAS ventas tiene
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


public static Empleado empleado_menos_eficiente() { //este metodo compara la cantidad de ventas de los empleados y devuelve el que MENOS ventas tiene
	ArrayList<Integer> cantventasporempleado = new ArrayList<Integer>(); //arraylist con la cantidad de ventas por empleado
	for (int l=0;l<Empleado.lista_empleados.size();l++) {
		cantventasporempleado.add(lista_empleados.get(l).getNumero_ventas());
	}
	Integer minimo = Collections.min(cantventasporempleado); //minimo numero de ventas por empleado
	for (int j=0;j<cantventasporempleado.size();j++) {
		if(cantventasporempleado.get(j)==minimo) {
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

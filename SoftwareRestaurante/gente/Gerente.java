package gente;

import restaurante.*;
import java.util.ArrayList; 
import java.util.Collections;

public class Gerente extends Persona {
	
	//constructor
	
	public Gerente(int cedula,String nombre,int telefono) {
		super(cedula,nombre,telefono);
	}
	
	//metodos
	
public void arqueo_de_caja_global() {
	//realiza un arqueo de caja de forma global,
	//es decir, realiza el arqueo de caja para todas las cajas
	//y al final suma los resultados
}

public void ventas_global() {
	//devuelve el total de ventas realizado por todas las cajas
}

public void comprar_ingredientes() {
	//actualiza el numero de ingredientes y resta de el total de efectivo
	//disponible de lo que cuesta
}

public void contratar_empleado(int cedula,String nombre,int telefono) {
	Empleado b=new Empleado(cedula,nombre,telefono);
}

public void despedir_empleado(Empleado empleado) {
	empleado=null;
}
///////pruebas///////
public static void main(String args[]) {
	Gerente g=new Gerente(1,"demetrio",2);
	g.contratar_empleado(1,"pan",22);
	g.contratar_empleado(2,"pin",23);
	g.contratar_empleado(3,"pen",24);
	Empleado.lista_empleados.get(1).nuevaVenta();
	Empleado.lista_empleados.get(1).nuevaVenta();
	Empleado.lista_empleados.get(2).nuevaVenta();
	Empleado.lista_empleados.get(2).nuevaVenta();
	Empleado.lista_empleados.get(2).nuevaVenta();
	Empleado.lista_empleados.get(2).nuevaVenta();
	String a=Empleado.empleado_mas_eficiente().getNombre();
	String b=Empleado.empleado_menos_eficiente().getNombre();
	System.out.print("el empleado mas eficiente es: "+a+" y el menos eficiente es: "+b);
}





}

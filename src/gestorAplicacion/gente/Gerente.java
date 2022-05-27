package gestorAplicacion.gente;

import static gestorAplicacion.restaurante.Caja.cantidad_cajas;

public class Gerente extends Persona {
	
	//constructor
	
	public Gerente(int cedula,String nombre,int telefono) {
		super(cedula,nombre,telefono);
	}
	
	//metodos
	
public int arqueo_de_caja_global() {
	int res = 0;
	for (int i = 0; i < cantidad_cajas; i++) {
		int x = 0;
		int[] ingresos = new int[0];
		for (int n : ingresos) {
			x += n;
		}
		//realiza un arqueo de caja de forma global,
		//es decir, realiza el arqueo de caja para todas las cajas
		//y al final suma los resultados

	}
	return res;
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
package uiMain;
import java.util.Scanner;

import gestorAplicacion.gente.Empleado;
import gestorAplicacion.gente.Gerente;

public class ClaseUi {
	
	static Scanner R = new Scanner(System.in);
	
	//nombrar gerente
	
	public static boolean nombrar_gerente() {
		System.out.print("\n\ncedula: ");
		int cedula= R.nextInt();
		System.out.print("\nnombre: ");
		String nombre= R.nextLine();
		System.out.print("\ntelefono: ");
		int telefono= R.nextInt();
		System.out.print("\ncontraseña: ");
		String contraseña= R.nextLine();
		Gerente gerente=new Gerente(cedula,nombre,telefono,contraseña);
		return false;
	}
	
	//inicio de sesion empleado
	
	public static boolean inicio_Sesion_empledo(int nemp) { //recibe el numero de empleado, para verificar que si sea un nunmero de empleado
		if(nemp<=Empleado.numero_empleados && 0<nemp) {
			System.out.println("\nesta es la informacion del empleado asociado a este numero de empleado, si no coincide con su informacion cierre sesion\n");
			System.out.println(Empleado.lista_empleados.get(nemp-1).informacion());
			return opciones_empleado();	
		}
		else {
			System.out.println("\nEste numero de empleado no es valido, ingrese nuevamente\n");
			return false;
		}
		
	}
	
	//inicio de sesion gerente
	public static boolean inicio_Sesion_gerente(int contraseña) { //recibe el numero de empleado, para verificar que si sea un nunmero de empleado
		if(contraseña==Gerente.arr[0].getConstraseña_gerente()) {
			return opciones_gerente();	
		}
		else {
			System.out.println("\nEste contraseña no es valida, ingrese nuevamente\n");
			return false;
		}
		
	}
	
	//es lo que el empleado puede realizar mientras esta en el sistema
	
	public static boolean opciones_empleado() {
		System.out.print("\nseleciones una opcion: \n\n (1) tomar Orden \n (2) arqueo de caja \n (3) cerrar sesion \n\n respuesta: ");
		int opcion= R.nextInt();
		
		switch(opcion) {
		case 1:
			System.out.println("\ntomando orden");
			return true;
		case 2:
			System.out.println("\narqueo de caja");
			return true;
		case 3:
			System.out.println("\ncerrando  sesion\n");
			return false;
		}
		return false;
	}
	
	/////////////////////////////////////////////////////////////////////////
	
	//es lo que el gerente puede realizar mientras esta en el sistema
	
	public static boolean opciones_gerente() {
		System.out.print("\nselecione una opcion: \n\n (1) arqueo de caja global \n (2) arqueo de caja \n (3) contratar empleado"
				+ "\n (4) despedir empleado \n (5) despido inteligente \n (6) cerrar sesion \n\n respuesta: ");
		
		int ob= R.nextInt();
		
		switch(ob) {
		case 1:
			System.out.println("tomando orden");
			return true;
		case 2:
			System.out.println("arqueo de caja");
			return true;
		case 3:
			System.out.println("arqueo de caja global");
			return true;
		case 4:
			System.out.println("despidiendo empleado");
			return true;
		case 5:
			System.out.println("arqueo de caja global");
			return true;
		case 6:
			System.out.println("\ncerrando  sesion\n");
			return false;
        }
		return false;
		
	}
	
	//////////////////////////////////////////////////////
	
	public static void matanga() {
		System.out.print("El despido inteligente se encarga de despedir al empleado con peor rendimiento \nseguro de que quiere continuar? \n\n (1)si \n (2)no \n Respuesta: ");
		int confirmacion= R.nextInt();
		switch(confirmacion) {
		case 1:
			System.out.println("realizando despido inteligente");
			break;
		case 2:
			System.out.println("volviendo al menu principal");
			break;
	     }
	}
		
		
//en esta clase se implementa lo necesario para la interfaz generica por consola
	public static void main (String[] args) {
		Empleado e=new Empleado(1,"juan",1);
		Gerente g=new Gerente();
		boolean estado_programa=true;
		
		do {
		System.out.print("Selecione una opcion: \n\n (1) iniciar sesion como empleado \n (2) iniciar sesion como Gerente \n (3) nombrar gerente \n (4) cerrar programa \n\n Respuesta: ");
		
		Scanner R = new Scanner(System.in);

		
		int Respuesta = R.nextInt(); //respuesta
		
			switch(Respuesta) {
			
			//en caso de que sea tipo empleado
			case 1:
				boolean sesion=true; //estado de seion del empleado
				System.out.print("\nbienvenido Empleado, digite su numero de empleado: ");
				int nemp = R.nextInt(); //numero de empleado
				do {
					sesion=inicio_Sesion_empledo(nemp);
				}
				while(sesion==true);
				
				break;
			
			//en caso de que sea tipo gerente
			case 2:
				boolean sesiong=true; //estado de sesion gerente
				System.out.print("\nbienvenido Gerente, dijite la contraseña de gerente para poder acceder: ");
				int contraseña = R.nextInt(); //contraseña gerente
				do {
					sesiong=inicio_Sesion_gerente(contraseña);
				}
				while(sesiong==true);
				
				break;
				
			case 3:
				System.out.print("\n ingrese los datos del nuevo gerente");
				boolean estado=true;
				do {
					nombrar_gerente();
				}
				while(estado==true);
				
				break;
		     	
			case 4:
				System.out.print("\n cerrando programa :) ");
				estado_programa=false;
		     	break;
		     	
			default:
				System.out.println("\n opcion invalida \n");
	        }
		
          }
		
		while(estado_programa==true);
		
        }
}


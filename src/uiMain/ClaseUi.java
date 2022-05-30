package uiMain;
import java.util.ArrayList;
import java.util.Scanner;

import gestorAplicacion.gente.Empleado;
import gestorAplicacion.gente.Gerente;
import gestorAplicacion.restaurante.Platillo;
import gestorAplicacion.restaurante.ingredientes;

public class ClaseUi {
	
	static Scanner R = new Scanner(System.in); //para los int
	static Scanner N = new Scanner(System.in); //para los String
	
//Nombrar gerente, este metodo se encarga de ingresar la informacion del nuevo gerente y eliminar la del anterior
	
	public static boolean nombrar_gerente() {
		System.out.print("\n\ncedula: ");
		int cedula= R.nextInt();
		System.out.print("\nnombre: ");
		String nombre= N.nextLine();
		System.out.print("\ntelefono: ");
		int telefono= R.nextInt();
		System.out.print("\ncontraseña: ");
		String contraseña= N.nextLine();
		Gerente gerente=new Gerente(cedula,nombre,telefono,contraseña);
		return false;
	}
	
///////////////////////////////////////////////////////////////////////////////////	
	
//inicio de sesion empleado, recibe el numero del empleasdo y verifica que este en la lista de empleados
	
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
	
///////////////////////////////////////////////////////////////////////////////////	
	
//inicio de sesion gerente, recibe una contraseña para verificar que se trate del mismisimo gerente en persona
	
	public static boolean inicio_Sesion_gerente(String contraseña) { 
		if(contraseña.equals(Gerente.arr[0].getConstraseña_gerente())) {
			return opciones_gerente();	
		}
		else {
			System.out.println("\nEste contraseña no es valida, ingrese nuevamente\n");
			return false;
		}
		
	}
	
///////////////////////////////////////////////////////////////////////////////////		
	
//lista de ingredientes, imprime una lista con todos los ingredientes y sus precios
	
	public static void lista_ingredientes() {
    	for (int l=0;l<ingredientes.lista_ingredientes.size();l++) {
    		System.out.println(l+1+") ingrediente: "+ingredientes.lista_ingredientes.get(l).getTipo()+" precio de venta: "+ingredientes.lista_ingredientes.get(l).getPrecio_compra()*2+
    				" cantidad: "+ingredientes.lista_ingredientes.get(l).getCantidad()+"\n");
    	}
    }
	
///////////////////////////////////////////////////////////////////////////////////	
	
//construir platillo
	
	public static Platillo crear_platillo() {
		ArrayList<ingredientes> ingredientes_platillo = new ArrayList<ingredientes>();
		Platillo platillo=new Platillo(ingredientes_platillo);
		boolean x=true;
		do {
			System.out.println("\ningredientes en el platillo :\n");  //se imprime una pequeña lista con los ingredientes que tiene el platillo
			for (int l=0;l<ingredientes_platillo.size();l++) {
				System.out.println(ingredientes_platillo.get(l).getTipo());
			}
			System.out.print("\nseleccione una opcion: \n\n(1)añadir ingrediente \n\n(2)retirar ingrediente \n\n(3)terminar platillo\n\nrespuesta: ");
			int res=R.nextInt();
			switch(res) {
			case(1):
				System.out.println("");
			    lista_ingredientes();
			    System.out.print("seleccione el ingrediente que va a añadir: ");
			    int ingre=R.nextInt();            //numero correspondiente al lugar en la lista que ocupa el ingredientes
			    
			    //en caso de que se tenga en inventario el ingrediente
			    if(ingre>0 && ingredientes.lista_ingredientes.size()>=ingre) {
			    	System.out.println(platillo.anadirIngrediente(ingredientes.lista_ingredientes.get(ingre-1)));
			    }
			    //en caso de que no haya inventario 
			    else {
			    	System.out.println("\nese ingrediente no se encuentra en la lista de intregientes");
			    }
			  
			    break;
			case(2):
				if (ingredientes_platillo.size()>0) {
					System.out.println("\nseleccione el ingrediente que va a retirar");
					for (int l=0;l<ingredientes_platillo.size();l++) {
						System.out.println(l+1+") "+ingredientes_platillo.get(l).getTipo());
					}
					System.out.println("\nnumero de ingrediente");
				    int ingre_ret=R.nextInt();
				    
				    if(0<ingre_ret && ingre_ret<=ingredientes_platillo.size()) {
				    	platillo.retirarIngrediente(ingredientes.lista_ingredientes.get(ingre_ret-1));
				    }
				    
				    else {
				    	System.out.println("ese numero de ingrediente no esta en el platillo");
				    }
				
				}
				else {
					System.out.println("\nerror este platillo no cuenta con ingredientes");
				}
			    break;
			case(3):
				if(ingredientes_platillo.size()==0) {
					System.out.println("\neste platillo no tiene ingredientes\n");
					x=false;
				}
				else {
					System.out.println("platillo terminado");
					x=false;
				}
			    break;
			}
			
		}
		while(x==true);
		
		if (ingredientes_platillo.size()>1) {                       //aqui se crea el platillo con los ingredientes que añadimos anteriormente
			
			return platillo;
		}
		else {
			System.out.print("platillo sin ingredientes");       //se imprime en caso de que no se pongan ingredientes, se retorna un null
			return null;
		}
	}
	
/////////////////////////////////////////////////////////////////////////
	
//es lo que el gerente puede realizar mientras esta en el sistema
	
	public static boolean opciones_gerente() {
		System.out.print("\nselecione una opcion: \n\n (1) arqueo de caja global \n (2) arqueo de caja \n (3) contratar empleado"
				+ "\n (4) despedir empleado \n (5) despido inteligente \n (6) cerrar sesion \n\n respuesta: ");
		
		int ob= R.nextInt();
		
		switch(ob) {
		case 1:
			System.out.println("arqueo de caja global");
			return true;
		case 2:
			System.out.println("arqueo de caja");
			return true;
		case 3:
			System.out.println("ingrese los datos del empleado que desea contratar ");
			System.out.print("\n\ncedula: ");
			int cedula_e= R.nextInt();
			System.out.print("\nnombre: ");
			String nombre_e= N.nextLine();
			System.out.print("\ntelefono: ");
			int telefono_e= R.nextInt();
			Empleado e=new Empleado(cedula_e,nombre_e,telefono_e);
			return true;
		case 4:
			System.out.println("\nverificando lista de empleados..");
			if(Empleado.lista_empleados.size()>0) {
				System.out.print("\ndigite el numero del empleado al que quiere despedir: ");
				int nu_e= R.nextInt(); //numero de empleado que se piensa despedir
				if(nu_e>0 && nu_e<=Empleado.lista_empleados.size()) {
					Gerente.arr[0].despedir_empleado(Empleado.lista_empleados.get(nu_e-1));
				}
				else {
					System.out.println("\nerror, ese numero de empleado no existe \n");
				}
			}
			else {
				System.out.println("\nerror la lista de empleados se encuentra vacia, para poder despedir empleados primero debe contratar empleados\n");
			}
			
			return true;
		case 5:
			System.out.print("\nel despido inteligente se encarga de despedir al empleado con peor rendimiento, seguro que quiere continuar?: \n\n(1)si\n(2)no \n\nRespuesta: ");
			int confirmacion= R.nextInt();
			switch(confirmacion) {
			case 1:
				System.out.println("\nverificando lista de empleados..\n");
				if(Empleado.lista_empleados.size()>0) {	
				System.out.println("\nrealizando despido inteligente");
				Gerente.arr[0].despido_inteligente();
				}
				else {
				System.out.println("\nerror la lista de empleados se encuentra vacia, para poder despedir empleados primero debe contratar empleados\n");
				}
				break;
			case 2:
				System.out.println("\nvolviendo al menu principal\n");
				break;
		     }
			
			return true;
		case 6:
			System.out.println("\ncerrando  sesion\n");
			return false;
        }
		return false;
		
	}

/////////////////////////////////////////////////////////////////////////
	
//es lo que el empleado puede realizar mientras esta en el sistema
	
	public static boolean opciones_empleado() {
		System.out.print("\nseleciones una opcion: \n\n (1) tomar Orden \n (2) arqueo de caja \n (3) cerrar sesion \n\n respuesta: ");
		int opcion= R.nextInt();
		
		switch(opcion) {
		case 1:
			System.out.println("seleccione una opcion: \n\n(1)añadir platillo \n(2)retirar platillo \n(3)cancelar orden\n");
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
	
///////////////////////////////////////////////////////////////////////////////////	
	
//en esta clase se implementa lo necesario para la interfaz generica por consola
	
	public static void main (String[] args) {
		ingredientes ing1=new ingredientes(1,0,"chococola");
		ingredientes ing2=new ingredientes(1,44,"papa");
		ingredientes ing3=new ingredientes(1,44,"jd");
		System.out.print(ingredientes.lista_ingredientes.size());
		//System.out.println(ing1.verificar_inventario());
		//Platillo a=new Platillo();
		//System.out.println(a.anadirIngrediente(ing1));
		Empleado e=new Empleado(1,"juan",1);
		Gerente g=new Gerente();
		
		lista_ingredientes();
		//crear_platillo();*/
		
		/*boolean estado_programa=true;
		do {
		System.out.print("Selecione una opcion: \n\n (1) iniciar sesion como empleado \n (2) iniciar sesion como Gerente \n (3) nombrar gerente \n (4) cerrar programa \n\n Respuesta: ");

		
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
				String contraseña = N.nextLine(); //contraseña gerente
				do {
					sesiong=inicio_Sesion_gerente(contraseña);
				}
				while(sesiong==true);

				break;
				
			case 3:
				//System.out.print("\n ingrese los datos del nuevo gerente");
				boolean estado=true;
				do {
					System.out.print("\n ingrese los datos del nuevo gerente");
					estado=nombrar_gerente();
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
		*/
        }
        
}


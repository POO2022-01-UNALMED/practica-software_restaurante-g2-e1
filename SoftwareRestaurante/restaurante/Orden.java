package restaurante;
import java.util.ArrayList; 
import java.util.Collections;
import gente.*;
import java.lang.Math;

public class Orden {
	private ArrayList<Platillo> platillos = new ArrayList<Platillo>();
	private int numero_orden;
	private int precio_total;
	private Cliente cliente;
	private int propina;
	private static int cantidad_orden = 0;
	
	
	//constructor 
	public Orden() {
		this(new ArrayList<Platillo>(), null, 0);
	}
	public Orden(ArrayList<Platillo> platillos,  Cliente cliente) {
		this(platillos, cliente, 0);
	}
	public Orden(ArrayList<Platillo> platillos,  Cliente cliente, int propina) {
		this.platillos = platillos;
		int x = 0;
		for(Platillo i : platillos) {
			x += i.getPrecio();
		}
		x += propina; 
		precio_total = x;
		this.cliente = cliente;
		this.propina = propina;
		numero_orden = cantidad_orden;
		cantidad_orden ++;													// se tiene cantidad de orden y numero de orden por separado porque 
																			// uno me sirve para la instancia y el otro a modo de contador para 
																			// saber cuantas ordenes han sido creadas
	}
	
	
	//metodos set 
	public ArrayList<Platillo> getPlatillos(){
		return platillos;
	}
	public int getNumero_orden() {
		return numero_orden;
	}
	public int getPrecio_total() {
		return precio_total;
	}
	public Cliente getCliente() {
		return cliente;
	}
	public int getPropina() {
		return propina;
	}
	public static int getCantidad_orden() {
		return cantidad_orden;
	}
	
	
	
	//metodos set
	public void anadirPlatillos(Platillo platillo) {
		platillos.add(platillo);
		precio_total += platillo.getPrecio();                           // aumento el precio 
	}
	public void retirarPlatillo(Platillo platillo) {
		for (Platillo i: platillos) {
			if (i == platillo) {
				precio_total -= platillo.getPrecio();                   //quito el precio del platillo
				for (ingredientes e: platillo.getIngredientes()) {      // elimino ingredientes 1 por 1 para poder tenerlos otra vez en el inventario
					platillo.retirarIngrediente(e);
				}
				platillos.remove(platillos.indexOf(platillo));
			}
			break;
		}
	}
	public void descuento() {
		if (precio_total > 100000) {
			precio_total =  (int) Math.round(precio_total * 0.95);              //descuento del 5% por cantiad de dinero gastado
		}
		else if (platillos.size() > 50) {
			precio_total =  (int) Math.round(precio_total * 0.90);              //descuento del 10% por cantidad de compras
		}
		// falta descuento por ser un cliente especifico
	}
	public void cancelar_orden() {														//cambiar cancelar orden
		for (Platillo i: platillos) {
			retirarPlatillo(i);
		}
	}
	public void duplicar(Platillo platillo) {
		
		for (int i= 0; i < platillo.getIngredientes().size(); i++) {
			if (platillo.getIngredientes().get(i).verificar_inventario()) {
				if (i == platillo.getIngredientes().size()-1) {
					Platillo x = new Platillo(platillo.getIngredientes());
					anadirPlatillos(x);
				}
			}
		}
	}
}

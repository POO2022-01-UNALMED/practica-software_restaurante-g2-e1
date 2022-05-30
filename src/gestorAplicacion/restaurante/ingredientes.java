package gestorAplicacion.restaurante;

import java.util.ArrayList;

import gestorAplicacion.gente.Empleado;

public class ingredientes {
	private int precio_compra; // precio al cual el proveedor vende los articulos
	private int cantidad;
	private String tipo;
	public static ArrayList<ingredientes> lista_ingredientes = new ArrayList<ingredientes>();

	public ingredientes(int precio_compra, int cant, String tipo) {
		for (ingredientes i: lista_ingredientes) {
			if(tipo == i.tipo) {
				nosepuede();
			}
			else {
				if (i == lista_ingredientes.get(lista_ingredientes.size()-1)) {
					this.precio_compra = precio_compra;
					this.cantidad = cant;
					this.tipo = tipo;
					lista_ingredientes.add(this);
				}
			}
		}
	}
	
	public String getTipo() {
		return this.tipo;
	}
	public int getCantidad(String tipo) {// Aqui directamente escogemos cual tipo de carne queremos saber la cantidad
		if (this.tipo.equals(tipo)) {
			this.cantidad = +cantidad;
			return this.cantidad;
		} else {
			return 0;
		}
	}
	
	public int getPrecio_compra() {
		return precio_compra;
	}
	
	
	public void setCantidad(int cantidad) {
		this.cantidad = cantidad;

	}

	public void setTipo(String type) {
		this.tipo = type;
	}

	public void setPrecio_compra(int precio_compra) {
		this.precio_compra = precio_compra;
	}

	public String nosepuede() {
		return "no se puede a�adir un ingrediente repetido";
	}

	public static String anadirCantidad(int cantidad, String tipo) { // busca en la lista de lista_ingredientes y cambia la cantidad.
		for (ingredientes i: lista_ingredientes) {
			if (i.tipo == tipo) {
				i.cantidad += cantidad;
				return "Se aumento el stock de: " + tipo + " en " +  cantidad + " unidades";
			}
			else {
				return "ingrediente inexistente";
			}
		}
		return null;
	}
	
	public String anadirCantidad(int cantidad) { // a�ade la cantidad en la que se aumenta la cantidad de unidades de esta instancia
		this.cantidad += cantidad;
		return "Se aumento el stock de: " + tipo + " en " +  cantidad + " unidades";
	}

	public boolean verificar_inventario() {
		if (cantidad > 0) {
			return true;
		} else {
			return false;
		}
	}

}
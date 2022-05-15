package restaurante;

public enum ingredientes {
	//ingredientes
	carne_hamburguesa(2000, 0), salchicha(1000, 0), pan_hamburguesa(500, 0), pan_perro(400, 0);
	
	
	//atributos
	private int precio;
	private int cantidad;
	
	
	//constructor
	private ingredientes(int precio, int cantidad) {
		this.precio = precio;
		this.cantidad = cantidad;
	}
	
	
	//metodos get
	public int getPrecio() {
		return precio;
	}
	public int getCantidad() {
		return cantidad;
	}
	
	
	//metodos set
	public void setPrecio(int precio) {
		this.precio = precio;
	}
	public void anadircantidad(int cantidad) {
		this.cantidad += cantidad;
	}
	
	
	
	//metodos 
	public boolean verificar_inventario() {
		if (cantidad > 0) {
			return true;
		}
		else {
			return false;
		}
	}
}

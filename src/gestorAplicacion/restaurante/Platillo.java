package gestorAplicacion.restaurante;
import java.util.ArrayList; 
import java.util.Collections;
public class Platillo {
	private ArrayList<ingredientes> ingredientes = new ArrayList<ingredientes>(); //ingredientes es un enum, agragar despues
	private int precio = 0;
	
	//get precio se cambio por getprecio_venta
	
	//constructor
	public Platillo() {
		
	}
	public Platillo(ArrayList<ingredientes> ingredientes) {
		this.ingredientes = ingredientes;
		int x = 0;
		for(ingredientes i: ingredientes) {
			x += i.getPrecio_venta();
		}
		precio = x;
	}
	//metodos get
	public ArrayList<ingredientes> getIngredientes(){
		return ingredientes;
	}
	public int getPrecio() {
		return precio;
	}
	
	
	
	//metodos set
	public String anadirIngrediente(ingredientes ingrediente) {
		if (ingrediente.verificar_inventario() == true) {
			ingrediente.anadirCantidad(-1,ingrediente.getTipo());      // resto al inventario
			ingredientes.add(ingrediente);		 //aï¿½ado a la lista de ingredientes
			precio += ingrediente.getPrecio_venta();     // aumento el precio del platillo
			return "añadido con exito";
		}
		else {
			return "no hay existencias de este producto";
		}
	}
	public String retirarIngrediente(ingredientes ingrediente) {
		for (int i = 0; i < ingredientes.size(); i++) {
			if (ingredientes.get(i) == ingrediente) {          //compruebo si existe ese elemento en la lista
				ingredientes.remove(i);
				ingrediente.anadirCantidad(1,ingredientes.get(i).getTipo());
				precio -= ingrediente.getPrecio_venta();
				return "ingrediente eliminado";
			}	
		}
		return "no existe tal ingrediente";
	}
	

}
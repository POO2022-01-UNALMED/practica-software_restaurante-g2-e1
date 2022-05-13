package restaurante;
import java.util.ArrayList; 
import java.util.Collections;
import gente.*;

public class Orden {
	private ArrayList<Platillo> platillos = new ArrayList<Platillo>();
	private int numero_orden;
	private int precio_total;
	private int factura;
	private Cliente cliente;
	private int propina;
}

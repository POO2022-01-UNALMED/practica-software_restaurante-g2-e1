package gestorAplicacion.restaurante;
import java.util.ArrayList; 
import java.util.Collections;
import java.io.Serializable;
public class Caja implements Serializable{
	private int efectivo;
	public ArrayList<Integer> ingresos;
	private ArrayList<Integer>  egresos;    
	static private ArrayList<Integer>  totalingresos = new ArrayList<Integer>();
	static private ArrayList<Integer>  totalegresos = new ArrayList<Integer>();
	
	
	//contructores
	public Caja() {
		this(0,new  ArrayList<Integer>(),new  ArrayList<Integer>());
	}
	public Caja(int efectivo, ArrayList<Integer> ingresos, ArrayList<Integer> egresos) {
		this.efectivo = efectivo;
		this.ingresos = ingresos;
		this.egresos = egresos;	
	}

	
	
	//metodos get
	public int getEfectivo() {
		return efectivo;
	}
	public ArrayList<Integer> getIngresos(){
		return ingresos;
	}
	public ArrayList<Integer> getEgresos(){
		return egresos;
	}
	public static ArrayList<Integer> getTotalIngresos(){
		return totalingresos;
	}
	
	public static ArrayList<Integer> getTotalEgresos(){
		return totalegresos;
	}

	
	
	//metodos set 
	public void setEfectivo(int n) {
		efectivo = n;
	}

	public void nuevoIngreso(int n) {
		ingresos.add(n);
		totalingresos.add(n);
	}
	public void nuevoEgreso(int n) {
		egresos.add(n);
		totalegresos.add(n);
	}
	
	
	//metodos reales
	public String devuelta(int n, Orden orden) {
		if (n > orden.getPrecio_total()) {
			int w = n - orden.getPrecio_total();   //devuelta 
			this.nuevoIngreso(orden.getPrecio_total());     //agrego ingresos a la lista
			return  w + "";                    // convierto el int a string 
		}
		else {
			return "Cantidad Insuficiente";
		}
	}
	
	public int arqueo() {
		int x = 0;
		for (int n: ingresos) {
			x += n;
		}
		return x;
	}
	
	public int arqueoTotal() {
		int x = 0;
		for (int n: totalingresos) {
			x += n;
		}
		return x;
	}
}
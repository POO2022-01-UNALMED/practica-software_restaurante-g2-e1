package gestorAplicacion.restaurante;

import java.util.ArrayList;

import gestorAplicacion.gente.Empleado;

public class ingredientes{
    private int precio_compra; //precio al cual el proveedor vende los articulos
    private int precio_venta; //precio al cual vendemos los articulos 
    private int cantidad; 
    private String tipo;
    public static ArrayList<ingredientes> lista_ingredientes = new ArrayList<ingredientes>();
    public static ArrayList<String> lista_tipos_ingredientes = new ArrayList<String>();
    public static ArrayList<Integer> lista_precios = new ArrayList<Integer>();
    
    public ingredientes(int precio_compra,int cant, String tipo){ // Constructor 
    	if (!lista_tipos_ingredientes.contains(tipo)){
    		this.precio_compra=precio_compra;
            this.cantidad=cant;
            this.tipo=tipo;
            precio_venta=precio_compra*2;
            lista_tipos_ingredientes.add(tipo);
            lista_precios.add(precio_venta);
            lista_ingredientes.add(this);
    	}
    	else {
    		nosepuede();
    	}
    	}
    
    public String nosepuede() {
    	return "no se puede añadir un ingrediente repetido";
    }
    
    public void setPrecio_compra(int precio_compra) {
        this.precio_compra=precio_compra; 
    }
    
    public int getPrecio_compra(){
        return precio_compra;
    }
    
    public int getPrecio_venta() {
        return precio_venta;
    }
    
    public String anadirCantidad(int cantidad,String tipo) {// Escogemos el tipo de carne al cual se quiere aumentar el stock
    	for (int j=0;j<lista_ingredientes.size();j++) {
    		
        if(lista_ingredientes.get(j).equals(tipo)){
            this.cantidad=this.cantidad+cantidad;
            return "Se aumento el stock de: "+ tipo + " en " + cantidad + " unidades";
        }
        
        else{
            return "ingrediente Erroneo";
        }
        
        }
    	
		return null;
    }
    
    public int getCantidad(String tipo) {// Aqui directamente escogemos cual tipo de carne queremos saber la cantidad
        if(this.tipo.equals(tipo)){
            this.cantidad=+cantidad;
            return this.cantidad;
        }
        else{
            return 0;
        }
    }
    
    public void setCantidad(int cantidad) {
        this.cantidad=cantidad;
        
    }
    
    public void setTipo(String type){
        this.tipo=type;
    }
    
    public String getTipo(){
        return this.tipo;
    }
    
    public boolean verificar_inventario() {
        if (cantidad > 0) {
			return true;
		}
		else {
			return false;
		}
    }

}
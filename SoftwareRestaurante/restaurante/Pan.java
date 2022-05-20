package restaurante;

public class Pan extends ingredientes {
    private int precio;
    private int cantidad;
    private String tipo;

    public Pan(int pre, int cant, String tp){ // Constructor 
        this.precio=pre;
        this.cantidad=cant;
        this.tipo=tp;
    }
    @Override
    public void setPrecio(int precio) {
        this.precio=precio; 
    }

    @Override
    public int getPrecio() {
        return this.precio;
    }

    @Override
    public String anadirCantidad(int cantidad,String tipo) {// Escogemos el tipo de pan al cual se quiere aumentar el stock
        if(this.tipo.equals(tipo)){
            this.cantidad=this.cantidad+cantidad;
            return "Se aumento el stock del Pan tipo "+ tipo;
        }
        else{
            return "Pan Erroneo";
        }
        
    }

    @Override
    public int getCantidad(String tipo) {// Aqui directamente escogemos cual tipo de pan queremos saber la cantidad
        if(this.tipo.equals(tipo)){
            this.cantidad=+cantidad;
            return this.cantidad;
        }
        else{
            return 0;
        }
    }

    @Override
    public void setCantidad(int cantidad) {
        this.cantidad=cantidad;
        
    }
    @Override
    public void setTipo(String type){
        this.tipo=type;
    }
    @Override
    public String getTipo(){
        return this.tipo;
    }
    @Override
    public boolean verificar_inventario() {
        if (cantidad > 0) {
			return true;
		}
		else {
			return false;
		}
    }
    
}
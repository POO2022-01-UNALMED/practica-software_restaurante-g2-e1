package restaurante;

public abstract class ingredientes {
    //Clase para reformular ingredientes, se puede formular como una clase abstracta
    //Con los metodos get set precio de cada ingrediente
    //de esta forma es posible crear una lista de ingredientes tanto para los platillos como
    //para  los proveedores
    public abstract void setPrecio(int precio);
    public abstract int getPrecio();
    public abstract void setCantidad(int cantidad); // Probablemente no se use pero la pongo de igual froma
    public abstract int getCantidad(String tipo); 
    public abstract String anadirCantidad(int cantidad, String tipo);
    public abstract void setTipo(String type);
    public abstract String getTipo();
	public abstract boolean verificar_inventario();
    


}

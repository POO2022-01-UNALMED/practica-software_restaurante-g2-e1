package gestorAplicacion.restaurante;

import java.util.ArrayList;

public class mainprueba {
    public static void main(String[] args) {
        System.out.println("PRUEBA DE INGREDIENTES Y CONSTRUCTORES");
       ingredientes carne1= new Carne(100, 15, "Salchicha");
        System.out.println(carne1.getCantidad("Salchicha"));
        carne1.anadirCantidad(5, "Salchicha");
        System.out.println(carne1.getCantidad("Salchicha"));
        System.out.println("PRUEBA DE PROVEEDORES");
        ingredientes carne2= new Carne(250, 30, "Hamburguesa");
        ingredientes carne3= new Carne(50,2,"Atun");

        Proveedor pv1 = new Proveedor("Juan");
        pv1.anadirArticulo(carne1);
        pv1.anadirArticulo(carne2);
        pv1.anadirArticulo(carne3);
        System.out.println(pv1.getArticulos().get(0).getPrecio());
        System.out.println(pv1.mostrarArticulos());
        System.out.println(carne2.anadirCantidad(2, "Hamburguesa"));

        System.out.println("PRUEBA DE PLATILLO Y ORDEN");
        ingredientes pan1= new Pan(25,10,"Pan Americano"); //Pan Americano es el pan de hamburguesa de toda la vida
        ingredientes mozarela = new Lacteos(30, 5, "Queso Mozzarela");
        //Platillo HamburguesaConQueso = new Platillo(new ArrayList<ingredientes>=(pan1,carne1,mozarela));
    }
}
package gestorAplicacion.gente;
import gestorAplicacion.restaurante.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
public class Proveedor {	 
    ArrayList<ingredientes> lista_arts= new ArrayList<ingredientes>();
    private String nombre;
    // Debido a la estructura de enum no es ��posible crear un constructor que contenga todos los elementos del enum e instacnciarlas
    // Hay que replantear clase Ingredientes 
    public Proveedor(String nombre){
        this.nombre=nombre;
    }

    public void setNombre(String name){
        this.nombre=name;
    }

    public String getNombre(){
        return this.nombre;
    }
    public void setArticulos(ingredientes ing){
        lista_arts.add(ing);
    }

    public ArrayList<ingredientes> getArticulos(){
        return this.lista_arts;
    }

    public void anadirArticulo(ingredientes ing){
        lista_arts.add(ing);
    }
    /*public String mostrarArticulos2(){
        String r1= "<===LISTA DE ARTICULOS===>";
        String r2="\n";
        String r3="";//para el tipo de ingrediente
        String r4="";//para el precio del ingrediente
        String r5="";//Unir el ingrediente y el precio
        String r6="";
        for(int i =0;i<=this.getArticulos().size()-1;i++){
            r3=this.getArticulos().get(i).getTipo();
            r5+=String.join(r2, r3);
            r5+="|"+r2;
            r4=String.valueOf(this.getArticulos().get(i).getPrecio());  
            r6+=String.join(r2,r4); 
            r6+=r2;
        }
        //return r1+r2+"===Ingrediente==="+r2+r5+"===Precio==="+r2+r6;
        return r1+r2+"===Ingrediente==="+"|"+"===Precio==="+r2+r5+r6;
        //return r1+r2+"===Ingrediente==="+"|"+"===Precio==="+r2+r5;
        
    } */
    public String mostrarArticulos(){
        String r1= "<===LISTA DE ARTICULOS===>";
        String r2="\n";//Nueva Linea
        String r3="";//para el tipo de ingrediente
        String r4="";//para el precio del ingrediente
        String r5="";//Unir el ingrediente y el precio
        String r6="";//Unir y poner en nueva linea
        for(int i =0;i<=this.getArticulos().size()-1;i++){
            r3=this.getArticulos().get(i).getTipo();
            r4=String.valueOf(this.getArticulos().get(i).getPrecio());  
            r5=r3+"=>"+r4+"$"+r2;
            r6+=String.join(r2, r5);         
        }
        return r1+r2+"Ingrediente"+"|"+"Precio"+r2+r6;   
    } 

  
    }  
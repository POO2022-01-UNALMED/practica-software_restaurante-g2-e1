package baseDatos;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

import gestorAplicacion.*;
import gestorAplicacion.gente.Cliente;
import gestorAplicacion.gente.Empleado;
import gestorAplicacion.gente.Gerente;
import gestorAplicacion.restaurante.Caja;
import gestorAplicacion.restaurante.Orden;
import gestorAplicacion.restaurante.Platillo;
import gestorAplicacion.restaurante.horarios;
import gestorAplicacion.restaurante.ingredientes;

public class Deserializador {
    /**
     * Utilizamos clases genericas para permitir reutilizar la funcion para todas
     * las clases del proyecto
     * 
     * @param <E>       el generico se usa para poder agredar las clases que se
     *                  crearon
     * @param lista     Una lista de objetos
     * @param className El nombre de la clase que queremos usar como nombre del
     *                  archivo
     * @throws ClassNotFoundException
     */

    public static <E> void deserializar(ArrayList<E> obj, String className) throws ClassNotFoundException {
        FileInputStream fileIn;
        try {
            // Creamos una cadena con la ruta del archivo que vamos a cargar
            String path = System.getProperty("user.dir") + "/src/baseDatos/temp/" + className + ".txt";
            System.out.println(path);
            // utilizamos un file para crear este archivo si no existe aun
            // File archivo = new File(path);
            // archivo.createNewFile(); // Crea un nuevo archivo si no existe
            fileIn = new FileInputStream(path);
            ObjectInputStream in = new ObjectInputStream(fileIn);
            ArrayList<E> obj2 = (ArrayList<E>) in.readObject();
            in.close();
            fileIn.close();

            for (E l : obj2) {
                obj.add(l);
            }
            /*
             * for(int i=0;i<obj.size();i++){
             * obj.add(obj.get(i));
             * }
             */
        } catch (

        FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            System.out.println("Esta vacio");
        }
        System.out.println("Deserilizando " + className);
    }

    public static void deserializarTodo() throws ClassNotFoundException {
        // Deserializador.deserializar(Gerente.arr, "Gerente");
        Deserializador.deserializar(Empleado.lista_empleados, "Empleado");
        Deserializador.deserializar(ingredientes.lista_ingredientes, "ingredientes");

    }
}
package restaurante;
import java.util.ArrayList; 
import java.util.Collections;
import gente.*;

public class Turno {
	private Empleado empleado;
	private Caja caja;
	private String horario;
	public static ArrayList<Orden> lista_empleados = new ArrayList<Orden>();
	
	//constructor
	public Turno(Empleado empleado,Caja caja,String horario) {
		this.empleado=empleado;
		this.caja=caja;
		this.horario=horario;
	}
	
	//metodos get y set
	
	public Empleado getEmpleado(){
		return empleado;
	}
	
	public void setEmpleado(Empleado empleado) {
		this.empleado=empleado;
	}
	
	public Caja getCaja() {
		return caja;
	}
	
	public void setCaja(Caja caja) {
		this.caja=caja;
	}
	
	public String getHorario() {
		return horario;
	}
	
	public void setHorario(String horario) {
		this.horario=horario;
	}
	
}

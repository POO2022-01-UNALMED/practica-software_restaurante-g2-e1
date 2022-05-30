package gestorAplicacion.restaurante;

public enum horarios {
	horario1(9, 20), horario2(10, 18);//lunes a viernes, sadado y domingo
	
	private int inicio;
	private int fin;
	
	private horarios(int inicio, int fin) {
		this.inicio = inicio;
		this.fin  =fin;
	}
	
	public int getInicio() {
		return inicio;
	}
	public int getFinal() {
		return fin;
	}
	public void setInicio(int inicio) {
		this.inicio = inicio;
	}
	public void setFinal(int fin) {
		this.fin = fin;
	}
}

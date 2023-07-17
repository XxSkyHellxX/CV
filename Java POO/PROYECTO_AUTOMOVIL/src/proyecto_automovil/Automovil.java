
package proyecto_automovil;


public class Automovil {
    
    private String patente;
    private int anio, combustible,precio,tipoAutomovil,marca;

    public Automovil(String patente, int anio, int combustible, int precio, int tipoAutomovil, int marca) {
        this.patente = patente;
        this.anio = anio;
        this.combustible = combustible;
        this.precio = precio;
        this.tipoAutomovil = tipoAutomovil;
        this.marca = marca;
    }

    public Automovil() {
    }

    
    
    public String getPatente() {
        return patente;
    }

    public void setPatente(String patente) {
        this.patente = patente;
    }

    public int getAnio() {
        return anio;
    }

    public void setAnio(int anio) {
        this.anio = anio;
    }

    public int getCombustible() {
        return combustible;
    }

    public void setCombustible(int combustible) {
        this.combustible = combustible;
    }

    public int getPrecio() {
        return precio;
    }

    public void setPrecio(int precio) {
        this.precio = precio;
    }

    public int getTipoAutomovil() {
        return tipoAutomovil;
    }

    public void setTipoAutomovil(int tipoAutomovil) {
        this.tipoAutomovil = tipoAutomovil;
    }

    public int getMarca() {
        return marca;
    }

    public void setMarca(int marca) {
        this.marca = marca;
    }

   
    
    
}

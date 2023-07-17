package proyecto_automovil;

import java.util.ArrayList;

public class Camion extends Automovil {

    int capacidadCarga, cantidadEjes;
    ArrayList<Camion> listacamion = new ArrayList<>();
    public Camion(int capacidadCarga, int cantidadEjes, String patente, int anio, int combustible, int precio, int tipoAutomovil, int marca) {
        super(patente, anio, combustible, precio, tipoAutomovil, marca);
        this.capacidadCarga = capacidadCarga;
        this.cantidadEjes = cantidadEjes;
    }

    public Camion() {

    }

    public ArrayList<Camion> getListacamion() {
        return listacamion;
    }

    public void setListacamion(ArrayList<Camion> listacamion) {
        this.listacamion = listacamion;
    }

    public int getCapacidadCarga() {
        return capacidadCarga;
    }

    public void setCapacidadCarga(int capacidadCarga) {
        this.capacidadCarga = capacidadCarga;
    }

    public int getCantidadEjes() {
        return cantidadEjes;
    }

    public void setCantidadEjes(int cantidadEjes) {
        this.cantidadEjes = cantidadEjes;
    }

    public void agregar(Camion camion){
        listacamion.add(camion);
    }
    
    public void eliminar(){
        listacamion.remove(0);
    }

}

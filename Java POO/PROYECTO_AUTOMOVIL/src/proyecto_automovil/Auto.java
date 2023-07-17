package proyecto_automovil;

import java.util.ArrayList;

public class Auto extends Automovil {

    int kilometros, caballosDeFuerza;
    ArrayList<Auto> listaauto = new ArrayList<>();
    public Auto(int kilometros, int caballosDeFuerza, String patente, int anio, int combustible, int precio, int tipoAutomovil, int marca) {
        super(patente, anio, combustible, precio, tipoAutomovil, marca);
        this.kilometros = kilometros;
        this.caballosDeFuerza = caballosDeFuerza;
    }

    public Auto() {
    }

    public int getKilometros() {
        return kilometros;
    }

    public void setKilometros(int kilometros) {
        this.kilometros = kilometros;
    }

    public int getCaballosDeFuerza() {
        return caballosDeFuerza;
    }

    public void setCaballosDeFuerza(int caballosDeFuerza) {
        this.caballosDeFuerza = caballosDeFuerza;
    }

    public ArrayList<Auto> getListaauto() {
        return listaauto;
    }

    public void setListaauto(ArrayList<Auto> listaauto) {
        this.listaauto = listaauto;
    }

    public void agregarAuto(Auto auto){
        listaauto.add(auto);
    }
    
    public void eliminar(){
        listaauto.remove(0);
    }  

}

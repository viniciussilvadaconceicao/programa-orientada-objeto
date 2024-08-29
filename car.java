public class Car{
    string marca;
    string modelo;
    int year;
    boolean isRunning;
    int velocidade ;

    public Car(string marca, string modelo, int year){
        this.marca = marca;
        this.modelo = modelo;
        this.year = year;
        this.lsRunning = false;
        this.velocidade = 0;
    }
    // definindo os metodos
    // ligar o carro
    public void start(){
        if (!isRunning){
            lsRunning = True;
            System.out.println("Carro ligado");
        }
    }

    // desligar o carro
    public void stop(){
        if (isRunning){
            isRunning = false;
            System.out.println('Carro desligado');
        }

    // dirigir o carro
    public void drive(int distancia){
        if (isRunning){
            this.velocidade += distancia;
            system.out.println("o carro esta em uma velocidade de " +distancia+ "km/h");
    }
    }

    public static void main(string[] args){
        Car carro = new Car("fiat","uno", 2010);
        carro.start();
        carro.drive(50);
        carro.stop();
    }
}
package logicadeprogramacao.estruturadedadosjava;

public class EstruturaDeRepeticao {
    public static void main(String[] args) {
        int contador = 0;
        while (contador < 5) {

            System.out.println("while " + contador);
            contador++;
        }

        do {
            System.out.println("do while " + contador);
            contador++;

        } while (contador < 5);

        int i;
        for (i = 1; i <= 5; i++) {

            System.out.println("for " + i);
        }

    }
}

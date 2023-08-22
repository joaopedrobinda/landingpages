package logicadeprogramacao.estruturadedadosjava;

public class EstruturaDeDecisao {
    
    public static void main(String[] args) {    
    int a = 20;
    int b = 10;
    if (a < 10) {

        System.out.println(a);
    }
    else {

        System.out.println(b);
    }


    int dia = 5;
    String mensagem;
    switch (dia) {
        case 1:
            mensagem = "domingo";
            break;
        case 2:
            mensagem = "segunda";
        case 5:
            mensagem = "quinta";
            break;

        default:
            mensagem = "dia invalido";
            break;
        }    

        System.out.println(mensagem);

    }
}

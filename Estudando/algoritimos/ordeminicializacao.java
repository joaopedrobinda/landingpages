public class ordeminicializacao {

    static {
        System.out.println("só posso aparecer uma vez - static");
    }

    {
        System.out.println("apareco para cada instacia - em cima do construtor");
    }

    public ordeminicializacao() {
        System.out.println("contrutor - cada instancia também");
    }

    public static void main(String[] args) {
        ordeminicializacao objeto1 = new ordeminicializacao();
        System.out.println("primeiro objeto");
        ordeminicializacao objeto2 = new ordeminicializacao();
        System.out.println("segundo objeto");
    }

}

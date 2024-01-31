import java.util.ArrayList;

public class ordenacaoSelecao {
    public static void main(String[] args) {
        
        ArrayList<Integer> arr = new ArrayList<>();

        arr.add(3);
        arr.add(2);
        arr.add(1);
        arr.add(4);
        arr.add(5);

        System.out.println(ordenarSelecao(arr));

    }

    public static Integer buscarMenor(ArrayList<Integer> arr){
        Integer menor = arr.get(0);
        Integer menor_indice = 0;

        for (Integer i = 1; i < arr.size(); i++) {
            if (arr.get(i) < menor) {
                menor = arr.get(i);
                menor_indice = i;
            }
        }

        return menor_indice;
    }

    public static ArrayList<Integer> ordenarSelecao(ArrayList<Integer> arr){
        ArrayList<Integer> novaLista = new ArrayList<>();

        for (Integer i = arr.size(); i != 0; i--) {
            int indice = buscarMenor(arr);
            Integer menor = arr.get(indice);
            novaLista.add(menor);
            arr.remove(indice);
        }

        return novaLista;
    }

}

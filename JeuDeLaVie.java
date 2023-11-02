import java.util.Random;
import java.util.concurrent.TimeUnit;

public class JeuDeLaVie {
    static final int vivante = 1, morte = 0, taille = 25;
    static int generation = 1;
    static int[][] tab = new int[taille][taille];

    public static void print() {
        int celluleVivante = 0;

        System.out.print("\t\t\t\t\t\t\tGénération : " + generation++);
        for (int[] ints : tab) {
            for (int j = 0; j < tab[0].length; j++) {
                if (ints[j] == vivante)
                    celluleVivante++;
            }
        }
        System.out.println("\tCellules vivantes(🔵) : " + celluleVivante + "\n");

        for (int[] ints : tab) {
            System.out.print("\t\t\t\t");
            for (int j = 0; j < tab[0].length; j++) {
                if (ints[j] == vivante)
                    System.out.print("🔵 ");
                else
                    System.out.print("⚪ ");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void juge(int i, int j, int nbrVivante) {
        if (tab[i][j] == vivante) {
            if (1 >= nbrVivante || nbrVivante > 3)
                tab[i][j] = morte;
        } else {
            if (nbrVivante == 3)
                tab[i][j] = vivante;
        }
    }

    public static void engine() {
        int[][] copie = new int[tab.length][tab.length];
        int nbrVivante;
        for (int i = 0; i < tab.length; i++) {
            System.arraycopy(tab[i], 0, copie[i], 0, tab[0].length);
        }

        for (int i = 0; i < taille; i++) {
            for (int j = 0; j < taille; j++) {
                nbrVivante = 0;
                if ((j - 1 >= 0) && copie[i][j - 1] == vivante)
                    nbrVivante += 1;
                if ((i - 1 >= 0) && (j - 1 >= 0) && copie[i - 1][j - 1] == vivante)
                    nbrVivante += 1;
                if ((i - 1 >= 0) && copie[i - 1][j] == vivante)
                    nbrVivante += 1;
                if ((i - 1 >= 0) && (j + 1 <= taille - 1) && copie[i - 1][j + 1] == vivante)
                    nbrVivante += 1;
                if ((j + 1 <= taille - 1) && copie[i][j + 1] == vivante)
                    nbrVivante += 1;
                if ((i + 1 <= taille - 1) && (j + 1 <= taille - 1) && copie[i + 1][j + 1] == vivante)
                    nbrVivante += 1;
                if ((i + 1 <= taille - 1) && copie[i + 1][j] == vivante)
                    nbrVivante += 1;
                if ((i + 1 <= taille - 1) && (j - 1 >= 0) && copie[i + 1][j - 1] == vivante)
                    nbrVivante += 1;
                juge(i, j, nbrVivante);
            }
        }
    }

    public static void planeur() {
        tab[0][1] = vivante;
        tab[1][2] = vivante;
        tab[2][0] = vivante;
        tab[2][1] = vivante;
        tab[2][2] = vivante;
    }

    public static void lwss() {
        tab[0][0] = vivante;
        tab[0][3] = vivante;
        tab[1][4] = vivante;
        tab[2][0] = vivante;
        tab[2][4] = vivante;
        tab[3][1] = vivante;
        tab[3][2] = vivante;
        tab[3][3] = vivante;
        tab[3][4] = vivante;
    }

    public static void random() {
        Random rand = new Random();
        for (int i = 0; i < tab.length; i++) {
            for (int j = 0; j < tab[i].length; j++) {
                tab[i][j] = rand.nextInt(2);
            }
        }
    }

    public static void main(String[] args) {

        int speed = 1000;

        random();
        for (int i = 0; i < 100; i++) {
            try {
                TimeUnit.MILLISECONDS.sleep(speed);
                String os = System.getProperty("os.name");
                if (os.contains("Windows")) {
                    ProcessBuilder pb = new ProcessBuilder("cmd", "/c", "cls");
                    Process ps = pb.inheritIO().start();
                    ps.waitFor();
                } else {
                    ProcessBuilder pb = new ProcessBuilder("clear");
                    Process ps = pb.inheritIO().start();
                    ps.waitFor();
                }
            } catch (Exception e) {
                e.printStackTrace();
            }

            System.out.println("\t\t\t\t\t\t\t\t\tJeu de la vie\n");
            print();
            engine();
        }
    }
}

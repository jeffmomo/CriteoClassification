import java.io.*;

/**
 * Created by mdl94 on 28/03/2016.
 */
public class Kagglefy
{

    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new FileReader("pred.txt"));
        BufferedWriter bw = new BufferedWriter(new FileWriter("kaggle.out"));

        bw.write("Id,Predicted");
        bw.newLine();

        int id = 60000000;

        String tmp;
        while((tmp = br.readLine()) != null)
        {
            double d = Double.parseDouble(tmp);
            d = 1 / (1 + Math.exp(-d));

            bw.write(Integer.toString(id++));
            bw.write(",");
            bw.write(String.format("%.12f", d));
            bw.newLine();
        }
	bw.close();
    }
}


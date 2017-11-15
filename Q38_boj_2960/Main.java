import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Main {
    public static BufferedReader in  = new BufferedReader(new InputStreamReader(System.in));
    public static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
    public static int n;
    public static int k;
    public static ArrayList<Integer> primes = new ArrayList<>();
    public static void main(String args[])throws Exception{
        String line[] =in.readLine().split(" ");
        n = Integer.parseInt(line[0]);
        k = Integer.parseInt(line[1]);
        for(int i =2; i<n+1; i++) {
            primes.add(i);
        }
        int s=0;
        int t=2;
        int ans;
        while(s!=k&&t!=n+1) {
            for(int i =1; i<=n/t; i++) {
                int tmp = primes.indexOf(i*t);
                if (tmp == -1)continue;
                else ans =primes.remove(tmp);
            s++;
                if(s==k) out.write(ans+"");
            }
            t++;
        }
        in.close();
        out.close();

    }
}

mport java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static Map<Integer,Integer> m = new HashMap<>();
    public static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String args[])throws Exception {
        String[] line = in.readLine().split(" ");
        int n = Integer.parseInt(line[0]), p =Integer.parseInt(line[1]);
        m.put(n,1);
        while(true) {
            int cur = n;
            n = cal(cur,p);
            if(m.containsKey(n)) {
                System.out.println(m.get(n)-1);
                break;
            } else {
                m.put(n, m.get(cur)+1);
            }
        }
    }
    public static int cal(int cur,int p) {
        int c = cur;
        int sum =0;
        while (c>0) {
            sum += (int)Math.pow((c%10),p);
            c/=10;
        }
        return sum;
    }
}

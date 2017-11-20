import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Main {
    public static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    public static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
    public static ArrayList<Integer>[] cnjList;
    public static int v, e,cnt;
    public static boolean[] visit;
    public static void main(String args[])throws IOException {
        getInput();
        for (int c = 0; c<v; c++) {
            if(!visit[c])dfs(c);
            cnt ++;
        }
        System.out.println(cnt);
        out.write(cnt+'\n');
        in.close();
        out.close();
    }
    public static void getInput()throws IOException {
        String line[] = in.readLine().split(" ");
        v = Integer.parseInt(line[0]); e = Integer.parseInt(line[1]); 
        cnjList = new ArrayList[v];
        for(int i =0; i< v; i++) {
            cnjList[i] = new ArrayList<Integer>();
        }
        visit = new boolean[v];
        for(int i =0; i<v; i++)visit[i]=false;
        for(int i =0; i<e; i++) {
            int cur, nex;
            line = in.readLine().split(" ");
            cur = Integer.parseInt(line[0]); nex = Integer.parseInt(line[1]);
            cnjList[cur-1].add(nex);
            cnjList[nex-1].add(cur);
        }
    }
    public static void dfs (int cur) throws IOException {
        if(visit[cur])return;
        System.out.println(cur);
        visit[cur] = true;
        for (int c : cnjList[cur]) {
            int nex = c-1;
            if (!visit[nex]) {
                dfs(nex);
            }
        }
    }
}

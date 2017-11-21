
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.io.IOException;

public class Main {
    public static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    public static ArrayList<Integer>[] cnj;
    public static int[] visit;
    public static void main(String[] Args)throws IOException {
        int t = Integer.parseInt(in.readLine());
        //in testCase
        while(t!=0) {
            String[] line = in.readLine().split(" ");
            int v = Integer.parseInt(line[0]) , e= Integer.parseInt(line[1]);
            cnj = new ArrayList[v];
            for(int i=0; i<v; i++) {
                visit = new int[v];
                cnj[i] = new ArrayList();
                visit[i]=0;
            }
            for(int i=0; i<e; i++) {
            line = in.readLine().split(" ");
            int cur = Integer.parseInt(line[0])-1 , nex = Integer.parseInt(line[1])-1;
            cnj[cur].add(nex);
            cnj[nex].add(cur);
            }
            find(v);
            t--;
        }
    }
    public static boolean dfs (int cur, int flag) {
        if(visit[cur]==flag&&visit[cur]!=0)return true;
        if(visit[cur]!=flag&&visit[cur]!=0)return false;
        if(visit[cur]==0)visit[cur] = flag;
        for(int n : cnj[cur]) {
            if (!dfs(n,flag*-1)) return false;
        }
        return true;
    }
    public static void find(int v) {
            for( int node =0; node < v; node++) {
                if(visit[node] == 0) {
                    if(!dfs(node,1)) {
                        System.out.println("NO");
                        return;
                    }
                }
            }System.out.println("YES");
        
    }
}


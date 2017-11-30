package findRoot;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
class pair{
    int x;
    ArrayList <Integer> y;
    pair (int x, ArrayList<Integer> y){
        this.x=x;
        this.y=y;
    }
    
}

public class Main {
    public static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    public static ArrayList<Integer> cnj[];
    public static int [] roots ;
    public static Queue<pair> q = new LinkedList<>();
    public static int N;
    public static void main(String args[]) throws Exception{
        getInput();
        BFS(0);
//      for (int i : roots) {
//          System.out.print(i+" ");
//      } System.out.println();
        for(int i =1; i< N; i++) {
            int tmp =roots[i];
            for(int j : cnj[i]) {
                if(tmp>roots[j])System.out.println((j+1));
                
            }
        }
    }
    public static void BFS(int root) {
        q.add(new pair(1,cnj[root]));
        roots[root] =1; 
        while(!q.isEmpty()) {

            pair targets = q.poll();
            int depth = targets.x+1;
            for (int r : targets.y) {
                if(roots[r]==0) {q.add(new pair(depth,cnj[r]));
                roots[r] = depth ;
                } 
            }
        }
    }
    public static void getInput()throws Exception {
        N = Integer.parseInt(in.readLine());
        cnj = new ArrayList[N];
        for(int i =0; i< N; i++) {
            cnj[i] = new ArrayList<Integer>();
        }
        roots = new int[N];
        for (int i =0; i<N-1; i++) {
        int a, b;
        String line[] = in.readLine().split(" ");
        a= Integer.parseInt(line[0])-1; b= Integer.parseInt(line[1])-1;
        cnj[a].add(b);
        cnj[b].add(a);
        }
    
    }
}


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;

public class Main {
    public static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    public static ArrayList<Integer>[] cnj;
    public static int numOfS;
    public static int visit[];
    public static int cnt = 0;
    public static HashMap<Integer,Integer> m = new HashMap<>();
    public static void main(String args[])throws Exception {
        int t = Integer.parseInt(in.readLine());
        while(t!=0) {
            numOfS=Integer.parseInt(in.readLine());
            getInput();
            for(int i=0; i<numOfS; i++) {
            }
            for(int i =0 ; i< numOfS; i++){
                if(visit[i]==0)dfs(i,1,1);
            }
            System.out.println(numOfS-cnt);
            cnt=0;
            t--;
        }
    }
    public static void getInput() throws Exception{
        cnj = new ArrayList[numOfS];
        visit = new int[numOfS];
        for(int i =0; i< numOfS; i++) {
            visit[i] = 0;
            cnj[i] = new ArrayList<Integer>();
        }
        String line[] = in.readLine().split(" ");
        for (int i =0 ; i< numOfS ; i++) {
            int nex =Integer.parseInt(line[i])-1; 
            cnj[i].add(nex);
        }
    }
    public static void dfs(int curNd, int dfsNum, int ndCnt){
        if (visit[curNd]!=0){
            if(visit[curNd]!= dfsNum)return;
            if(m.containsKey(curNd)){
                cnt += (ndCnt - m.get(curNd));
                return;
            }
        }
        else{
            visit[curNd] = dfsNum;
            m.put(curNd, ndCnt);
            dfs(cnj[curNd].get(0),dfsNum,ndCnt+1);
            m.clear();
        }
    }
}

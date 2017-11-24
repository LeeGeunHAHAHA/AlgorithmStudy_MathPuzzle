package tomato;

import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Main {
    public static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    public static int [][] tmt;
    public static boolean [][] visit;
    public static int n , m;
    public static int dx[] = {0,1,0,-1};
    public static int dy[] = {1,0,-1,0};
    public static boolean change;
    public static int cnt=0;
    public static void main(String args[])throws Exception{
        getInput();
        do{
            find();
        }while(change);
        for(int i=0; i<n ; i++)
            for(boolean a : visit[i])
                if(a){ 
                    System.out.println(-1);
                    return;
                }
                else{ 
                    System.out.println(cnt);
                    return;
                    }
        in.close();
    }
    public static void find(){
        clean();
        for(int i =0; i< n; i++){
            for(int j =0; j<m; j++){
                if(visit[i][j]==false&&(tmt[i][j]==0||tmt[i][j]==2))DFS(i,j);
            }
        }
        test();
        if(change)cnt++;
    }
    public static boolean isSafe(int x, int y){
        return x>=0 && y>=0&& x<n && y<m;
    }
    public static void DFS(int x, int y){
        visit[x][y] = true;
        tmt[x][y] =2;
        for(int i =0; i<4; i++){
            int nx = x+dx[i];
            int ny = y+dy[i];
            if(tmt[x][y]==2&&isSafe(nx,ny)&&tmt[nx][ny]==1&&visit[nx][ny]==false){
                tmt[x][y]=1;
                change = true;
            }
        }
        for(int i =0; i<4; i++){
            int nx = x+dx[i];
            int ny = y+dy[i];
            if(isSafe(nx,ny)&&visit[nx][ny]==false&&tmt[nx][ny]==0){
                DFS(nx,ny);
            }
        }
    }
    public static void getInput()throws Exception{
        String line[] = in.readLine().split(" ");
        // m , n (6col ,4row)
        m = Integer.parseInt(line[0]);
        n = Integer.parseInt(line[1]);
        tmt = new int[n][m];
        visit = new boolean[n][m];
        for (int i =0; i< n; i++){
            line = in.readLine().split(" ");
            for(int j =0; j<m; j++){
                tmt[i][j] = Integer.parseInt(line[j]);
                visit[i][j] = false;
            }
        }
    }
    public static void clean(){
        change = false;
//      for(int i =0; i<n; i++){
//          for(int j =0; j<m; j++){
//              visit[i][j]=false;
//          }
//      }
        visit = new boolean [n][m];
    }
    public static void test(){
        for (int i =0; i<n ; i++){
            for(int j=0; j<m; j++){
                System.out.print(tmt[i][j]+" ");
            } System.out.println();
        }
        for (int i =0; i<n ; i++){
            for(int j=0; j<m; j++){
                System.out.print(visit[i][j]+" ");
            } System.out.println();
        }
    }
}

package tomato;
import java.util.*;
public class newTmt{

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int w=sc.nextInt();
        int h=sc.nextInt();
        int map[][]=new int[w][h];
        int totnum=w*h;
        ArrayList<Integer> queue=new ArrayList<Integer>();
        for(int i=0; i<h; i++) {
            for(int j=0; j<w; j++) {
                map[j][i]=sc.nextInt();
                if(map[j][i]==1) {
                    queue.add(10000*j+i);
                }else if(map[j][i]==-1) {
                    totnum--;
                }
            }
        }

        BFS(map, queue, w, h, totnum);

    }

    static void BFS(int map[][], ArrayList<Integer> queue, int w, int h, int totnum) {
        int days=-1, tottom=0;
        ArrayList<Integer> front=new ArrayList<Integer>();
        int x, y;

        while(!queue.isEmpty()) {
            days++; 
            for(int tmp:queue) {
                x=tmp/10000; y=tmp%10000;
                tottom++;

                if(x>0&&map[x-1][y]==0) {
                    map[x-1][y]=1;
                    front.add(tmp-10000);
                }
                if(x<w-1&&map[x+1][y]==0) {
                    map[x+1][y]=1;
                    front.add(tmp+10000);
                }
                if(y>0&&map[x][y-1]==0) {
                    map[x][y-1]=1;
                    front.add(tmp-1);
                }
                if(y<h-1&&map[x][y+1]==0) {
                    map[x][y+1]=1;
                    front.add(tmp+1);
                }
            }
            queue.clear();
            queue.addAll(front);
            front.clear();
        }
        if(tottom==totnum) {
            System.out.println(days);
        }else if(tottom<totnum){
            System.out.println(-1);
        }

    }
}

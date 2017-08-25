package mirrorNum;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.BufferedReader;
import java.io.BufferedWriter;
public class Main {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter x = new BufferedWriter(new OutputStreamWriter(System.out));
    static int init =11;
    public static void main(String args[]){
        boolean fin = false;
        while(!fin){
            String target = Integer.toString(init);
            String targetB = decToNum(init, 2);
            String targetC = decToNum(init, 8);
            if(isMirror(target,0,target.length()/2)&&isMirror(targetB,0,targetB.length()/2)&&isMirror(targetC,0,targetC.length()/2))fin=true;
            init+=2;
        }
        System.out.println(init-2);
    }
    public static boolean isMirror(String num, int index, int limit){
        char h = num.charAt(index);
        char t = num.charAt(num.length()-1-index);
        if(index==limit&&h==t)return true;
        if(h==t)index++;
        if(h!=t)return false;
        return isMirror(num,index,limit);
    }
    public static String decToNum(int target, int num){
        String fin="";
        int mod;
        while(target>0){
            mod = target%num;
            fin += mod;
            target/=num;
        }
        return fin;
    }

}

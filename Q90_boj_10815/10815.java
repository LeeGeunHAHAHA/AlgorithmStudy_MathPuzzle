package com.company;
import java.util.HashSet;
import java.util.function.BiFunction;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    public static HashSet<String> hs = new HashSet<>();
    public static int c;
    public static int n;
    public static void main(String[] args) throws Exception {
        c = Integer.parseInt(in.readLine());
        String cards[] = in.readLine().split(" ");
        for(String i :  cards){
            hs.add(i) ;
        }
        n = Integer.parseInt(in.readLine());
        String targets[] = in.readLine().split(" ");
        for (String i : targets){
            System.out.print((hs.contains(i) ? 1 : 0) + " ");
        }
    }
}

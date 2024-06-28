using System;
using System.Text;
using System.Collections.Generic;

namespace baek
{
    class Program
    {
        static int[,] graph = new int[102,102];
        static int[] dirX = {1,0,-1,0};
        static int[] dirY = {0,-1,0,1};
        static void Main()
        {
            int[] input = Array.ConvertAll(Console.ReadLine().Split(),int.Parse);
            int N = input[0];
            int M = input[1];

            for(int i=1;i<=N;i++)
            {
                string maze = Console.ReadLine();
                int index = 1;
                foreach(char s in maze)
                {
                    graph[i,index++]=s-'0';
                }
            }
            BFS(1,1);
            Console.Write(graph[N,M]);
        }

        public static void BFS(int x, int y)
        {
            Queue<Tuple<int,int>> myQ = new Queue<Tuple<int,int>>();
            myQ.Enqueue(new Tuple<int,int>(x,y));

            while(myQ.Count>0)
            {
                Tuple<int,int> now = myQ.Dequeue();
                for(int i=0;i<4;i++)
                {
                    int nextX = now.Item1 + dirX[i];
                    int nextY = now.Item2 + dirY[i];
                    if(graph[nextX,nextY]==0||(nextX==1&&nextY==1)) continue;
                    if(graph[nextX,nextY]==1) 
                    {
                        graph[nextX,nextY]=graph[now.Item1,now.Item2]+1;
                        myQ.Enqueue(new Tuple<int,int>(nextX,nextY));
                    } 
                }
            }
            
        }
    }
}
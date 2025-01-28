class Program  
{  
    static int getDistance(List<int> list1, List<int> list2) {
        list1.Sort();
        list2.Sort();
        int sum = 0;

        for (int i = 0; i < list1.Count; i++) {
            int distance = Math.Abs(list1[i] - list2[i]);
            sum += distance;
        }

        return sum;
    }


    static int getSimilarityScore(List<int> a, List<int> b) {
        Dictionary<int, int> counter = new Dictionary<int, int>();
        int score = 0;

        foreach (int num in b) {
            if (counter.ContainsKey(num)) {
                counter[num] += 1;
            } else {
                counter.Add(num, 1);
            }
        }

        foreach (int num in a) {
            if (counter.ContainsKey(num)) {
                score += num * counter[num];
            }
        }

        return score;
    }

    static void Main()  
    {  
        List<int> list1 = new List<int>{3, 4, 2, 1, 3, 3};
        List<int> list2 = new List<int>{4, 3, 5, 3, 9, 3};

        Console.WriteLine(Program.getDistance(list1, list2));
        Console.WriteLine(Program.getSimilarityScore(list1, list2));

        IEnumerable<string> lines = File.ReadLines("input.txt");


        list1 = new List<int>{};
        list2 = new List<int>{};

        foreach (string line in lines) {
            var tokens = line.Split("   ");
            int a = Int32.Parse(tokens[0]);
            int b = Int32.Parse(tokens[1]);
            list1.Add(a);
            list2.Add(b);
        }

        Console.WriteLine(Program.getDistance(list1, list2));
        Console.WriteLine(Program.getSimilarityScore(list1, list2));
    }  
}  

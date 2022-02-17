using System;
using System.Collections.Generic;
using System.Text;

namespace qwerty_keyboard_challenge
{
    public static class qwertyTyper
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Starting up");
            string[][] qwertyKeyboard = new string[3][];
            qwertyKeyboard[0] = new string[] { "q", "w", "e", "r", "t", "y", "u", "i", "o", "p" };
            qwertyKeyboard[1] = new string[] { "a", "s", "d", "f", "g", "h", "j", "k", "l" };
            qwertyKeyboard[2] = new string[] { "z", "x", "c", "v", "b", "n", "m" };
            WordFinder("car", qwertyKeyboard);
            
        }

        public static void WordFinder(string word, string[][] board)
        {
            StringBuilder builder = new StringBuilder();
            
            Dictionary<string, Tuple<int, int>> seenValues = new Dictionary<string, Tuple<int, int>>();
            for (int row = 0; row < board.Length; row++)
            {
                for (int col = 0; col < board[row].Length; col++)
                {
                    var letter = board[row][col].ToString();
                    seenValues.Add(letter, new Tuple<int, int>(row, col));
                }
            }
            Tuple<int, int> prev_cord = new(0,0);
            for (int i = 0; i < word.Length; i++)
            {
                var letter = word[i].ToString();
                var coordinates = seenValues[letter];
                var cord_x = coordinates.Item1;
                var cord_y = coordinates.Item2;
                var difference_x = cord_x - prev_cord.Item1;
                var difference_y = cord_y - prev_cord.Item2;
                string direction_vert = string.Concat(Enumerable.Repeat(difference_x >= 0 ? "down " : "up ", difference_x < 0 ? difference_x * -1 : difference_x));
                string direction_hori = string.Concat(Enumerable.Repeat(difference_y >= 0 ? "right " : "left ", difference_y < 0 ? difference_y * -1 : difference_y));
                builder.Append(direction_vert);
                builder.Append(direction_hori);
                builder.Append("select ");
                prev_cord = new(cord_x, cord_y);
            }
            var result = builder.ToString();
            Console.WriteLine(result);
        }
    }
}
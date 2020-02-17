using System;
using System.Text.RegularExpressions;

public class RegexTest {
    public static void Main() {
        string regex = "\\d";
        string searchTarget = "Luke Skywarker 02-123-4567 luke@daum.net\n다스베이더 070-9999-9999 darth_vader@gmail.com\nprincess leia 010 2454 3457 leia@gmail.com";

        foreach (Match m in Regex.Matches(searchTarget, regex)){
            Console.WriteLine(m.Value);
        }
    }
}
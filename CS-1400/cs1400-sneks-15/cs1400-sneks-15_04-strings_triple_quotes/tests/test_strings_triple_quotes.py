import ast
import unittest

import asttest

# Original text from: https://pastebin.com/raw/V7tWn1Rj
class TestStringsTripleQuotes(asttest.ASTTest):

    def setUp(self):
        super().setUp("strings_triple_quotes.py")

    def test_required_syntax(self):
        if ("'''" not in self.file) and ('"""' not in self.file):
            self.fail("Make sure you are using triple quoted strings!")

    def test_correct_result(self):
        self.exec_solution()
        sol="""                             ;\.
                            |' \.
         _                  ; : ;
        / `-.              /: : |
       |  ,-.`-.          ,': : |
       \  :  `. `.       ,'-. : |
        \ ;    ;  `-.__,'    `-.|
         \ ;   ;  :::  ,::'`:.  `.
          \ `-. :  `    :.    `.  `
           \   \    ,   ;   ,:    (o
            \   :., :.    ,'o)): ` `-.
           ,/,' ;' ,::"'`.`---'   `.  `-._
         ,/  :  ; '"      `;'          ,--`.
        ;/   :; ;             ,:'     (   ,:)
          ,.,:.    ; ,:.,  ,-._ `.     \""'/
          '::'     `:'`  ,'(  \`._____.-'"'
             ;,   ;  `.  `. `._`-.  \\
             ;:.  ;:       `-._`-.\  \`.
              '`:. :        |' `. `\  ) )
      Bark!      ` ;:       |    `--\__,'
                   '`      ,'
                        ,-"""
        self.assertGreaterEqual(len(self.printed_lines), 1, "You are printing "
                "the wrong number of lines.")
        output = self.printed_lines[0]
        self.assertNotEqual(sol.strip(), output, "Make sure you have not "
                "removed any of the whitespace around the image.")
        #self.assertIn(sol.strip(), output, "Make sure you have not "
                #"removed any of the text from the image.")
        #characters = len(sol) - len(output)
        #self.assertLessEqual(characters, 0, "You are not printing the right "
                #"text. Double check that you did not accidentally remove any "
                #"characters."+str(len(output))+str(len(sol)))
        #self.assertGreaterEqual(characters, 0, "You are not printing the right"
                #" text. Double check that you did not accidentally add any "
                #"whitespace or characters.")
        self.assertIn(sol, output, "Somehow, you are not printing the "
                "right text. Double check that you did not change any "
                "characters.")

if __name__ == "__main__":
    unittest.main()

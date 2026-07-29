class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s= []

        for token in tokens:
            
            if token.lstrip('-+').isdigit():
                s.append(int(token))
                
            else:
                op = token

                n1,n2=s.pop(),s.pop()

                match op:
                    case '+':
                        s.append(n1+n2)
                    case '-':
                        s.append(n2-n1)
                    case '*':
                        s.append(n1*n2)
                    case '/':
                        s.append(int(n2/n1))
               
                       
        if len(s):
            return s.pop()
        return 0